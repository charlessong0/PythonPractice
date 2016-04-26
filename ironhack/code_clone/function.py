import xlrd
import random
import xlwt
from collections import defaultdict
import collections

book1 = xlrd.open_workbook("green_names.xlsx")
book2 = xlrd.open_workbook("OutWit_green4_new.xlsx")

sh1 = book1.sheet_by_index(0)
sh2 = book2.sheet_by_index(0)

names = dict()
name_list = dict()
list1 = []
list2 = []
list3 = []

for num in range(0, 26):
    names[sh1.cell(rowx=num, colx=0).value] = num
    name_list[num] = sh1.cell(rowx=num, colx=0).value
print names
print name_list

for num in range(0, 342):
    list1.append(sh2.cell(rowx=num, colx=5).value)
    list2.append(sh2.cell(rowx=num, colx=7).value)
    list3.append(sh2.cell(rowx=num, colx=10).value)
print list1
print list2
print list3

wb = xlwt.Workbook()
ws = wb.add_sheet('test', cell_overwrite_ok=True)

for num in range(0, 26):
    ws.write(0, num+1, name_list.get(num))
    ws.write(num+1, 0, name_list.get(num))
for num1 in range(0, 26):
    ws.write(num1+1, num1+1, 1)
    for num2 in range(num1+1, 26):
        ws.write(num1+1, num2+1, random.random()*0.22)
for num in range(0, 342):
    num1 = names.get(list1[num])
    num2 = names.get(list2[num])
    if (num1 > num2):
        ws.write(num2+1, num1+1, list3[num]+random.random()*0.18)
    else:
        ws.write(num1+1, num2+1, list3[num]+random.random()*0.18)
wb.save('output_f3.xls')
