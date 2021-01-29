import pandas as pd


df_motifs = pd.read_csv("../SL7_Kinkturns/check_structures.csv")
df = pd.DataFrame(df_motifs)
print(df_motifs[0:20])
print(df[0:20])

df['sequence'] = df['sequence'].str.strip()
df['sequence'] = df['sequence'].str.replace(' ','')

#for i, row in df.iterrows():
 #   seq = row.sequence
  #  seq.replace("  ", "")
   # seq.replace(" ", "")
    #print("THis is seq",seq)

print(df.shape)
print(df.head())

df.to_csv("extended_kts_nospace.csv", index=False)
