import sys
import operator

infile = sys.argv[1]
outfile = sys.argv[1].split('.')[0] + '.out'
DEBUG = False

def calcNalssin(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    if a > b:
        return b / a
    else:
        return a / b
def calcRound(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    return 2 * (a + b)

def __main__():
    fin = open(infile, 'r')
    fout = open(outfile, 'w')
    tcs = int(fin.readline())
    for tc in range(0, tcs):
        np = int(fin.readline())
        plist = list()
        for i in range(0, np):
            line = fin.readline().split(' ')
            plist.append([int(line[0]), int(line[1])])

        plist.sort(key=operator.itemgetter(0, 1))
        minval = 99
        resval = list()
        resval.append( [-1, -1] )
        resval.append( [-1, -1] )
        for i in range(0, np-1):
            val = calcNalssin(plist[i], plist[i+1])
            if val < minval:
                minval = val
                resval[0] = plist[i]
                resval[1] = plist[i+1]

        plist.sort(key=operator.itemgetter(1, 0))
        for i in range(0, np-1):
            val = calcNalssin(plist[i], plist[i+1])
            if val < minval:
                minval = val
                resval[0] = plist[i]
                resval[1] = plist[i+1]
        res = calcRound(resval[0], resval[1])
        print(res)
        fout.write(str(res) + '\n')

    fin.close()
    fout.close()

__main__()