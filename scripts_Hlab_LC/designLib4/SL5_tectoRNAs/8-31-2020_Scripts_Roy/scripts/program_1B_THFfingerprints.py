#!/bin/bash

import sys
from library import *

# define csv files to read / write:
# NOTE: To run script change file paths / names here!
helixcsv = "150_chip_helices.csv"
eachloopcsv = "980.9_loop.csv"
eachreceptorcsv = "4LVV.4_receptor.csv"
coreloopcsv = "4LVV_loop.csv"
corereceptorcsv = "980_receptor.csv"
output1csv = "../outputs/fngrprt_150_4LVV.csv"
output2csv = "../outputs/fngrprt_150_980.csv"


# Read in data
hname, hseq, hss = parse_helix_csv(helixcsv)
elseq, elname = parse_tecto_csv(eachloopcsv)
erseq, ername = parse_tecto_csv(eachreceptorcsv)
clseq, clname = parse_tecto_csv(coreloopcsv)
crseq, crname = parse_tecto_csv(corereceptorcsv)


###generates a blank dataframe
#clseq = clseq[:-1]
#clname = clname[:-1]
#crseq = crseq[:-1]
#crname = crname[:-1]


# Generate core loops vs all receptor seqs:
counter = 0
outname = []
outseq = []
outss = []
for hnameit, hseqit, hssit in zip(hname, hseq, hss):
    for lseqit, lnameit in zip(clseq, clname):
        for rseqit, rnameit in zip(erseq, ername):
            newseqt, newsst = attach_receptor(rseqit, hseqit, hssit, -1)
            newseqt, newsst = attach_loop(lseqit, newseqt, newsst, newseqt.find('+'))
            newnamet = hnameit + ":" + lnameit + ":" + rnameit 
            outname.append(newnamet)
            outseq.append(newseqt)
            outss.append(newsst)
            #print("This is seqs:", counter)
            #print(newseqt)
            counter += 1
#print("This is outname",outname)

data = {'name': outname, 'sequence': outseq, 'ss': outss}
df = pd.DataFrame(data, columns = ['name', 'sequence', 'ss'])
print(df.head())
print(df.shape)
df.to_csv(output1csv, sep=",", index=False)


# Generate all loops vs core receptor seqs:
counter = 0
outname = []
outseq = []
outss = []
for hnameit, hseqit, hssit in zip(hname, hseq, hss):
    for lseqit, lnameit in zip(elseq, elname):
        for rseqit, rnameit in zip(crseq, crname):
            newseqt, newsst = attach_receptor(rseqit, hseqit, hssit, -1)
            newseqt, newsst = attach_loop(lseqit, newseqt, newsst, newseqt.find('+'))
            newnamet = hnameit + ":" + lnameit + ":" + rnameit 
            outname.append(newnamet)
            outseq.append(newseqt)
            outss.append(newsst)
            counter += 1


data = {'name': outname, 'sequence': outseq, 'ss': outss}
df = pd.DataFrame(data, columns = ['name', 'sequence', 'ss'])
print(df.head())
print(df.shape)
df.to_csv(output2csv, sep=",", index=False)












