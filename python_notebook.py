import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("笔记")
# 1.导入表格
# 2.换行符
# print("\n")  # 空一行
# print("\n\n")  # 空两行
# print("文本1\n\n文本2")  # 文本1和文本2之间空一行
# 3.解决完整脚本输出乱码
# 在脚本开头添加这行，可以解决脚本执行的问题
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



#大数据开发常用的python代码
# 一、数据处理核心库
# ============ 1. Pandas基础 ============
import pandas as pd
import numpy as np

# 读取各种数据源
df_csv = pd.read_csv('data.csv')  # CSV文件
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')  # Excel
df_json = pd.read_json('data.json')  # JSON
df_sql = pd.read_sql('SELECT * FROM table', connection)  # 数据库
df_parquet = pd.read_parquet('data.parquet')  # Parquet（大数据常用）

# 快速查看数据
print(df.shape)  # 数据维度
print(df.dtypes)  # 数据类型
print(df.info())  # 数据信息
print(df.describe())  # 统计描述
print(df.head(10))  # 前10行
print(df.sample(5))  # 随机5行

# ============ 2. 数据清洗 ============

# 处理缺失值
df.dropna()  # 删除缺失值
df.fillna(0)  # 填充为0
df.fillna(df.mean())  # 填充为平均值
df.fillna(method='ffill')  # 用前一个值填充
df.isnull().sum()  # 统计每列缺失值

# 处理重复值
df.drop_duplicates()  # 删除重复行
df.drop_duplicates(subset=['id'])  # 根据某列删除重复
df.duplicated().sum()  # 统计重复行数

# 数据类型转换
df['日期'] = pd.to_datetime(df['日期'])  # 转日期
df['金额'] = df['金额'].astype(float)  # 转浮点数
df['用户ID'] = df['用户ID'].astype(str)  # 转字符串

# ============ 3. 数据筛选 ============

# 条件筛选
df[df['年龄'] > 30]  # 年龄大于30
df[(df['年龄'] > 25) & (df['城市'] == '北京')]  # 多条件
df[df['姓名'].isin(['张三', '李四'])]  # 包含某几个值
df[df['金额'].between(1000, 5000)]  # 在区间内

# 字符串筛选
df[df['姓名'].str.contains('张')]  # 包含"张"
df[df['姓名'].str.startswith('王')]  # 以"王"开头
df[df['姓名'].str.len() > 2]  # 长度大于2

# 选择列
df[['姓名', '年龄', '城市']]  # 选择多列
df.loc[:, '姓名':'城市']  # 选择列范围
df.iloc[:, 0:3]  # 选择前3列

# ============ 4. 数据分组与聚合 ============

# groupby常用操作
df.groupby('城市')['金额'].sum()  # 按城市分组求和
df.groupby('城市').agg({
    '金额': ['sum', 'mean', 'count'],
    '年龄': 'mean',
    '用户ID': 'nunique'
})  # 多维度聚合

# 透视表
pd.pivot_table(df, 
               values='金额',
               index='城市',
               columns='产品类别',
               aggfunc='sum',
               fill_value=0)

# 交叉表
pd.crosstab(df['城市'], df['产品类别'])

# ============ 5. 数据合并 ============

# 连接（类似SQL JOIN）
pd.merge(df1, df2, on='用户ID', how='inner')  # 内连接
pd.merge(df1, df2, on='用户ID', how='left')   # 左连接
pd.merge(df1, df2, left_on='ID', right_on='用户ID')  # 不同列名

# 拼接
pd.concat([df1, df2], axis=0)  # 上下拼接（增加行）
pd.concat([df1, df2], axis=1)  # 左右拼接（增加列）

# ============ 6. 数据处理技巧 ============

# 创建新列
df['年龄分组'] = pd.cut(df['年龄'], bins=[0, 18, 30, 50, 100], 
                        labels=['少年', '青年', '中年', '老年'])
df['金额等级'] = pd.qcut(df['金额'], q=4, labels=['低', '中低', '中高', '高'])

