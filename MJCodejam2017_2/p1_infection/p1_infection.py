import sys
import math

WIDTH = math.pow(10, 9)
infile = sys.argv[1]
outfile = sys.argv[1].split('.')[0] + '.out'
DEBUG = False

class Infection(object):
    def transToHash(self, a, b):
        return a * WIDTH + b

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
            while True:
                isInfection = False
                addlist = list()
                for key in infects.keys():
                    k = infects.get(key)
                    if DEBUG:
                        print("target = ", k[0], k[1])
                    # k[0] - 1, k[1]
                    if infects.get(self.transToHash(k[0] - 1, k[1])) == None:
                        if infects.get(self.transToHash(k[0] - 1, k[1] + 1)) != None or infects.get(self.transToHash(k[0] - 2, k[1])) != None or infects.get(self.transToHash(k[0] - 1, k[1] - 1)) != None:
                            isInfection = True
                            addlist.append([k[0] - 1, k[1]])
                            if DEBUG:
                                print("up")

                    # k[0] + 1, k[1]
                    if infects.get(self.transToHash(k[0] + 1, k[1])) == None:
                        if infects.get(self.transToHash(k[0] + 1, k[1] - 1)) != None or infects.get(self.transToHash(k[0] + 2, k[1])) != None or infects.get(self.transToHash(k[0] + 1, k[1] + 1)) != None:
                            isInfection = True
                            addlist.append([k[0] + 1, k[1]])
                            if DEBUG:
                                print("down")

                    # k[0], k[1] - 1
                    if infects.get(self.transToHash(k[0], k[1] - 1)) == None:
                        if infects.get(self.transToHash(k[0] - 1, k[1] - 1)) != None or infects.get(self.transToHash(k[0], k[1] - 2)) != None or infects.get(self.transToHash(k[0] + 1, k[1] - 1)) != None:
                            isInfection = True
                            addlist.append([k[0], k[1] - 1])
                            if DEBUG:
                                print("left")

                    # k[0], k[1] + 1
                    if infects.get(self.transToHash(k[0], k[1] + 1)) == None:
                        if infects.get(self.transToHash(k[0] - 1, k[1] + 1)) != None or infects.get(self.transToHash(k[0], k[1] + 2)) != None or infects.get(self.transToHash(k[0] + 1, k[1] + 1)) != None:
                            isInfection = True
                            addlist.append([k[0], k[1] + 1])
                            if DEBUG:
                                print("right")

                if not isInfection:
                    break
                # apply changes
                for item in addlist:
                    infects[ self.transToHash(item[0], item[1]) ] = [item[0], item[1]]
                if DEBUG:
                    print(addlist)
                    t = input()

                time += 1
            fout.write(str(time)+'\n')
            print(time)
        fin.close()
        fout.close()

res = Infection()
r = res.Main()