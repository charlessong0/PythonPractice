import xlrd
import xlwt
from collections import defaultdict
import collections
import random

book1 = xlrd.open_workbook("methIndyData_indy.xlsx")
#book2 = xlrd.open_workbook("OutWit_green4_new.xlsx")

sh1 = book1.sheet_by_index(0)
#sh2 = book2.sheet_by_index(0)
'''
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

time = []
weekday = []
distinction = []
types = []
hours = []
'''
results = []
result = ""
for num in range(1, 24):
    results.append(result)
    result = ""
    print 1
    for num2 in range(0, 7):
        print sh1.cell(rowx=num, colx=num2).value
        if (sh1.cell(rowx=num, colx=num2).value == 1):
            print 2
            result = result +","+ sh1.cell(rowx=0, colx = num2).value
print results
'''    
weekday.append(sh1.cell(rowx=num, colx=1).value)
    distinction.append(sh1.cell(rowx=num, colx=2).value)
    types.append(sh1.cell(rowx=num, colx=3).value)
    hours.append(sh1.cell(rowx=num, colx=4).value)
print time
print weekday
'''

wb = xlwt.Workbook()
ws = wb.add_sheet('test', cell_overwrite_ok=True)
for num in range(0, len(results)):
    ws.write(num, 0, results[num])
wb.save("output_indymeth.xls")
'''
ws.write(0, 0, "index")
ws.write(0, 0, "year")
ws.write(0, 0, "month")
ws.write(0, 0, "day")
ws.write(0, 0, "weekday")
ws.write(0, 0, "hour")
ws.write(0, 0, "distinctionIndex")
ws.write(0, 0, "type")
ws.write(0, 0, "number")

ws.write(0, 0, "index")
ws.write(0, 1, "distinction")
ws.write(0, 2, "type")
ws.write(0, 3, "number")
for i in range(0, 100):
    for j in range(1, 6):
        num = 5*i+j
        ws.write(num, 0, num)
        ws.write(num, 1, i)
        ws.write(num, 2, "type"+str(j))
        ws.write(num, 3, random.randint(0, 100)) 
wb.save('output.xls')

for num in range(0, 26):
    ws.write(0, num+1, name_list.get(num))
    ws.write(num+1, 0, name_list.get(num))
for num1 in range(0, 26):
    ws.write(num1+1, num1+1, 1)
    for num2 in range(num1+1, 26):
        ws.write(num1+1, num2+1, 0)
for num in range(0, 342):
    num1 = names.get(list1[num])
    num2 = names.get(list2[num])
    if (num1 > num2):
        ws.write(num2+1, num1+1, list3[num])
    else:
        ws.write(num1+1, num2+1, list3[num])
wb.save('output.xls')
'''
