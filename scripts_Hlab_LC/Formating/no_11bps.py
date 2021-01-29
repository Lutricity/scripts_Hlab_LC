import pandas as pd
df = pd.read_csv("3A_11ntRs.csv")
print(df.columns)

for i, row in df.iterrows():
    if "11bp" in df["chip_type"][i]:
        df.drop(i, inplace=True)


df.to_csv("3A_no11bp.csv")