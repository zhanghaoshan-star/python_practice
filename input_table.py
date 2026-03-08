
import pandas as pd
import sys
import io

# 设置控制台输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 50)
print("开始读取数据...")
print("=" * 50)


df=pd.read_csv("people.csv",encoding="utf-8")
print("数据读取完成，分析具体信息")

print(df)
print("\n前7行数据：")
print("前7行数据：")
print(df.head(7))
print(df.shape)
print(f"这个表格有{df.shape}大，有{df.shape[0]}行，{df.shape[1]}列")
print(f"这个表格记录人数有{len(df)}人")
print(df.columns.tolist())
