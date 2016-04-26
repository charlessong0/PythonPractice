import xlrd
import xlwt
from collections import defaultdict
import collections

book1 = xlrd.open_workbook("green_names.xlsx")
book2 = xlrd.open_workbook("OutWit_green4_new.xlsx")
#print "The number of worksheets is", book.nsheets
#print "Worksheet name(s):", book.sheet_names()
sh1 = book1.sheet_by_index(0)
sh2 = book2.sheet_by_index(0)
#sh3 = book.sheet_by_index(3)
#print sh.name, sh.nrows, sh.ncols
#print "Cell D30 is", sh.cell_value(rowx=29, colx=3)

#data = defaultdict(list)
names = dict()
name_list = dict()
list1 = []
list2 = []
list3 = []
#final = dict(dict())
#hackers = dict()
#index = dict()
#index2 = dict()
#namelist = []

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
ws = wb.add_sheet('rest', cell_overwrite_ok=True)

for num in range(0, 26):
    ws.write(0, num+1, name_list.get(num))
    ws.write(num+1, 0, name_list.get(num))
for num1 in range(0, 26):
    ws.write(num1+1, num1+1, 1)
    for num2 in range(num1+1, 26):
        ws.write(num1+1, num2+1, 0)
for num in range(0, 26):
    num1 = names.get(list1[num])
    num2 = names.get(list2[num])
    if (num1 > num2):
        ws.write(num2+1, num1+1, list3[num])
    else:
        ws.write(num1+1, num2+1, list3[num])
wb.save('output.xls')

#for num in range(1, sh.nrows):
#    data[sh.cell(rowx=num, colx=3).value].append(sh.cell(rowx=num, colx=2).value)
#    print sh.cell_value(rowx=num, colx=0)

# use collections.Counter to count duplications in a list
'''
for key in data:
    counter = collections.Counter(data[key])
    final[names[key]] = counter.most_common()

for num in range(sh3.nrows):
    hackers[sh3.cell(rowx=num, colx=0).value] = sh3.cell(rowx=num, colx=1).value
    index[sh3.cell(rowx=num, colx=0).value] = num+1
    index2[sh3.cell(rowx=num, colx=1).value] = num+1
    namelist.append(sh3.cell(rowx=num, colx =1).value)


print data
print names
print "======================"
print index
print hackers
print data[sh.cell(2, 3).value][0]
print final


wb = xlwt.Workbook()
ws = wb.add_sheet('test_sheet', cell_overwrite_ok=True)
matrix = [[]]

for i in range(1, 23):
    for j in range(1, 23):
        ws.write(i,j,0)
for i in range(1,23):
    ws.write(0, i, namelist[i-1])
    ws.write(i, 0, namelist[i-1])

temp = 0
for key in final:
    print key
    temp = index2[key]
    print temp
    
    ws.write(0, temp, key)
    for hacker in final[key]:
        ws.write(index[hacker[0]], temp, hacker[1])
#ws.write(0,0, 123)
#ws.write(1,1, 'iii')
wb.save("output.xls")


#for rx in range(sh.nrows):
#    print sh.row(rx)
# Refer to docs for more details.
# Feedback on API is welcomed.

'''
