import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys, getopt
from statistics import *




def main(argv):

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('This program plots a histogram of how many barcodes per cluster in the library. Run on foo.csv- two column csv with seq in col1 and counts in col2 \n distributionList.py -i <inputfile>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print('This program plots a histogram of how many repeats per barcode in the library. Run on foo.stat from compressBarcodes_v8.py \n distributionList.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg


    count_file = pd.read_csv(inputfile)
    barcodesOfVars = count_file.iloc[:, 1]
    #print(count_file.iloc[:, 1])
    #print("Shape", barcodesOfVars.shape)
    print(type(barcodesOfVars))

    fig, ax = plt.subplots()
    temp = np.sort(barcodesOfVars)
    ax.hist(temp, bins=range(60), color = 'olivedrab', ec='white')

    # analyze stats
    # What is the median # copies per barcode sequence in 8 million reads?
    # What is the max # copies?
    # How many only have one cluster?
    most = max(temp)
    med = median(temp)
    meany = mean(temp)

    pos = 0
    for i in temp:
        if i == 1:
            pos += 1

    #Then - what was this for Lib 2 for S&N
    print("Analyzed", len(temp), "lib variants.")
    print("The max number of barcodes per variant is:", most)
    print("The number of variants with only one barcode is:", pos)
    print("The median number of clusters per barcode in ~8 million reads~ is:", med)
    print("The mean number of clusters per barcode in ~8 million reads~ is:", meany)

    #print(barcodeInts)
    #lbl_list = ax.get_xticklabels()
    #lbl_list

    plt.title('# Barcodes per Library Variant (Total Lib4)')
    plt.xlabel("Unique Lib Variant")
    plt.ylabel("# barcodes")
    plt.ylim(top=2000)
    #plt.xlim(left=2)
    ax.set_xlim(left = 1, right = 60)
    ax.set_ylim
    #ax.set_xticklabels()
    plt.show()

    #myplot = sns.histplot(barcodeDist, kde=True, bins = 100,
                  #color = 'darkblue', stat = "count")


    plt.title('# of Cluster per Barcode')
    plt.xlabel("Unique Lib Variant")
    plt.ylabel("# barcodes")
    #plt.ylim(top=40000)
    plt.xlim(left=2)

    #new_ticks = [i.get_text() for i in myplot.get_xticklabels()]
    #plt.xticks(range(0, len(new_ticks), 10), new_ticks[::10])

    #plt.show()




if __name__ == "__main__":
   main(sys.argv[1:])