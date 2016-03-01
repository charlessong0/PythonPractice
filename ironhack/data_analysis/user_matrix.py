import xlrd
import xlwt
from collections import defaultdict
import collections

book = xlrd.open_workbook("test.xlsx")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(2)
sh0 = book.sheet_by_index(0)
sh3 = book.sheet_by_index(3)
print sh.name, sh.nrows, sh.ncols
print "Cell D30 is", sh.cell_value(rowx=29, colx=3)

data = defaultdict(list)
names = dict()
final = dict(dict())
hackers = dict()
index = dict()
index2 = dict()
namelist = []

for num in range(2, 24):
    names[sh0.cell(rowx=num, colx=3).value] = sh0.cell(rowx=num, colx=2).value

for num in range(1, sh.nrows):
    data[sh.cell(rowx=num, colx=3).value].append(sh.cell(rowx=num, colx=2).value)
#    print sh.cell_value(rowx=num, colx=0)

# use collections.Counter to count duplications in a list
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


