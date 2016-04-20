# histon_modifica_-analyse\
#count peaks from chip-seq hiscone 

file_all = open('all.gff3')
file_peaks = open('peaks.xls')
file_out = open('peaks.txt', 'w')
index2 = 0
dict_all = dict()
dict_peaks = dict()
gene_count=0
while 1:
    line = file_all.readline()
    if not line:
        break

    tmp = line.split('\t')

    if len(tmp)==9:
        key = tmp[0]
        if not dict_all.has_key(key):
           dict_all[key]=[]
        #if tmp[2]=='gene':
        dict_all[key].append((int(tmp[3]),int(tmp[4]),tmp[8],tmp[2]))
        #print tmp[2]
        gene_count+=1
        #print tmp[2],tmp[3],tmp[4]
print gene_count

while 1:
    line = file_peaks.readline()
    if not line:
        break
    if line.startswith('Chr'):
        tmp=line.split('\t')
        key=tmp[0]
        if not dict_peaks.has_key(key):
            dict_peaks[key]=[]
        dict_peaks[key].append((int(tmp[1]),int(tmp[2])))

keys = dict_peaks.keys()

count=0
count_map=dict()

for key in keys:
    data1 = dict_all[key]
    data2 = dict_peaks[key]
    p1=0
    p2=0
    while p1<len(data1) and p2<len(data2):
        row1 = data1[p1]
        row2 = data2[p2]

        start = row1[0]
        end = row1[1]
        message = row1[2]
        start2=row2[0]
        end2=row2[1]
        if end2<start:
            p2+=1
            #print '1st',start,end,'-',start2,end2
            continue
        if start2>end:
            p1+=1
            #print '2st',start,end,'-',start2,end2
            continue

        #print >> file_out,count,key,data[0],data[1],data[2]
        ratio = abs((start+start2)-(end+end2))/(end2-start2)
        if ratio>0.5:
            count+=1
            #print count,key,row1[0],row1[1],str(row1[2]).rstrip(),ratio
            #print start,end,start2,end2

            file_out.write(str(count)+" "+key+" "+str(row1[0])+" "+str(row1[1])+" "+row1[2]+' '+str(ratio))
            if count_map.has_key(row1[3]):
                count_map[row1[3]]+=1
            else:
                count_map[row1[3]]=0

        if end2>=start and end2<=end:
            p2+=1
        else:
            p1+=1



print('count',count)
print count_map
file_out.close()