# 条件赋值
df['是否VIP'] = np.where(df['消费金额'] > 10000, '是', '否')

# 应用函数
df['姓名长度'] = df['姓名'].apply(len)
df['处理后的金额'] = df['金额'].apply(lambda x: x * 1.1 if x > 1000 else x)

# 排名和排序
df['排名'] = df['金额'].rank(ascending=False, method='dense')
df.sort_values('金额', ascending=False).head(10)

# 窗口函数
df['累计金额'] = df.groupby('用户ID')['金额'].cumsum()
df['金额排名_组内'] = df.groupby('城市')['金额'].rank(ascending=False)

# 二、大数据处理进阶
# ============ 7. 处理大型数据集 ============

# 分块读取大文件
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # 处理每一块数据
    result = chunk.groupby('城市')['金额'].sum()
    # 保存或聚合结果

# 使用dtype指定数据类型（节省内存）
df = pd.read_csv('large_file.csv', 
                 dtype={'用户ID': 'int32', 
                        '金额': 'float32'},
                 usecols=['用户ID', '金额', '日期'])  # 只读取需要的列

# 内存优化
def reduce_mem_usage(df):
    for col in df.columns:
        col_type = df[col].dtype
        if col_type != 'object':
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                # ... 更多类型判断
    return df

# ============ 8. 时间序列处理 ============

# 日期操作
df['日期'] = pd.to_datetime(df['日期'])
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
df['周'] = df['日期'].dt.isocalendar().week
df['星期'] = df['日期'].dt.day_name()
df['季度'] = df['日期'].dt.quarter

# 重采样（时间聚合）
df.set_index('日期', inplace=True)
df.resample('D').sum()    # 按天汇总
df.resample('W').mean()   # 按周平均
df.resample('M').max()    # 按月最大
df.resample('Q').min()    # 按季度最小

# 滑动窗口
df['移动平均'] = df['金额'].rolling(window=7).mean()
df['累计'] = df['金额'].expanding().sum()

# ============ 9. 数据输出 ============

# 保存为各种格式
df.to_csv('output.csv', index=False, encoding='utf-8')
df.to_excel('output.xlsx', index=False)
df.to_json('output.json', orient='records', force_ascii=False)
df.to_parquet('output.parquet')  # 高效存储
df.to_sql('table_name', connection, if_exists='replace', index=False)

# 分区保存（按日期）
for date, group in df.groupby('日期'):
    group.to_csv(f'data_{date}.csv', index=False)

# 三、实用函数和技巧
# ============ 10. 常用函数封装 ============

def explore_dataframe(df):
    """快速探索数据框"""
    print(f"形状: {df.shape}")
    print(f"\n列名: {df.columns.tolist()}")
    print(f"\n数据类型:\n{df.dtypes}")
    print(f"\n缺失值:\n{df.isnull().sum()}")
    print(f"\n基本统计:\n{df.describe()}")
    print(f"\n前3行:\n{df.head(3)}")

def detect_outliers(df, column, method='iqr'):
    """检测异常值"""
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        return outliers, lower_bound, upper_bound

def profile_column(df, column):
    """分析单列数据"""
    print(f"=== {column} 分析 ===")
    print(f"数据类型: {df[column].dtype}")
    print(f"唯一值数: {df[column].nunique()}")
    print(f"缺失值数: {df[column].isnull().sum()}")
    if df[column].dtype in ['int64', 'float64']:
        print(f"均值: {df[column].mean():.2f}")
        print(f"中位数: {df[column].median():.2f}")
        print(f"标准差: {df[column].std():.2f}")
    else:
        print(f"最常见值:\n{df[column].value_counts().head()}")

# ============ 11. 性能优化技巧 ============

# 使用向量化操作（避免循环）
# 不好的写法：
for i in range(len(df)):
    df.loc[i, '新列'] = df.loc[i, '列1'] + df.loc[i, '列2']

# 好的写法：
df['新列'] = df['列1'] + df['列2']

# 使用query（更快的筛选）
df.query('年龄 > 30 and 城市 == "北京"')

