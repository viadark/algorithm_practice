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
            redinput = int(fin.readline())
            rlist.append(redinput)
            sumlist.append( [rlist[len(rlist)-1], 1] )
        for i in range(0, m):
            blueinput = int(fin.readline())
            blist.append(blueinput)
            # try:
            #     res = rlist.index(blueinput)
            #     if res != -1:
            #         print("duplicate value :", blueinput, res)
            # except:
            #     pass
            sumlist.append( [blist[len(blist)-1], 2] )
        for i in range(0, n):
            purlist.append(int(fin.readline()))
            sumlist.append( [purlist[len(purlist)-1], 3] )
        
        val = 0

        sumlist.sort(key=operator.itemgetter(0))
        purlist.sort()

        if n != 0:
            for i in range(0, len(purlist)-1):
                val += abs(purlist[i+1] - purlist[i])
        
        isFirstPurple = True
        redStack = list()
        blueStack = list()
        prePurple = -1
        for i in range(0, len(sumlist)):
            if sumlist[i][1] == 3:
                # flush
                if isFirstPurple:
                    # max value not delete
                    sumval = 0
                    if len(redStack) != 0:
                        if len(redStack) >= 2:
                            for j in range(0, len(redStack)-1):
                                sumval += redStack[j+1] - redStack[j]
                        sumval += sumlist[i][0] - redStack[len(redStack)-1]
                        redStack.clear()

                    if len(blueStack) != 0:
                        if len(blueStack) >= 2:
                            for j in range(0, len(blueStack)-1):
                                sumval += blueStack[j+1] - blueStack[j]
                        sumval += sumlist[i][0] - blueStack[len(blueStack)-1]
                        blueStack.clear()
                    val += sumval
                    isFirstPurple = False
                    prePurple = sumlist[i][0]

                else:
                    # delete max value
                    sumval = 0
                    maxval = 0
                    if len(redStack) != 0:
                        if len(redStack) >= 2:
                            for j in range(0, len(redStack)-1):
                                if maxval < redStack[j+1] - redStack[j]:
                                    maxval = redStack[j+1] - redStack[j]
                                sumval += redStack[j+1] - redStack[j]
                        sumval += sumlist[i][0] - redStack[len(redStack)-1]
                        sumval += redStack[0] - prePurple
                        if maxval < sumlist[i][0] - redStack[len(redStack)-1]:
                            maxval = sumlist[i][0] - redStack[len(redStack)-1]
                        if maxval < redStack[0] - prePurple:
                            maxval = redStack[0] - prePurple
                        sumval -= maxval
                        redStack.clear()

                    maxval = 0
                    if len(blueStack) != 0:
                        if len(blueStack) >= 2:
                            for j in range(0, len(blueStack)-1):
                                if maxval < blueStack[j+1] - blueStack[j]:
                                    maxval = blueStack[j+1] - blueStack[j]
                                sumval += blueStack[j+1] - blueStack[j]
                        sumval += sumlist[i][0] - blueStack[len(blueStack)-1]
                        sumval += blueStack[0] - prePurple
                        if maxval < sumlist[i][0] - blueStack[len(blueStack)-1]:
                            maxval = sumlist[i][0] - blueStack[len(blueStack)-1]
                        if maxval < blueStack[0] - prePurple:
                            maxval = blueStack[0] - prePurple
                        sumval -= maxval
                        blueStack.clear()
                    val += sumval
                    prePurple = sumlist[i][0]

            elif sumlist[i][1] == 1 :
                redStack.append(sumlist[i][0])
            else:
                blueStack.append(sumlist[i][0])
                

        # flush, not delete max value
        if len(redStack) != 0:
            # flush redStack
            sumval = 0
            if len(purlist) != 0:
                sumval += redStack[0] - purlist[len(purlist)-1]
            if len(redStack) >= 2:
                for i in range(0, len(redStack)-1):
                    sumval += redStack[i+1] - redStack[i]
            val += sumval
        if len(blueStack) != 0:
            # flush blueStack
            sumval = 0
            if len(purlist) != 0:
                sumval += blueStack[0] - purlist[len(purlist)-1]
            if len(blueStack) >= 2:
                for i in range(0, len(blueStack)-1):
                    sumval += blueStack[i+1] - blueStack[i]
            val += sumval

        print(val)
        fout.write(str(val)+"\n")
        #temp = input()

    fin.close()
    fout.close()

__main__()