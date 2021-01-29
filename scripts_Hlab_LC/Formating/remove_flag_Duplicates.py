import numpy as np
import pandas as pd
from collections import Counter
###read in tertiary contact sequences
# read in csv file - assuming the col with sequences is named “sequence"
df = pd.read_csv("last_TAR_1B_20200929.csv")
print(df.head())
print(df.columns)
#Make a series of all the unique sequences, then check how many repeat sequences there are

#uni = df['sequence'].unique()
#one = len(df['sequence'])
#two = len(uni)

#print("There were", one, "original seqs. After cutting repeats there are", two)

#Make a second dataframe with only unique seqs
#Add a column of how many times that sequecne is repeated
#double up on names (add multiple name columns/ max repeat of a seq- if >4 then start combining strings instead- write that part if needed)


#Roy- all of the above is me thinking about hte best way to accomplish the goals in my email, def take with a grain of salt

# add whatever is needed to read in files/ import libs


#df = pd.read_csv(csvfilename)
# read in csv file - assuming the col with sequences is named “sequence"

listofseqs = df['chip_sequence'].tolist()
# convert the col of sequences into a python list

counts = dict(Counter(listofseqs))
# counts the # of occurrences of each seq in listofseqs

counting = []
for k in counts.keys():
# print out each seq and how many times its in the list
    x = "%s => %d repeats" % (k, counts[k])
    counting.append(x)
    #print(x)

#df2 = pd.DataFrame(counting)
#df2.to_csv("repeated_ mseqs.csv")
# Filter out only the seqs that are present > 1 times:
listofrepeatedseqs = []
for k in counts.keys():
    if counts[k] > 1:
        listofrepeatedseqs.append(k)
print("Number repeats:", len(listofrepeatedseqs))
#print(counts)

repeated = {}
for i in counts:
    #if counts[i] > 1:
    df1 = df[df['chip_sequence'].str.contains(i)]
    #df1 = df["sequence"] = i
    y = df1["project_name"].tolist()
    #print(df1)
    d = []
    for u in y:
        if u not in d:
            d.append(u)
    repeated[i] = d
print(repeated)
# Filter out duplicate elements in data frame (to create a new df)
# uses sequence col Vals to look for duplicates and keeps the first df entry among the repeated entries:
dfunique = df.drop_duplicates(subset= "chip_sequence", keep = 'first')
seqs = df["chip_sequence"]

# Filter out repeated elements (all repeats, including the first one)
#dfrepeat = df[seqs.isin(seqs[seqs.duplicated()])].sort_values("sequence")
dfrepeat = pd.DataFrame.from_dict(repeated, orient = 'index')
print(dfrepeat.head())
#dfrepeat.columns = ['sequence', 'name0', 'name1', 'name2', 'name3']
#print(dfunique)
#print(dfrepeat)

# no. of seqs removed:
print("removed: %d" % (df.shape[0] - dfunique.shape[0]))
#print(repeated)
dfunique.to_csv("SL1_last_unique_sorted_seqs.csv")
dfrepeat.to_csv("SL1_last_seqs_to_project.csv")