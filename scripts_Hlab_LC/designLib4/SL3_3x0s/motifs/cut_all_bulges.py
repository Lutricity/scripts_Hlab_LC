import pandas as pd
df = pd.read_csv("all_3x0_bulges_test.csv")

df["motif_name"]
print(df.shape)

for i, row in df.iterrows():
    if "GGGG" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass

for i, row in df.iterrows():
    if "AAAA" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass

for i, row in df.iterrows():
    if "CCCC" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass

for i, row in df.iterrows():
    if "UUUU" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass

for i, row in df.iterrows():
    if "UUU" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "UCU" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "CCC" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "+UC" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "GGG" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "AAA" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "GG+CC" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "CC+GG" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "AA+UU" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
for i, row in df.iterrows():
    if "UU+AA" in df["sequence"][i]:
        df.drop(i, inplace=True)
    else:
        pass
#to_drop = ["GGGG", "CCCC", "UUUU", "AAAA"]
#df2 = df[~df["sequence"].isin(to_drop)]
#for i, row in df.iterrows():
 #   df["sequence"][i].drop(to_drop)

print(df.shape)
df.to_csv("cut_more_all_3x0_bulges.csv")