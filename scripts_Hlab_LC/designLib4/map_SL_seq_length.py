import pandas as pd
import matplotlib.pyplot as plt
import statistics

df = pd.read_csv("SL8_seq_to_project.csv", index_col = None)

print(df.head())
print(df.shape)

seq_lengths = []
for i,row in df.iterrows():
    x = len(df["sequence"][i])
    seq_lengths.append(x)

stdev = statistics.pstdev(seq_lengths)
m = statistics.mean(seq_lengths)
negdev = (m - (stdev))
sdev = (m + stdev)
min = min(seq_lengths)
max = max(seq_lengths)

plt.hist(seq_lengths)
plt.xlabel("Sequence #")
plt.ylabel("Length (nts)")
plt.title("Sublibrary 8: Kissing Loop")
plt.axvline(x = m, linewidth = 2, color = "black", label = ("mean = ", int(m)))
plt.axvline(x = sdev, linewidth = 2, color = "green", label = ("+1 stdev = ", int(sdev)))
plt.axvline(x = negdev, linewidth = 2, color = "green", label = ("-1 stdev = ", int(negdev)))
plt.axvline(x = min, linewidth = 2, color = "red", label = ("min = ", int(min)))
plt.axvline(x = max, linewidth = 2, color = "red", label = ("max = ", int(max)))
plt.legend()
#plt.ylim(0, 10)
plt.show()