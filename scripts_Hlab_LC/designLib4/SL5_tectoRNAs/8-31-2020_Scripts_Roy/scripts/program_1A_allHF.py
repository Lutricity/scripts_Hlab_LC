#!/bin/bash

import sys
from library import *

# define csv files to read / write:
# NOTE: To run script change file paths / names here!
helixcsv = "3_chip_helices.csv"
loopcsv = "980.9_base_Loop.csv"
receptorcsv = "980R_singleMuts.csv"
outputcsv = "THF_Muts/output_980R_singleMuts.csv"

# Read in data
hname, hseq, hss = parse_helix_csv(helixcsv)
lseq, lname = parse_tecto_csv(loopcsv)
rseq, rname = parse_tecto_csv(receptorcsv)

# Generate all seqs:
counter = 0
outname = []
outseq = []
outss = []
for hnameit, hseqit, hssit in zip(hname, hseq, hss):
    for lseqit, lnameit in zip(lseq, lname):
        for rseqit, rnameit in zip(rseq, rname):
            newseqt, newsst = attach_receptor(rseqit, hseqit, hssit, -1)
            newseqt, newsst = attach_loop(lseqit, newseqt, newsst, newseqt.find('+'))
            newnamet = hnameit + ":" + lnameit + ":" + rnameit 
            outname.append(newnamet)
            outseq.append(newseqt)
            outss.append(newsst)
            counter += 1

data = {'name': outname, 'sequence': outseq, 'ss': outss}
df = pd.DataFrame(data, columns = ['name', 'sequence', 'ss'])
df.to_csv(outputcsv, sep=",", index=False)
