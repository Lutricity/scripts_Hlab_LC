#!/bin/bash

import sys
from library import *

# define csv files to read / write:
# NOTE: To run script change file paths / names here!
thfcsv = "../core_kts_3.csv"
outputcsv = "core_kts_single_muts.csv"

# Read in data
seq, name = parse_tecto_csv(thfcsv)

# Generate core loops vs all receptor seqs:
counter = 0
outname = []
outseq = []
for nameit, seqit in zip(name, seq):
    indicestomutate = list(range(len(seqit)))
    if '+' in seqit:
        indicestomutate.remove(seqit.find('+'))
    mtseq, mtname = get_point_mutants(seqit, indicestomutate, nameit)
    outname.extend(mtname)
    outseq.extend(mtseq)


data = {'name': outname, 'sequence': outseq}
df = pd.DataFrame(data, columns = ['name', 'sequence'])
df.to_csv(outputcsv, sep=",", index=False)

