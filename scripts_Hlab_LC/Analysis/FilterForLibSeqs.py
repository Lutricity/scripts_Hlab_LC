# take a CPseq file
# make two lists with R1 as and the rvs comp R2 from each CPseq file
# Library 4 - expect less than ten, if any, overlapping bases between reads, but Read 1 should cover all of the variable region
# Read 2 is the reverse complement of the ordered library so make the reverse complement of every input librarys sequence (eassier computationally than sequencing read)
#
#run in python3

import pandas as pd
import numpy as np
import sys, getopt

#tool to troubleshoot if needed:
import time


# Note from Hannah Wayment-Steele
#  download package pandarallel
#  usage: beginning of script, call
#  from pandarallel import pandarallel
#  pandarallel.initialize()


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


def find_ref_seq(row, ref_seqs):
    # print("This is row R2D2", row['R2'])
    for j in ref_seqs:
        if j in row['R2']:
            return True
    return False

#------------------------------------------------

def main(argv):
    start_time = time.time()

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


# Assign command lne args
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('trueSeqReads.py -i <inputfile>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print('trueSeqReads.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    print('Input file is "', inputfile)



# read in CPseq

    #setting input/output file names
    in_foo = str(inputfile)


    #read in the active columns of the CPSeq to be edited
    CPseq = pd.read_csv(in_foo, delimiter="\t", index_col = False, names = ["location", "exp", "R1", "QR1", "R2", "QR2", "BC", "QBC", "BS1"])


    #make a list of the rvs complement of each of read 2 sequences
    refseq_rc = []
    for i in ref_seqs:
        o = reverse_complement(i, complement)
        refseq_rc.append(o)


    #rvs_refseq = pd.DataFrame(refseq_rc)

#save rvsComp list of ref seqs to a csv
    #rvs_refseq.to_csv("rvsd_Lib4_refs_30E3.csv", index=False)

#turn the read 2 into a list
    r2 = list(CPseq["R2"])


# append an empty column to flag if a row contains a lib4 sequence
    CPseq["Lib_flag"] = np.nan



#use the function find_ref_seqs to seqrch if a row value in column "R2" contains a substring equal to a string in refseq_rc
#populates the "Lib_flag" column with a boolean if a refseq_rc is present
    CPseq['Lib_flag'] = CPseq.apply(lambda row: find_ref_seq(row, refseq_rc), axis=1)

#drop any row that does not contain a ref seq (Lib_flag == False)
    CPseq.drop(CPseq[CPseq['Lib_flag'] == False].index, inplace=True)



# save to a csv
    end_name =   in_foo.replace(".sort.CPseq", "filtered.sort.CPseq")
    CPseq.to_csv(end_name, sep = "\t", index = False)


    print("--- %s seconds ---" % (time.time() - start_time))
    print(in_foo, "was filtered!")



if __name__ == "__main__":
    main(sys.argv[1:])
