# This is a set of random classes / functions that we might be able to reuse for different
# scripts as and when we write them (Reuse them as much as possible!)
#must first attach a loop, then attach a receptor
import pandas as pd

loopsschar = 'x' # use this character to represent ss of tecto RNA loop / receptor for now

# Read the csv file for a helix and return the cols as python lists:
def parse_helix_csv(csvfile):
    df = pd.read_csv(csvfile)
    names = df['name'].tolist()
    seqs = df['sequence'].tolist()
    ss = df['ss'].tolist()
    return (names, seqs, ss)

# Read the csv file for a loop/receptor and return the cols as python lists:
def parse_tecto_csv(csvfile):
    df = pd.read_csv(csvfile)
    seqs = df['sequence'].tolist()
    # give a name to each seq:
    if 'name' in df.columns:
        name = df['name'].tolist()
        return (seqs, name)
    name = ['type'+str(i+1) for i in range(len(seqs))]
    return (seqs, name)

# Function to attach  a THF loop sequence at a particular index in a parent sequence:
def attach_loop(loopseq, seq, ss, index):
    # if there is only one strand in parent seq: (straight forward)
    if '+' not in seq:
        newseq = seq[:index] + loopseq + seq[index:] #  create new seq
        newss = ss[:index] + loopsschar*len(loopseq) + ss[index:]
        return (newseq, newss)
    
    # Else split into cases based on where the loop will be inserted:
    splitidx = seq.find('+')

    # Case 1a and b: Inserting loop within one of the helices:
    if index < splitidx or index > splitidx+1:
        newseq = seq[:index] + loopseq + seq[index:]
        newss = ss[:index] + loopsschar*len(loopseq) + ss[index:]
        return (newseq, newss)


    # Case 3: Inserting loop to join the two helices:
    else:
        seqspl = seq.split('+')
        ssspl = ss.split('+')
        newseq = seqspl[0] + loopseq + seqspl[1]
        newss = ssspl[0] + loopsschar*len(loopseq) + ssspl[1]
        return (newseq, newss)

# Function to attach a receptor to a sequence with predefined ss:
def attach_receptor(rseq, seq, ss, index):
    rseqh1 = rseq.split('+')[0]
    rseqh2 = rseq.split('+')[1]
    # Split it up into two cases:
    if '+' not in seq:  # adding the receptor to a single strand seq
        newseq = seq[:index] + rseqh1 + '+' + rseqh2 + seq[index:]
        newss = ss[:index] + loopsschar*len(rseqh1) + '+' + loopsschar*len(rseqh2) + ss[index:]
        return (newseq, newss)

    else:   # adding the receptor to a double stranded seq
        splidx = seq.find('+')
        seqh1 = seq.split('+')[0]
        seqh2 = seq.split('+')[1]
        ssh1 = ss.split('+')[0]
        ssh2 = ss.split('+')[1]

        if index == -1: # add receptor to beginning of duplex
            newseq = rseqh1 + seqh1 + '+' + seqh2 + rseqh2
            newss = loopsschar*len(rseqh1) + ssh1 + '+' + ssh2 + loopsschar*len(rseqh2)
            return (newseq, newss)

        elif index == splidx: # add receptor to end of duplex
            newseq = seqh1 + rseqh1 + '+' + rseqh2 + seqh2
            newss = ssh1 + loopsschar*len(rseqh1) + '+' + loopsschar*len(rseqh2) + ssh2
            return (newseq, newss)

        else: # add receptor to middle of duplex (TODO)
            raise Exception("Not yet implemented")

# Function to generate a list of seqs with Single Point Mutations withing range of indices:
def get_point_mutants(seq, indices, seqname=""):
    mutant_seq = []
    mutant_name = []
    mutations = ['A', 'U', 'G', 'C', 'KO']
    mutant_seq.append(seq)
    mutant_name.append(seqname + "-WT")

    for idx in indices:
        initnt = seq[idx]
        if initnt not in mutations:
            raise Error("Index supplied cannot be mutated!")

        finalmutations = mutations.copy()
        finalmutations.remove(initnt)
        for mutation in finalmutations:
            mutantname = "%s-%s%d%s"%(seqname, initnt, idx+1, mutation)
            newseq = ""
            
            if mutation == "KO":
                newseq = seq[:idx] + seq[idx+1:]
            else:
                newseq = seq[:idx] + mutation + seq[idx+1:]

            mutant_seq.append(newseq)
            mutant_name.append(mutantname)
    return (mutant_seq, mutant_name)

