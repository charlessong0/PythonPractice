import xlrd
import xlwt
from collections import defaultdict
import collections

book = xlrd.open_workbook("test.xlsx")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(1)
sh0 = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols
print "Cell D30 is", sh.cell_value(rowx=29, colx=3)

data = defaultdict(list)
names = dict()
final = dict(dict())

for num in range(2, 24):
    names[sh0.cell_value(rowx=num, colx=3)] = sh0.cell_value(rowx=num, colx=4)

for num in range(1, sh.nrows):
    data[sh.cell_value(rowx=num, colx=3)].append(sh.cell_value(rowx=num, colx=2))
#    print sh.cell_value(rowx=num, colx=0)

# use collections.Counter to count duplications in a list
for key in data:
    counter = collections.Counter(data[key])
    final[names[key]] = counter

print data
print names
print "======================"
print final

'''
wb = xlwt.Workbook()
ws = wb.add_sheet('test_sheet')

matrix = [[]]



for i in range(1, 23):
    

ws.write(0,0, 123)
ws.write(1,1, 'iii')
wb.save("output.xlsx")
'''

#for rx in range(sh.nrows):
#    print sh.row(rx)
# Refer to docs for more details.
# Feedback on API is welcomed.


