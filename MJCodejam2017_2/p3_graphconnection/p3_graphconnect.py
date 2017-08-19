import sys
import operator

infile = sys.argv[1]
outfile = sys.argv[1].split('.')[0] + '.out'
DEBUG = False

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
        
        rlist.sort()
        blist.sort()
        purlist.sort()

        val = 0
        for i in range(0, l-1):
            val += rlist[i+1] - rlist[i]
        for i in range(0, m-1):
            val += blist[i+1] - blist[i]
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