import os 
from pathlib import Path

def writefile(indicator):
    srcpath = '/home/dataset/'+indicator
    w = open('/home/dataset/'+indicator+'.txt','w')

    subpath_0 = srcpath + '/fake'
    subpath_1 = srcpath + '/real'

# -----------------------Deepfakes (0)----------------------- #
    a_0_1 = []     # a_type_stream
    for a1 in Path(subpath_0).rglob("*.*"):
        a_0_1.append(str(a1))
    a_0_1.sort()

    for i in range(len(a_0_1)):
        w.write(a_0_1[i] + ' ' + '0' + '\n')

    
# -------------------------real (1)-------------------------- #
    b_1_1 = []     # b_type_stream
    for b1 in Path(subpath_1).rglob("*.*"):
        b_1_1.append(str(b1))
    b_1_1.sort()

    for i in range(len(b_1_1)):
        w.write(b_1_1[i] + ' ' + '1' + '\n')

    w.close() 

writefile('train')


