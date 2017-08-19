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
        