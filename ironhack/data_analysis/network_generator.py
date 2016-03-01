import networkx as nx
import numpy as np
import string
import xlrd

'''
book = xlrd.open_workbook("test.xlsx")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(2)
sh0 = book.sheet_by_index(0)
sh3 = book.sheet_by_index(3)
print sh.name, sh.nrows, sh.ncols
print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
'''

dt = [('len', float)]

A = np.array([(0.3, 0, 0.3, 0.4, 0.7),
               (0.3, 0.6,  0, 0.9, 0.2),
               (0.4, 0.9, 0.4, 0, 0.1),
               (0.7, 0.2, 0.1, 0.1, 0),
               (0.3, 0.9, 0.9, 0.5, 0.1)		
               ])*10
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

G = nx.drawing.nx_agraph.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="blue", width="2.0")

G.draw('out.png', format='png', prog='neato')


