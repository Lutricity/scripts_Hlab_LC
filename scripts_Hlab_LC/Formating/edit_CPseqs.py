# Written by Lena Cuevas, Stanford University, 11/18/2020
# goal- remove Ns from columns 3 (R1), 4 (Q_read1) & 7(BC), 8 (QBC) in Sarah's CPseq files

# import statement
import pandas as pd
import time

#setting slicing variable
start_v = 1
stop_v = -1

#setting input/output file names
in_foo = "bite_AEL52.CPseq"
out_foo = "corrected_bite_AEL52.CPseq"

#read in the active columns of the CPSeq to be eited
CPseq = pd.read_csv(in_foo, delimiter="\t", index_col = False, usecols = [2, 3, 6, 7], names = ["R1", "QR1", "BC", "QBC"])
#names = ["location", "exp", "R1", "QR1", "R2", "QR2", "BC", "QBC", "BS1"], )
start_time = time.time()

#correctly format dataframe
#CPseq.drop("BS1", axis = 1, inplace = True)

#define string as datatype to speed up program (I think)
CPseq["R1"].str
CPseq["QR1"].str
CPseq["BC"].str
CPseq["QBC"].str

CPseq.dropna(inplace = True)
print(CPseq.head())

# converting to string data type
CPseq["R1"] = CPseq["R1"].astype(str)
CPseq["QR1"] = CPseq["QR1"].astype(str)
CPseq["BC"] = CPseq["BC"].astype(str)
CPseq["QBC"] = CPseq["QBC"].astype(str)


# slicing away first element
CPseq["R1"] = CPseq["R1"].str.slice(start = start_v)
CPseq["QR1"] = CPseq["QR1"].str.slice(start = start_v)
CPseq["BC"] = CPseq["BC"].str.slice(start = start_v)
CPseq["QBC"] = CPseq["QBC"].str.slice(start = start_v)

#checking success
print(CPseq.head())
print(CPseq.shape)
print()

#read in the rest of the csv file
CPseq_leaf = pd.read_csv(in_foo, delimiter="\t", index_col = False, usecols = [0, 1, 4, 5], names = ["location", "exp", "R2", "QR2"])
#["location", "exp", "R1", "QR1", "R2", "QR2", "BC", "QBC", "BS1"]

#make a list of dataframes and append them to the final dataframe
l1 = [CPseq_leaf["location"], CPseq_leaf["exp"], CPseq["R1"], CPseq["QR1"], CPseq_leaf["R2"], CPseq_leaf["QR2"], CPseq["BC"], CPseq["QBC"]]

final = pd.concat(l1, axis = 1)

#saving output file
final.to_csv(out_foo, sep="\t", index = False)

print("--- %s seconds ---" % (time.time() - start_time))