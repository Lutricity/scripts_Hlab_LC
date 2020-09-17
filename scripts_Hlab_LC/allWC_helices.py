#Goal: Write a program that makes every possible WC helix at the 8-12 bp length
#w/ G bulge for 4LVV THF tectoRNA
#w/0 G bulge

import pandas as pd
import csv

nts_RNA = "A", "C", "G", "U"
base = "GGGGGGGGGGGG"
# first make a 5' side and sequentially populate every possible sequence
#make for 12 bp, and then trim ends
#def all_nts_at_pos_X(start_base, end_seq)
lst = []

for i in nts_RNA:
    seq0 = i + base[1:]
    lst.append(seq0)

lst2 = []
for j in lst:
    for m in nts_RNA:
        seq1 = j[0] + m + j[2:]
        lst2.append(seq1)
        #print(seq1)

        
#print(lst)
print(lst2)


#then make a 3' side that matches each 5' side

#then make a function that checks for duplicate sequences and removes them