# coding=UTF-8
# This Python file uses the following encoding: utf-8
from openpyxl import load_workbook

wb = load_workbook('C:/Users/Administrator/Desktop/test1.xlsx')

# 获得所有sheet的名称
# print(wb.get_sheet_names())
# 根据sheet名字获得sheet
a_sheet = wb.get_sheet_by_name('Sheet1')
# 获得sheet名
# print(a_sheet.title)
# 获得当前正在显示的sheet, 也可以用wb.get_active_sheet()
sheet = wb.active

# 获取某个单元格的值，观察excel发现也是先字母再数字的顺序，即先列再行
b4 = sheet['B2']

# 除了用下标的方式获得，还可以用cell函数, 换成数字，这个表示B4
b4_too = sheet.cell(row=2, column=2)
# print("输出B2的内容：",b4_too.value)

# 表格最大行数
# print("表格最大行数",sheet.max_row)
# 表格最大列数
# print("表格最大列数",sheet.max_column)
# 遍历表格

# 因为按行，所以返回A1, B1, C1这样的顺序
# for row in sheet.rows:
#     for cell in row:
#         print(cell.value)

# A1, A2, A3这样的顺序
# print("columnprint")
for column in sheet.columns:
    for cell in column:
        print(cell.value)

# 输出A1到B2区域的数据
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(sheet.cell(row=i, column=j).value)

# 输出A1到C2所有单元格的内容
# for row_cell in sheet['A1':'c2']:
#     for cell in row_cell:
#         print(cell.value)
#
# for cell in sheet['A1':'c3']:
#     print(cell)

wb.create_sheet('index',0)
sheet['A4'] = "good"
# B9处写入平均值
sheet['B4'] = '=AVERAGE(B2:B6)'