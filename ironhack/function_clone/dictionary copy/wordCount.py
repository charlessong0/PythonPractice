import glob
import sys

#get all the template files
dictionaryList =  glob.glob("*")
mapList = []
componentList1 = []
componentList2 = []
d3List = []

for files in dictionaryList:
    if files.startswith('d3'):
        d3List.append(files)
    elif files.startswith('dictionary'):
        mapList.append(files)
    elif files.startswith('bootstrap'):
        componentList1.append(files)
    else:
        componentList2.append(files)


#get input files from the two projects
project1 = glob.glob(argv[1] + '/*')
project2 = glob.glob(argv[2] + '/*')


#compare d3 components
d3-project1 = 0
d3-project2 = 0
for files in d3List:
    with open(files) as f:
        for line in f:
            parameter = line.split(' ')[0]
            for 
            

#compare map components


#compare html components



#data = open('test.txt').read()
#count = data.count('test')
#print count
