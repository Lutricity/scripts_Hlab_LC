#Goal: run through the millions of possible chip helices with 4LVV in a controlable bitewise manner
#Make all 4LVV/TAR constructs
#Flag all helices that 'worked' and count the number of successful sequences they made
#run overnight

import pandas as pd
from support_THF_4LVV import *
import subprocess
import numpy as np


def main():

    #Load in sequence structures to tile and flip into the chip pieces
    df_motifs = pd.read_csv("input_motifs/TAR_20200821_1A.csv")


    # Load in the empty chip piece to tile motifs into
    for i in range(1967):
        count = 654 + i
        name = "chip_pieces/9bp_helices/9bp_4LVV_Hs" + str(count) + ".csv"
        #print("Reading in", name)
        df = pd.read_csv(name)
        num = "_"+ str(count)

        # Made blank pandas df to begin filling resulting chip pieces into
        df_result = pd.DataFrame(columns='project_name motif_name helix chip_type chip_sequence chip_structure insert_sequence insert_structure'.split())



# The following for loop iterates over each motif in 'motifs.csv', separates the 5' and 3' ends, then-
# it runs each motif through save_all_chip_piece_variant_for_motif, which appends the motif in every chip sequence to a dataframe
# then, for each motif, flip_motif() is called
# finally, save_all_chip_piece_variant_for_motif is called again n the flipped motif

        for i, row in df_motifs.iterrows():
            motif_seq_1 = row.sequence.split("+")[0]
            motif_seq_2 = row.sequence.split("+")[1]
            motif_ss_1 = row.structure.split("+")[0]
            motif_ss_2 = row.structure.split("+")[1]
            project_name = row.project_name
            motif_name = row.motif_name

            #print("call save all chip pieces")
            save_all_chip_piece_variant_for_motif(project_name, motif_name, df, df_result, motif_seq_1, motif_seq_2, motif_ss_1, motif_ss_2)


            lst = flip_motif(motif_seq_1, motif_seq_2, motif_ss_1, motif_ss_2)


            save_all_chip_piece_variant_for_motif(project_name, motif_name, df, df_result, lst[0], lst[1], lst[2], lst[3])

        #print("This is df result", df_result.head())
        #print(df_result.shape)
        df_result.to_csv("20200826_seqs_pre_RNAfolded.csv", index=False)

    #Below this comment begins trying to match chip_structure against RNAfold's predicted secondary structure for a sequence.
        df_result['chip_sequence'].to_csv("chip_seqs_to_RNAfold.csv", index = False, header = False)


        subprocess.call("RNAfold -T20 --noLP chip_seqs_to_RNAfold.csv > out", shell = True)

        f = open("out")
        lines = f.readlines()
        RNAfold = pd.DataFrame(np.array(lines).reshape(-1, 2))
        f.close()

        RNAfold['ss'] = RNAfold[1].str.split(" ").str[0]
        print(RNAfold.head())

        chip_real_structure = []
        chip_real_structure.append(RNAfold['ss'])


        #Now I have a list with the RNAfold secondary structure. Next I will:
        #append this to a new column in a dataframe with my program results, then I will throw out any rows whose
        #chip_structure column and ss column don't match

        final_df = df_result.copy()
        final_df['RNAfold_structure'] = RNAfold['ss']


        #print(final_df.head())
        #print("Before cutting misfolded constructs", final_df.shape)

        for i, row in final_df.iterrows():
            # check if anything PAST receptor loop is different(chip constructs seem to commonly access two states)
            #if final_df['chip_structure'][i] != final_df['RNAfold_structure'][i]:
            if final_df['chip_structure'][i][10:] != final_df['RNAfold_structure'][i][10:] and final_df['chip_structure'][i][:-15] !=  final_df['RNAfold_structure'][i][:-15]:
                final_df.drop(i, inplace=True)

        #print(final_df.head())
        #print("After cutting misfolded constructs", final_df.shape)

        new_name = "folded/9bp/9bp_4LVV.4_4LVV_RNAfolded_20200915"+ num + ".csv"
        print("Making", new_name, "with shape", final_df.shape )
        final_df.to_csv(new_name, index=False)




if __name__ == "__main__":
    main()


#for i in range(655):
 #   name = "chip_pieces/12bp_helices/8bp_4LVV_Hs"+str(i) + ".csv"
  #  helix_df = pd.read_csv("name")

#Below section splits a large csv of chip piece helices int many smaller csvs
#read in chip pieces
#helix_df = pd.read_csv("chip_pieces/12bp_all_4LVV_chip_pieces.csv")
#print(helix_df.head(10))
#split up number of chip pieces into number of dfs to be run
#rw, cl = helix_df.shape
#num = rw//100

#pos = 0
#for i in range(num):
 #   name = "chip_pieces/12bp_helices/12bp_4LVV_Hs"+str(i) + ".csv"
  #  if i == 0:
   #     x = helix_df.iloc[0:100]
    #    x.to_csv(name)
    #else:
     #   v1 = i*100
      #  v2= (i+1)*100
       # y = helix_df.iloc[v1:v2]
        #y.to_csv(name)




#set input csv variable


#set output csv variables

# in final_df from test program, count how many repeats of each helix index, and return a list starting with most 'populous' chip pieces