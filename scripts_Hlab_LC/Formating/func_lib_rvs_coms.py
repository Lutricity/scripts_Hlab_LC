import pandas as pd
import numpy as np



complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
seq = "ATGC"

master_seqs = np.array([])
def reverse_complement(seq):
    l = []
    rvs = seq[::-1]

    for i in rvs:
        l.append(complement[i])
        #print(l)
    s = ''.join(l)
    return(s)


