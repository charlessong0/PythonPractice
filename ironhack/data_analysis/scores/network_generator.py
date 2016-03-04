import networkx as nx
import numpy as np
import string
import xlrd


book = xlrd.open_workbook("phase3-phase1.xls")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(1)
#sh0 = book.sheet_by_index(0)
#sh3 = book.sheet_by_index(3)
print sh.name, sh.nrows, sh.ncols
print "Cell D30 is", sh.cell_value(rowx=3, colx=3)

names = [0 for x in range(sh.nrows-1)]
array = [[0 for x in range(sh.nrows-1)] for x in range(sh.ncols-1)]

for i in range(1, sh.nrows):
	names[i-1] = sh.cell_value(0, i)
	for j in range(1, sh.ncols):
		array[i-1][j-1] = sh.cell_value(rowx=i, colx=j)
print array

dt = [('len', float)]

A = np.array(array)/5
#A = np.array([(0.3, 0, 0.3, 0.4, 0.7),
#               (0.3, 0.6,  0, 0.9, 0.2),
#               (0.4, 0.9, 0.4, 0, 0.1),
#               (0.7, 0.2, 0.1, 0.1, 0),
#               (0.3, 0.9, 0.9, 0.5, 0.1)		
#               ])*10
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    
#G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),names)))

G = nx.drawing.nx_agraph.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="blue", width="2.0")

G.draw('output3-1total.png', format='png', prog='neato')
