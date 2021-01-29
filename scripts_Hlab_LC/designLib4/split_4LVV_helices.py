import pandas as pd



#for i in range(655):
    #name1 = "chip_pieces/12bp_helices/8bp_4LVV_Hs"+str(i) + ".csv"
    #helix_df = pd.read_csv(name1)

#Below section splits a large csv of chip piece helices int many smaller csvs
#read in chip pieces
helix_df = pd.read_csv("chip_pieces/12bp_all_4LVV_chip_pieces.csv")
print(helix_df.head(10))
#split up number of chip pieces into number of dfs to be run
rw, cl = helix_df.shape
num = rw//100

for i in range(num):
    name = "chip_pieces/12bp_helices/12bp_4LVV_Hs"+str(i) + ".csv"
    if i == 0:
        x = helix_df.iloc[0:100]
        x.to_csv(name)
    else:
        v1 = i*100
        v2= (i+1)*100
        y = helix_df.iloc[v1:v2]
        y.to_csv(name)




#set input csv variable


#set output csv variables

# in final_df from test program, c