#check ss and remove seqs whose tert contacts don't match up
import pandas as pd
import subprocess
import numpy as np

df = pd.read_csv("THF_kts.csv")


df['sequence'].to_csv("chip_seqs_to_RNAfold.csv", index = False, header = False)

subprocess.call("RNAfold -T20 --noLP chip_seqs_to_RNAfold.csv > out", shell = True)

f = open("out")
lines = f.readlines()
RNAfold = pd.DataFrame(np.array(lines).reshape(-1, 2))
f.close()

RNAfold['ss'] = RNAfold[1].str.split(" ").str[0]
print(RNAfold.head())

chip_real_structure = []
chip_real_structure.append(RNAfold['ss'])

# Now I have a list with the RNAfold secondary structure. Next I will:
# append this to a new column in a dataframe with my program results, then I will throw out any rows whose
# chip_structure column and ss column don't match

final_df = df
final_df['RNAfold_structure'] = RNAfold['ss']

print(final_df.head())
print("Before cutting misfolded constructs", final_df.shape)

for i, row in final_df.iterrows():
    # check if anything PAST receptor loop is different(chip constructs seem to commonly access two states)
    # if final_df['chip_structure'][i] != final_df['RNAfold_structure'][i]:
    if final_df['RNAfold_structure'][i][:5] != "(((((" and  final_df['RNAfold_structure'][i][-5:] != ")))))":
        # final_df["motif_name"][i] = 'misfold_' + final_df["motif_name"][i]
        final_df.drop(i, inplace=True)


print(final_df.head())
print("After cutting misfolded constructs", final_df.shape)

# final_df.drop(columns=['RNAfold_structure'])
# Figure out how to do the above later- not important now

final_df.to_csv("72_RNAfolded_20200922.csv", index=False)