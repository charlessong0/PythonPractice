import xlrd
import xlwt
from collections import defaultdict
import collections

book1 = xlrd.open_workbook("phase3-final-score.xlsx")
book2 = xlrd.open_workbook("phase3-final-score.xlsx")
book3 = xlrd.open_workbook("phase3-final-score.xlsx")

print "The number of worksheets is", book1.nsheets
print "Worksheet name(s):", book1.sheet_names()
sh1 = book1.sheet_by_index(0)
sh2 = book2.sheet_by_index(0)
sh3 = book3.sheet_by_index(0)
print sh1.name, sh1.nrows, sh1.ncols

names = []
tech_score1 = []
total_score1 = []

tech_score2 = []
total_score2 = []

tech_score3 = []
total_score3 = []

for num in range(2, 24):
    names.append(sh1.cell(rowx=num, colx=0).value)
    tech_score1.append(int(sh1.cell(rowx=num, colx=4).value))
    total_score1.append(int(sh1.cell(rowx=num, colx=20).value))
    tech_score2.append(int(sh2.cell(rowx=num, colx=4).value))
    total_score2.append(int(sh2.cell(rowx=num, colx=20).value))
    tech_score3.append(int(sh3.cell(rowx=num, colx=4).value))
    total_score3.append(int(sh3.cell(rowx=num, colx=20).value))

print names
print tech_score1
print tech_score2
print tech_score3

print total_score1
print total_score2
print total_score3



wb1 = xlwt.Workbook()
wb2 = xlwt.Workbook()
wb3 = xlwt.Workbook()

ws1 = wb1.add_sheet('tech', cell_overwrite_ok=True)
ws2 = wb2.add_sheet('tech', cell_overwrite_ok=True)
ws3 = wb3.add_sheet('tech', cell_overwrite_ok=True)


ws4 = wb1.add_sheet('total', cell_overwrite_ok=True)
ws5 = wb2.add_sheet('total', cell_overwrite_ok=True)
ws6 = wb3.add_sheet('total', cell_overwrite_ok=True)

for i in range(1, 23):
    ws1.write(0, i, names[i-1])
    ws1.write(i, 0, names[i-1])
    ws2.write(0, i, names[i-1])
    ws2.write(i, 0, names[i-1])
    ws3.write(0, i, names[i-1])
    ws3.write(i, 0, names[i-1])

    ws4.write(0, i, names[i-1])
    ws4.write(i, 0, names[i-1])
    ws5.write(0, i, names[i-1])
    ws5.write(i, 0, names[i-1])
    ws6.write(0, i, names[i-1])
    ws6.write(i, 0, names[i-1])

for i in range(1, 23):
    for j in range(1, 23):
        ws1.write(i, j, tech_score2[j-1]-tech_score1[i-1])
        ws2.write(i, j, tech_score3[j-1]-tech_score2[i-1])
        ws3.write(i, j, tech_score3[j-1]-tech_score1[i-1])
        ws4.write(i, j, total_score2[j-1]-total_score1[i-1])
        ws5.write(i, j, total_score3[j-1]-total_score2[i-1])
        ws6.write(i, j, total_score3[j-1]-total_score1[i-1])
        

#ws.write(0,0, 123)
#ws.write(1,1, 'iii')
#wb1.save("phase2-phase1.xls")
#wb2.save("phase3-phase2.xls")
#wb3.save("phase3-phase1.xls")

wb1.save("phase3-phase3-1.xls")
wb2.save("phase3-phase3-2.xls")
wb3.save("phase3-phase3-3.xls")
