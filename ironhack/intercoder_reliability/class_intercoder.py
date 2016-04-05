from __future__ import division
import xlrd
import xlwt
import glob
import os

file_list = glob.glob("data_test/*.xls")
wb = xlwt.Workbook()
ws = wb.add_sheet("intercoder_matrix", cell_overwrite_ok=True)

index_x = 1
index_y = 1
num_matching = 0
num_total = 0

#temp_path = ""
for path1 in file_list:
    book1 = xlrd.open_workbook(path1)
    sh1 = book1.sheet_by_index(0)
    index_x = 1
    for path2 in file_list:
        '''
        print path1
        print "==="
        print path2
        print "============="
        '''
        book2 = xlrd.open_workbook(path2)
        sh2 = book2.sheet_by_index(0)
        #x range: 2-4; y range: 50-54, 58-59, 63-68
        for i in range(2, 5):
            for j in range(50, 55):
                if (sh1.cell_value(rowx=j, colx=i) == sh2.cell_value(rowx=j, colx=i)):
                   num_matching = num_matching + 1 
                num_total = num_total + 1
            for j in range(58, 60):
                if (sh1.cell_value(rowx=j, colx=i) == sh2.cell_value(rowx=j, colx=i)):
                   num_matching = num_matching + 1 
                num_total = num_total + 1
            for j in range(63, 69):
                if (sh1.cell_value(rowx=j, colx=i) == sh2.cell_value(rowx=j, colx=i)):
                   num_matching = num_matching + 1 
                num_total = num_total + 1
        #write into output
        print index_x, index_y
        ws.write(index_y, index_x, num_matching/num_total)
        #swich to next y and reset the numbers
        num_matching = 0
        num_total = 0
        index_x = index_x+1
    index_y = index_y+1

wb.save("output.xls")
