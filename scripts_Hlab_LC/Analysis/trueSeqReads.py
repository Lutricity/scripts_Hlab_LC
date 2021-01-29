# take a CPseq file
# make two lists with R1 as and the rvs comp R2 from each CPseq file
# Library 4 - expect less than ten, if any, overlapping bases between reads, but Read 1 should cover all of the variable region
# Read 2 is the reverse complement of the ordered library so make the reverse complement of every input librarys sequence (eassier computationally than sequencing read)
#
#

import pandas as pd
import numpy as np
from multiprocessing import pool

#tool to troubleshoot if needed:
#import time
#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))


# rvs_comp function takes a list of sequences and outputs an equal length list of the rvs_complements of the sequences it read
def reverse_complement(seq,comp):
    l = []
    rvs = seq[::-1]

    for i in rvs:
        l.append(comp[i])
        #print(l)
    s = ''.join(l)
    return(s)

# finder function
def finder(ref_lst, vari_lst):
    pos = 0
    seq_dict = {}

    for i in ref_lst:
        count = 0
        for j in vari_lst:
            if i in j:
                count += 1
            else:
                pass
        # change pos to i on line below if want to assign counts to refernece sequences
        seq_dict[pos] = count
        pos += 1


    return(seq_dict)


#------------------------------------------------

def main():

#define complmenting nts for rvs_cmp function
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

#Read in the reference library sequecnes
    ref_seqs = []

    f = open("one_repeat_ref_Lib4.csv", 'r')
    for l in f:
        # if l[-2:] == "\r\n"
        l = l[:-2]
        ref_seqs.append(l)

    ref_seqs.pop(0)
    f.close()


# read in CPseq

    #setting input/output file names
    in_foo = "bite_lib4.sort.CPseq"
    #out_foo = "corrected_bite_AEL52.CPseq"

    #read in the active columns of the CPSeq to be edited
    CPseq = pd.read_csv(in_foo, delimiter="\t", index_col = False, usecols = [4], names = ["R2"])

    print("read_in_seq_file")

    #make a list of the rvs complement of each of read 2 sequences
    refseq_rc = []
    for i in ref_seqs:
        o = reverse_complement(i, complement)
        refseq_rc.append(o)

    print("rvsed_comp")

    #turn the read 2 into a list
    r2 = list(CPseq["R2"])

   # for each rvs ref seq check # of exact matches in R2 list
   # then add number of hits to the count of that ref seq in a dictionary (seq_hits)

    seq_hits = finder(refseq_rc, r2)

    print("found seqs")
    # check how many ref seqs have any hits in the ref seq
    numb = 0
    for key in seq_hits:
        if seq_hits[key] > 0:
            numb += 1

    numb_5 = 0
    for key in seq_hits:
        if seq_hits[key] > 4:
            numb_5 += 1




    prcnt_seq = float((numb / len(seq_hits)))
    prcnt_RNAP = float((numb / len(r2)))
    prcnt_5ormore = float((numb_5 / len(seq_hits)))
    prcnt_5ormore_RNAP = float((numb_5 / len(r2)))

    print("Number of ref seqs represented in sequencing file:", numb)
    print("Percentage of ref_seqs represented in sequencing file:", prcnt_seq)
    print("Percentage of RNAP Read2s that are in library 4:", prcnt_RNAP)
    print("Percentage of ref_seqs represented in sequencing file at n >= 5:", prcnt_5ormore)
    print("Percentage of RNAP Read2s n >= 5 that are in library 4:", prcnt_5ormore_RNAP)

    #statistics
    # % of ref seqs that appear
    # % of ref seqs that appear > 5 x on this chip
    # for i in dict



    counts = pd.DataFrame.from_dict(seq_hits, orient='index')
    csv_name = "dictSoln"+ in_foo
    counts.to_csv(csv_name, sep = "\t", index = False)

    print(counts.head)


if __name__ == "__main__":
    main()