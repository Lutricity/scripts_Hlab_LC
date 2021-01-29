import pandas as pd
import subprocess
import numpy as np

# Make three cutting/tiling programs- where the internal
# region shortens from the top, from the bottom,
# and depending on the even and odd cuts up one way, then down from the other


# I'll have to define the hairpin region variably? in each cut program?



# every time make end_5variable smaller ex: -20, -19...

# def seq_2cut_top(long_seq, long_ss):

# def seq_2cut_bottom(long_seq, long_ss):

def flip_motif(seq_1, seq_2, ss_1, ss_2):
    flip_seq1 = seq_2
    flip_seq2 = seq_1
    flip_ss1 = ""
    flip_ss2 = ""

    for i in range(0, len(ss_2)):
        if ss_2[i] == ")":
            flip_ss1 += "("
        else:
            flip_ss1 += "."
    #print(flip_ss1)

    for i in range(0,len(ss_1)):
        if ss_1[i] == "(":
            flip_ss2 += ")"
        else:
            flip_ss2 += "."
    #print(flip_ss2)

    return [flip_seq1, flip_seq2, flip_ss1, flip_ss2]


# Next step- work flip script into the order of operations to it runs quickly and seemlessly

def tile_motif_in_chip_sequence(chip_seq, chip_ss, seq_1, seq_2, ss_1, ss_2):
    count = 0
    # the first while loop i'll have to make should contain flip scrip and while the count = 0 then no flip script, else flip script, exit at third count
    # make another while loop up here that edits the original sequence between certain positions, cutting in pairs or adding in pairs

    # elif len(chip_seq)


    #length_offset = (len(chip_seq) - 47) // 2
    #print("This is the length offset", length_offset)

    start_pos = 14
    end_pos = -15

    start_hair = 20
    end_hair = 25
    #print("This is start_hair", start_hair)
    #print("This is end_hair", end_hair)

    tecto_variants = []

    #while 1:

    start_5prime = chip_seq[0:start_pos]
    #print("Start 5'",start_5prime)
    ss_start_5prime = chip_ss[0:start_pos]
    start_3prime = chip_seq[end_pos:]
    #print("Start 3'", start_3prime)
    ss_start_3prime = chip_ss[end_pos:]
    hairpin = chip_seq[start_hair:end_hair]
    #print("Hairpin:", hairpin)
    ss_hairpin = chip_ss[start_hair:end_hair]
    helix_5prime = chip_seq[start_pos:start_hair]
    #print("Helix 5'", helix_5prime)
    ss_helix_5prime = chip_ss[start_pos:start_hair]
    helix_3prime = chip_seq[end_hair:end_pos]
    #print("Helix 3'", helix_3prime)
    ss_helix_3prime = chip_ss[end_hair:end_pos]
    motif_length = len(seq_1)
    if motif_length > len(seq_2):
        motif_length = len(seq_2)

    #if len(helix_5prime) < motif_length:
     #   break

    # print start_5prime, start_3prime

    new_helix_5prime = seq_1 + helix_5prime[motif_length:start_hair + 1]
    new_helix_3prime = helix_3prime[0:-motif_length] + seq_2

    ss_new_helix_5prime = ss_1 + ss_helix_5prime[motif_length:start_hair + 1]
    ss_new_helix_3prime = ss_helix_3prime[0:-motif_length] + ss_2

    final_sequence = start_5prime + new_helix_5prime + hairpin + new_helix_3prime + start_3prime
    ss_final = ss_start_5prime + ss_new_helix_5prime + ss_hairpin + ss_new_helix_3prime + ss_start_3prime

    #print(final_sequence)
    #print(ss_final)

    tecto_variants.append([final_sequence, ss_final])
        #tecto_variants is the list of lists that contains the final outputs of define_motif_in_chip_sequence




        #start_pos += 1
        #end_pos -= 1
        #count += 1
        # if count > 1:
        # exit()
        # exit()
    return tecto_variants

def save_all_chip_piece_variant_for_motif(project_name, motif_name, df, df_result, motif_seq_1, motif_seq_2, motif_ss_1, motif_ss_2):
    pos = len(df_result)
    for i, row in df.iterrows():
        motif_tile_output = tile_motif_in_chip_sequence(row.sequence, row.structure, motif_seq_1, motif_seq_2, motif_ss_1, motif_ss_2)
        for l in motif_tile_output:
            #if l[1] ==
            df_result.loc[pos] = [project_name, motif_name, row['name'], l[0], l[1], motif_seq_1 + "+" + motif_seq_2,
                                  motif_ss_1 + "+" + motif_ss_2]
            pos += 1




def main():

    #Load in sequence structures to tile and flip into the chip pieces
    df_motifs = pd.read_csv("../../motifs/3x0_in_TARbp_shorter.csv")

    #Load in the empty chip piece to tile motifs into
    df = pd.read_csv("3x0_11ntR_chip_pieces.csv")

    #Made blank pandas df to begin filling resulting chip pieces into
    df_result = pd.DataFrame(columns='project_name motif_name chip_type chip_sequence chip_structure insert_sequence insert_structure'.split())

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

        save_all_chip_piece_variant_for_motif(project_name, motif_name, df, df_result, motif_seq_1, motif_seq_2, motif_ss_1, motif_ss_2)

#comment out the next two lines of code to get rid of flipped motifs
        lst = flip_motif(motif_seq_1, motif_seq_2, motif_ss_1, motif_ss_2)

        save_all_chip_piece_variant_for_motif(project_name, motif_name, df, df_result, lst[0], lst[1], lst[2], lst[3])


    df_result.to_csv("20200721_seqs_pre_RNAfolded.csv", index=False)

#Below this comment begins trying to match chip_structure against RNAfold's predicted secondary structure for a sequence.
    df_result['chip_sequence'].to_csv("chip_seqs_to_RNAfold.csv", index = False, header = False)


    subprocess.call("RNAfold -T20 chip_seqs_to_RNAfold.csv > out", shell = True)

    f = open("out")
    lines = f.readlines()
    RNAfold = pd.DataFrame(np.array(lines).reshape(-1, 2))
    f.close()
    #print(RNAfold)
    RNAfold['structure'] = RNAfold[1].str.split(" ").str[0]
    print(RNAfold.head())

    chip_real_structure = []
    chip_real_structure.append(RNAfold['structure'])


    #Now I have a list with the RNAfold secondary structure. Next I will:
    #append this to a new column in a dataframe with my program results, then I will throw out any rows whose
    #chip_structure column and ss column don't match

    final_df = df_result
    final_df['RNAfold_structure'] = RNAfold['structure']


    print(final_df.head())
    print("Before cutting misfolded constructs", final_df.shape)

    for i, row in final_df.iterrows():
        if final_df['chip_structure'][i][11:] != final_df['RNAfold_structure'][i][11:] and final_df['chip_structure'][i][:-12] != final_df['RNAfold_structure'][i][:-12] and final_df['RNAfold_structure'][i][21:27] !=  final_df['chip_structure'][i][21:27]:
            #final_df["motif_name"][i] = 'misfold_' + final_df["motif_name"][i]
            final_df.drop(i, inplace=True)

    print(final_df.head())
    print("After cutting misfolded constructs", final_df.shape)

    #final_df.drop(columns=['RNAfold_structure'])
    #Figure out how to do the above later- not important now

    final_df.to_csv("3.A_one_RNAfold_3x0_all_20200921.csv", index=False)




if __name__ == "__main__":
    main()

