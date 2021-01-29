import pandas as pd
import numpy as np



def flip_motif(seq_1, seq_2):
    flip_seq1 = seq_2
    flip_seq2 = seq_1



    return [flip_seq1, flip_seq2]


def main():
    df_motifs = pd.read_csv("150_chip_helices.csv")
    print(df_motifs.columns)
    print(df_motifs.head())

    h1 = []
    h2 = []

    for i, row in df_motifs.iterrows():
        name = row.sequence
        helix_seq_1 = row.sequence.split("+")[0]
        helix_seq_2 = row.sequence.split("+")[1]
        #helix_ss_1 = row.ss.split("+")[0]
        #helix_ss_2 = row.ss.split("+")[1]

        x, y = flip_motif(helix_seq_1, helix_seq_2)
        h1.append(x)
        h2.append(y)

    flipped = []
    for j in range(len(h1)):
        new_seq = h1[j] + "+" + h2[j]
        flipped.append(new_seq)

    df2 = df_motifs[['name','sequence', 'ss']].copy(deep = True)
    nseqs = pd.DataFrame(flipped, columns = ['sequence'])
    #print(nseqs.head())

    df2['sequence'] = nseqs['sequence']
    print(df2.head())

    df2.to_csv("flipped_150_chip_helices.csv")

if __name__ == "__main__":
    main()
