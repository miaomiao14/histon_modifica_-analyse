__author__ = 'Miaomiao'

diff = 100
ratio = 0.001

file1 = open('3.csv', 'r')
line = file1.readline()
list1 = []
while line:
    line = line.rstrip()
    item = line.split(',')
    start = int(item[1])
    end = int(item[2])

    list1.append((int(item[0].rstrip()), start,end))
    line = file1.readline()
print('========================')
file2 = open('4.csv', 'r')
line = file2.readline()
list2 = []
while line:
    line = line.rstrip()
    item = line.split(',')
    start = int(item[1])
    end = int(item[2])

    list2.append((int(item[0].rstrip()), start,end))
    line = file2.readline()

if len(list1) <= len(list2):
    length = len(list1)
    list_short = list1
    list_long = list2
else:
    length = len(list2)
    list_short = list2
    list_long = list1

index1 = 0
index2 = 0
count = 0


def get_num(schr):
    num = schr[3:]
    return int(n)


while index1 < len(list1) and index2 < len(list2):
    item1 = list1[index1]
    item2 = list2[index2]
    chr1 = item1[0]
    start1 = item1[1]
    end1 = item1[2]
    chr2 = item2[0]
    start2 = item2[1]
    end2 = item2[2]
    print(index1,index2,item1,item2)
    if chr1 == chr2:
        r1 = (start1 - start2)/start1
        r2 = (end1 - end2)/end1
        if r1<-ratio:
            index1 += 1
        elif r1>ratio:
            index2 += 1
        elif abs(r2)<ratio:
            print(count, 'match:', (start1, end1))
            count += 1
            index1 += 1
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    else:
        if int(chr1) > int(chr2):
            index2 += 1
        else:
            index1 += 1

print('count', count)
print(len(list1), len(list2))
