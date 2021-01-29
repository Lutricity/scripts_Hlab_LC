import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
from statistics import *




def main(argv):

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('This program plots a histogram of how many repeats per barcode in the library. Run on foo.stat  from compressBarcodes_v8.py \n distributionList.py -i <inputfile>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print('This program plots a histogram of how many repeats per barcode in the library. Run on foo.stat from compressBarcodes_v8.py \n distributionList.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg


    with open(inputfile) as f:
        barcodeDist = f.readlines()
    barcodeDist = [x.strip() for x in barcodeDist]
    #print(barcodeDist[100000:101000])
    f.close()

    barcodeInts = [int(x) for x in barcodeDist]



    fig, ax = plt.subplots()
    temp = np.sort(barcodeInts)
    ax.hist(temp, bins=range(500), color = 'darkblue')

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
    print("The max number of clusters for a barcode is:", most)
    print("The number of cluster with only one read is:", pos)
    print("The median number of clusters per barcode in ~8 million reads~ is:", med)
    print("The mean number of clusters per barcode in ~8 million reads~ is:", meany)

    #print(barcodeInts)
    #lbl_list = ax.get_xticklabels()
    #lbl_list

    plt.title('# of Cluster per Barcode')
    plt.xlabel("Unique Lib Variant")
    plt.ylabel("# barcodes")
   # plt.ylim(top=40000)
    plt.xlim(left=2)
    ax.set_xlim(left = 1, right = 50)
    ax.set_ylim
    #ax.set_xticklabels()
    plt.show()

    #myplot = sns.histplot(barcodeDist, kde=True, bins = 100,
                  #color = 'darkblue', stat = "count")


    plt.title('# of Cluster per Barcode')
    plt.xlabel("Per Barcode Variant in Lib 4 (407,000 barcodes)")
    plt.ylabel("# clusters")
    #plt.ylim(top=40000)
    plt.xlim(left=2)

    #new_ticks = [i.get_text() for i in myplot.get_xticklabels()]
    #plt.xticks(range(0, len(new_ticks), 10), new_ticks[::10])

    #plt.show()




if __name__ == "__main__":
   main(sys.argv[1:])