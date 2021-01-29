#Lena Cuevas, Stanford University, Jan 2021
# make a grouped bar graph with matplotlib
# see example code https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/bar_stacked.html

#import statements
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys, getopt

# hardcoded lib 4 variables
total_lib4 = 29836

#calc percent
def percentage(part, whole):
  return 100 * float(part)/float(whole)

# add labels on top of the bar graph
def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize = 12)


#main
def main(argv):

# input argument parser
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('This program plots a grouped bargraph of two correlated columns in a csv. Run on foo.csv   \n groupedBarGraph.py -i <inputfile>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print('This program plots a grouped bargraph of two correlated columns in a csv. Run on foo.csv   \n groupedBarGraph.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg

# parse csv columns
    data = pd.read_csv(inputfile, index_col = False)
    front = data.iloc[:, 1]
    back = data.iloc[:, 2]

    head = []
    tail = []

    for i in front:
        pcnt = int(percentage(i, total_lib4))
        head.append(pcnt)

    for j in back:
        pcnt = int(percentage(j, total_lib4))
        tail.append(pcnt)

    print("Data set 1:", head)
    print("Data set 2", tail)


    N = 3
    ind = np.arange(N)
    width = 0.25
    labels = ["1", "2", "3"]

    fig, ax = plt.subplots()
    chip_one = ax.bar(ind - width/2, head, width, label='chip 1', color = 'crimson' )
    chip_two = ax.bar(ind + width/2, tail, width, label='chip 2', color = 'darkmagenta')


    autolabel(chip_one, ax)
    autolabel(chip_two, ax)

    ax.set_ylabel('% of Lib Represented', fontsize = 16)
    ax.set_xlabel('# Sequencing Reads (Millions)', fontsize = 16)
    ax.set_title('% of Library with ≥ 5 Counts', y=1.0, fontsize = 18)
    ax.set_xticks(ind)
    ax.set_xticklabels(labels, fontsize = 12)
    ax.set_yticks(np.arange(0, 110, 10))
    ax.legend(loc = 'lower left', fontsize = 12)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])