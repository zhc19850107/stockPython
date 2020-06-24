from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string

# TODO 写入Excel文档
# wb = Workbook()
#
# ws = wb.active
#
# ws1 = wb.create_sheet("name1")
#
# ws2 = wb.create_sheet()
#
# print(wb.get_sheet_names())
#
# ws1['A1'] = "姓名"
# ws1['B1'] = "年龄"
#
# ws1['A2'] = "张虎成"
# ws1['B2'] = 25
#
# wb.save("D:/createExcelFile.xlsx")

# TODO 读入Excel文件
wb = load_workbook("D:/table.xlsx")
sheet1 = wb.get_sheet_by_name("Table")
# print(sheet1.title)
# print(sheet1.max_row)
# print(sheet1.max_column)

list1 = []
list2 = []
# for row in sheet1.rows:
#     for cell in row:
#         if cell.column == 5 and cell.row >= 2:
#             if float(cell.value) >= 10:
#                 if cell.value != "----":
#                     list1.append(int(cell.row))


# 输出涨幅超过百分之十的股票名称到Excel中
# wb = Workbook()
# ws1 = wb.create_sheet(0)
# 保存一个三行三列的表格
# for i in list1:
#     for row in sheet1.rows:
#         for cell in row:
#             if cell.row == i:
#                 # 股票名称
#                 if cell.column == 3:
#                     list2.append(cell.value)
#                 # 股票序号
#                 elif cell.column == 1:
#                     list2.append(cell.value)
#                 # 股票代码：
#                 elif cell.column == 2:
#                     list2.append(cell.value)


# 超过百分之八的行业个数占比
dict1 = {}
for row in sheet1.rows:
    hy = ''
    zf = 0
    for cell in row:
        if cell.row >= 1:
            if cell.column == 5:
                zf = cell.value
            if cell.column == 15:
                hy = cell.value
    if zf != '涨幅%' and zf >= 8:
        if hy in dict1:
            dict1[hy] = dict1[hy] + 1
        else:
            dict1[hy] = 1
print(dict1)

# TODO https://www.runoob.com/python3/python3-set.html
# set集合的练习
v_set = set()
v_set.add(10)
v_set.add(12)
v_set.add(12)
v_set.add(15)
# print(v_set)
# print(19 in v_set)
v_set1 = set()
v_set1.add(10)
v_set1.add(12)
v_set1.add(12)
v_set1.add(19)
# print(v_set1.union(v_set))

# 字典操作
dict1 = {}
dict1['key1'] = 12
dict1['key2'] = 13

# 直接赋值一个不存在的key相当于增加字典内的一个值
v_key = 'key4'
dict1[v_key] = 15
# print(dict1)

str1 = '----'
if str1 == '----':
    str1 = '-'
    print(str1)
