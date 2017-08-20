import sys
import operator

infile = sys.argv[1]
outfile = sys.argv[1].split('.')[0] + '.out'
DEBUG = False

def binSearch(arry, target):
    low = 0
    high = len(arry)-1
    res = -1
    while True:
        if low >= high:
            break
        if low + 1 == high:
            break
        mid = (high + low) // 2
        if arry[mid] == target:
            res = mid
            break
        if arry[mid] < target:
            low = mid
        else:
            high = mid

    if low == 0 and arry[low] > target:
        return [-1, -1]
    if high == len(arry) - 1 and arry[high] < target:
        return [len(arry), len(arry)]
    return [low, high]        

def sumVal(arry, left, right):
    total = 0
    total += arry[0] - left
    maxval = arry[len(arry)-1]
    for i in range(0, len(arry) - 1):
        total += arry[i+1] - arry[i]
        if maxval < arry[i]:
            maxval = arry[i]
    total += right - arry[len(arry)-1]
    return [total, maxval]

def __main__():
    fin = open(infile, 'r')
    fout = open(outfile, 'w')
    tcs = int(fin.readline())
    for tc in range(0, tcs):
        line = fin.readline().split(' ')
        l = int(line[0])
        m = int(line[1])
        n = int(line[2])
        rlist = list()
        blist = list()
        purlist = list()
        sumlist = list()
        for i in range(0, l):
            rlist.append(int(fin.readline()))
            sumlist.append( [rlist[len(rlist)-1], 1] )
        for i in range(0, m):
            blist.append(int(fin.readline()))
            sumlist.append( [blist[len(blist)-1], 2] )
        for i in range(0, n):
            purlist.append(int(fin.readline()))
            sumlist.append( [purlist[len(purlist)-1], 3] )
        
        val = 0

        if l != 0:
            rlist.sort()
        if m != 0:
            blist.sort()
        if n != 0:
            purlist.sort()
        sumlist.sort(key=operator.itemgetter(0, 1))

        if n != 0:
            for i in range(0, len(purlist)-1):
                val += abs(purlist[i+1] - purlist[i])

        # first phase
        if l != 0:
            initVal = binSearch(rlist, purlist[0])
            if initVal[0] != -1:
                val += sumVal(rlist, rlist[0], initVal[0])[0]
        
        if m != 0:
            initVal = binSearch(blist, purlist[0])
            if initVal[0] != -1:
                val += sumVal(blist, blist[0], initVal[0])[0]
        
        # second phase
        for i in range(1, len(purlist)-1):
            # purlist[i], purlist[i-1] 사이에 있는 rlist를 구한다
            if l != 0:
                leftend = binSearch(rlist, purlist[i-1])[1]
                rightend = binSearch(rlist, purlist[i])[0]
                rlistsumval = sumVal(rlist, rlist[leftend], rlist[rightend])
                val += rlistsumval[0] - rlistsumval[1]
            if m != 0:
                leftend = binSearch(blist, purlist[i-1])[1]
                rightend = binSearch(blist, purlist[i])[0]
                blistsumval = sumVal(blist, blist[leftend], blist[rightend])
                val += blistsumval[0] - blistsumval[1]
            
  
        # val = 0
        # for i in range(0, l-1):
        #     val += rlist[i+1] - rlist[i]
        # for i in range(0, m-1):
        #     val += blist[i+1] - blist[i]
        # minval = 1000000000
        # rind = -1
        # bind = -1
    
        # sumlist.sort(key=operator.itemgetter(0, 1))

        # for i in range(0, len(sumlist)-1):
        #     if sumlist[i][1] != sumlist[i+1][1]:
        #         if abs(sumlist[i][0] - sumlist[i+1][0]) < minval:
        #             minval = abs(sumlist[i][0] - sumlist[i+1][0])

        # val += minval
        print(val)
        fout.write(str(val)+"\n")

    fin.close()
    fout.close()

__main__()