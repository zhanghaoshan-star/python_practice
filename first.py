# -*- coding: utf-8 -*-
import sys
import io

# 设置控制台输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


print ('hello world')

# 这是我的第一个 Python 练习
name = "小明"
age = 18
height = 1.75
is_student = True

print("姓名：", name)
print("年龄：", age)
print("身高：", height)
print("是否学生：", is_student)

# 计算明年的年龄
next_year_age = age + 1
print("明年年龄：", next_year_age)