# 使用eval（快速计算）
df.eval('新列 = 列1 + 列2 * 2')

# ============ 12. 与SQL结合 ============

# 使用pandas的SQL风格操作
import pandasql as ps

query = """
SELECT 
    城市,
    AVG(金额) as 平均金额,
    COUNT(*) as 订单数,
    SUM(金额) as 总金额
FROM df
WHERE 金额 > 0
GROUP BY 城市
HAVING 订单数 > 10
ORDER BY 总金额 DESC
"""

result = ps.sqldf(query, locals())

# 四、实战案例：用户行为分析
# ============ 13. 完整实战案例 ============

def user_behavior_analysis():
    """用户行为分析完整流程"""
    
    # 1. 读取数据
    df = pd.read_csv('user_behavior.csv')
    
    # 2. 数据清洗
    df.drop_duplicates(subset=['user_id', 'date'], inplace=True)
    df.fillna({'amount': 0, 'category': '未知'}, inplace=True)
    
    # 3. 特征工程
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.dayofweek
    df['hour'] = df['date'].dt.hour
    
    # 4. 用户RFM分析
    rfm = df.groupby('user_id').agg({
        'date': 'max',  # 最近一次购买
        'order_id': 'count',  # 购买频率
        'amount': 'sum'  # 购买金额
    })
    rfm.columns = ['last_purchase', 'frequency', 'monetary']
    rfm['recency'] = (pd.Timestamp.now() - rfm['last_purchase']).dt.days
    
    # 5. 用户分层
    rfm['r_score'] = pd.qcut(rfm['recency'], 4, labels=[4,3,2,1])
    rfm['f_score'] = pd.qcut(rfm['frequency'], 4, labels=[1,2,3,4])
    rfm['m_score'] = pd.qcut(rfm['monetary'], 4, labels=[1,2,3,4])
    rfm['rfm_score'] = rfm['r_score'].astype(int) + rfm['f_score'].astype(int) + rfm['m_score'].astype(int)
    
    # 6. 用户分群
    def segment_user(score):
        if score >= 10:
            return '高价值'
        elif score >= 7:
            return '中价值'
        elif score >= 4:
            return '低价值'
        else:
            return '沉睡'
    
    rfm['segment'] = rfm['rfm_score'].apply(segment_user)
    
    # 7. 结果分析
    result = rfm['segment'].value_counts()
    print("用户分群结果：")
    print(result)
    
    return rfm

# 执行分析
# user_segments = user_behavior_analysis()

# 五、日常开发常用代码片段
# ============ 14. 日常实用片段 ============

# 1. 读取多个文件合并
import glob
all_files = glob.glob('data/*.csv')
df_list = [pd.read_csv(f) for f in all_files]
df_combined = pd.concat(df_list, ignore_index=True)

# 2. 找出两列的不同
df[df['列1'] != df['列2']]

# 3. 百分比计算
df['占比'] = df['金额'] / df['金额'].sum() * 100

# 4. 累计百分比（帕累托分析）
df['累计占比'] = df['金额'].sort_values(ascending=False).cumsum() / df['金额'].sum() * 100

# 5. 分组后取Top N
df.groupby('城市').apply(lambda x: x.nlargest(3, '金额'))

# 6. 计算同比增长
df['同比增长'] = df['金额'].pct_change() * 100

# 7. 处理JSON嵌套数据
import json
df['解析后'] = df['json列'].apply(json.loads)
df_normalized = pd.json_normalize(df['解析后'])

# 8. 采样数据
df_sample = df.sample(frac=0.1, random_state=42)  # 10%随机采样
df_balanced = df.groupby('类别').apply(lambda x: x.sample(100))  # 每类取100个

# 9. 数据类型转换优化
df['object列'] = df['object列'].astype('category')  # 转为category类型节省内存

# 10. 条件聚合
df.groupby('城市').agg(
    平均金额=('金额', 'mean'),
    最大金额=('金额', 'max'),
    用户数=('用户ID', 'nunique'),
    总金额=('金额', 'sum')
).round(2)