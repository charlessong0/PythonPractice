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
d3-common = 0
for files in d3List:
    with open(files) as f:
        for line in f:
            parameter = line.split(' ')[0]
            temp1 = 0
            temp2 = 0
            for file1 in project1:
                data = open(file1).read()
                temp1 += data.count(parameter)
            for file2 in project2:
                data = open(file2).read()
                temp2 += data.count(parameter)
            d3-project1 += temp1
            d3-common += getSmall(temp2, temp1)
            d3-project2 += temp2

#compare map components
map-project1 = 0
map-project2 = 0
map-common = 0
for files in mapList:
    with open(files) as f:
        for line in f:
            parameter = line.split(',')[0]
            temp1 = 0
            temp2 = 0
            for file1 in project1:
                data = open(file1).read()
                temp1 += data.count(parameter)
            for file2 in project2:
                data = open(file2).read()
                temp2 += data.count(parameter)
            map-project1 += temp1
            map-common += getSmall(temp2, temp1)
            map-project2 += temp2

#compare html components
com-project1 = 0
com-project2 = 0
com-common = 0
for files in componentList2:
    with open(files) as f:
        for line in f:
            parameter = line.split(' ')[0]
            temp1 = 0
            temp2 = 0
            for file1 in project1:
                data = open(file1).read()
                temp1 += data.count(parameter)
            for file2 in project2:
                data = open(file2).read()
                temp2 += data.count(parameter)
            com-project1 += temp1
            com-common += getSmall(temp2, temp1)
            com-project2 += temp2

for files in componentList1:
    with open(files) as f:
        for line in f:
            parameter = line
            temp1 = 0
            temp2 = 0
            for file1 in project1:
                data = open(file1).read()
                temp1 += data.count(parameter)
            for file2 in project2:
                data = open(file2).read()
                temp2 += data.count(parameter)
            com-project1 += temp1
            com-common += getSmall(temp2, temp1)
            com-project2 += temp2

print "map pro1: " + map-project1
print "map pro2: " + map-project2
print "map common" + map-common

print "d3 pro1: " + d3-project1
print "d3 pro2: " + d3-project2
print "d3 common: " + d3-common

print "components pro1: " + com-project1
print "components pro2: " + com-project2
print "components common: " + com-common

def getSmall(m, n):
    if m < n:
        return m
    else:
        return n
