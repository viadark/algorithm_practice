import sys
import math

WIDTH = math.pow(10, 9)
infile = sys.argv[1]
outfile = sys.argv[1].split('.')[0] + '.out'
DEBUG = False

class Infection(object):
    def transToHash(self, a, b):
        return str(a * WIDTH + b)

    def Main(self):
        fin = open(infile, 'r')
        fout = open(outfile, 'w')

        tcs = int(fin.readline())
        for tc in range(0, tcs):
            numInfect = int(fin.readline())
            infects = dict()
            for i in range(0, numInfect):
                line = fin.readline().split(' ')
                infects[ self.transToHash(int(line[0]), int(line[1])) ] = [ int(line[0]), int(line[1]) ]
            if DEBUG:
                print(infects)
            time = 0
            isFirst = True
            addlist = dict()
            while True:
                isInfection = False
                if isFirst:
                    for key in infects.keys():
                        k = infects.get(key)
                        if DEBUG:
                            print("target = ", k[0], k[1])
                        # k[0] - 1, k[1]
                        if infects.get(self.transToHash(k[0] - 1, k[1])) == None:
                            if infects.get(self.transToHash(k[0] - 1, k[1] + 1)) != None or infects.get(self.transToHash(k[0] - 2, k[1])) != None or infects.get(self.transToHash(k[0] - 1, k[1] - 1)) != None:
                                isInfection = True
                                addlist[ (k[0] - 1, k[1]) ] = [k[0] - 1, k[1]]
                                if DEBUG:
                                    print("up")

                        # k[0] + 1, k[1]
                        if infects.get(self.transToHash(k[0] + 1, k[1])) == None:
                            if infects.get(self.transToHash(k[0] + 1, k[1] - 1)) != None or infects.get(self.transToHash(k[0] + 2, k[1])) != None or infects.get(self.transToHash(k[0] + 1, k[1] + 1)) != None:
                                isInfection = True
                                addlist[ (k[0] + 1, k[1]) ] = [k[0] + 1, k[1]]
                                if DEBUG:
                                    print("down")

                        # k[0], k[1] - 1
                        if infects.get(self.transToHash(k[0], k[1] - 1)) == None:
                            if infects.get(self.transToHash(k[0] - 1, k[1] - 1)) != None or infects.get(self.transToHash(k[0], k[1] - 2)) != None or infects.get(self.transToHash(k[0] + 1, k[1] - 1)) != None:
                                isInfection = True
                                addlist[ (k[0], k[1] - 1) ] = [k[0], k[1] - 1]
                                if DEBUG:
                                    print("left")

                        # k[0], k[1] + 1
                        if infects.get(self.transToHash(k[0], k[1] + 1)) == None:
                            if infects.get(self.transToHash(k[0] - 1, k[1] + 1)) != None or infects.get(self.transToHash(k[0], k[1] + 2)) != None or infects.get(self.transToHash(k[0] + 1, k[1] + 1)) != None:
                                isInfection = True
                                addlist[ (k[0], k[1] + 1) ] = [k[0], k[1] + 1]
                                if DEBUG:
                                    print("right")
                    isFirst = False
                    if not isInfection:
                        break
                    time += 1
                    for item in addlist.keys():
                        infects[ self.transToHash(item[0], item[1]) ] = [item[0], item[1]]
                    continue
                else:
                    if DEBUG:
                        print(addlist)
                    changelist = dict()
                    for k in addlist.keys():
                        if DEBUG:
                            print("k = ", k)
                            print("target = ", k[0], k[1])
                        # k[0] - 1, k[1]
                        if infects.get(self.transToHash(k[0] - 1, k[1])) == None:
                            if k[0]-2 >= 0 and k[1] -2 >= 0 and k[0]+2 <= WIDTH and k[1]+2 <= WIDTH and (infects.get(self.transToHash(k[0] - 1, k[1] + 1)) != None or infects.get(self.transToHash(k[0] - 2, k[1])) != None or infects.get(self.transToHash(k[0] - 1, k[1] - 1)) != None):
                                isInfection = True
                                changelist[ (k[0] - 1, k[1]) ] = [k[0] - 1, k[1]]
                                if DEBUG:
                                    print("up")

                        # k[0] + 1, k[1]
                        if infects.get(self.transToHash(k[0] + 1, k[1])) == None:
                            if k[0]-2 >= 0 and k[1] -2 >= 0 and k[0]+2 <= WIDTH and k[1]+2 <= WIDTH and (infects.get(self.transToHash(k[0] + 1, k[1] - 1)) != None or infects.get(self.transToHash(k[0] + 2, k[1])) != None or infects.get(self.transToHash(k[0] + 1, k[1] + 1)) != None):
                                isInfection = True
                                changelist[ (k[0] + 1, k[1]) ] = [k[0] + 1, k[1]]
                                if DEBUG:
                                    print("down")

                        # k[0], k[1] - 1
                        if infects.get(self.transToHash(k[0], k[1] - 1)) == None:
                            if k[0]-2 >= 0 and k[1] -2 >= 0 and k[0]+2 <= WIDTH and k[1]+2 <= WIDTH and (infects.get(self.transToHash(k[0] - 1, k[1] - 1)) != None or infects.get(self.transToHash(k[0], k[1] - 2)) != None or infects.get(self.transToHash(k[0] + 1, k[1] - 1)) != None):
                                isInfection = True
                                changelist[ (k[0], k[1] - 1) ] = [k[0], k[1] - 1]
                                if DEBUG:
                                    print("left")

                        # k[0], k[1] + 1
                        if infects.get(self.transToHash(k[0], k[1] + 1)) == None:
                            if k[0]-2 >= 0 and k[1] -2 >= 0 and k[0]+2 <= WIDTH and k[1]+2 <= WIDTH and (infects.get(self.transToHash(k[0] - 1, k[1] + 1)) != None or infects.get(self.transToHash(k[0], k[1] + 2)) != None or infects.get(self.transToHash(k[0] + 1, k[1] + 1)) != None):
                                isInfection = True
                                changelist[ (k[0], k[1] + 1) ] = [k[0], k[1] + 1]
                                if DEBUG:
                                    print("right")
                    if not isInfection:
                        break
                    # apply changes
                    for item in changelist.keys():
                        infects[ self.transToHash(item[0], item[1]) ] = [item[0], item[1]]
                    if DEBUG:
                        print(addlist)
                        print(changelist)
                    addlist = changelist
                    time += 1
                
            fout.write(str(time)+'\n')
            print(time)
            #temp = input()
        fin.close()
        fout.close()

res = Infection()
r = res.Main()

# comments
# 추가된 infect에 대해서만 검사를 하면 되는가?