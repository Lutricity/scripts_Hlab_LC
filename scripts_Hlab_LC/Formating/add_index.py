import pandas as pd

df = pd.read_csv("12bp_all_4LVV_chip_pieces.csv")
#df2 = df[['name', 'sequence', 'structure']]
hlx_indx = []
for i, row in df.iterrows():
    string = "12p"+ str(i)
    hlx_indx.append(string)

df_ind  = pd.DataFrame(hlx_indx, columns = ["helix"])

print(df.shape)
print("This is new", df_ind.shape)
print(df_ind.head)

df3 = pd.concat([df_ind, df], axis = 1)

print(df_ind.columns)
print(df.columns)
print(df3.columns)
print(df.head())
print(df3.head())

df3.to_csv("12bp_all_4LVV_chip_pieces.csv", index=False)