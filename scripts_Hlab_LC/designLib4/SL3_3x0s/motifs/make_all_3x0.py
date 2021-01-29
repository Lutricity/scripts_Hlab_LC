import pandas as pd

nts = "G", "C", "A", "U"
print("running")
list = []
#for i in range(5):
for j in nts:
    str = j
    list.append(str)


list2 = list
for l in list:
    if len(l) > 4:
        exit

    else:
        for m in nts:
            str2 = l + m
            list2.append(str2)

list3 = []
for f in list2:
    if len(f) == 5:
        list3.append(f)

three_prime = []
#print(list3)
print(len(list3))
pos = 0
for r in range(len(list3)):
    #print(list3[r][0:1])
    d = list3[r][0:1]
    pos += 1
    print(pos, d)
    if d == "G":
        n1 = "C"
        three_prime.append(n1)
    elif d == "C":
        n1 = "G"
        three_prime.append(n1)
    elif d == "U":
        n4 = "A"
        three_prime.append(n4)
    elif d == "A":
        n1 = "U"
        three_prime.append(n1)

    else:
        exit


#print(three_prime)
for k in range(len(list3)):
    if list3[k][4:5] == "G":
        n2 = "+C" + three_prime[r]
        three_prime.append(n2)
    elif list3[k][4:5] == "C":
        n2 = "+G" + three_prime[r]
        three_prime.append(n2)
    elif list3[k][4:5] == "A":
        n2 = "+U" + three_prime[r]
        three_prime.append(n2)
    elif list3[k][4:5] == "U":
        n2 = "+A" + three_prime[r]
        three_prime.append(n2)

#print(three_prime)


prime = []
for s in three_prime:
    if len(s) == 3:
        prime.append(s)

#print(prime)
final_list = []

for w in range(len(list3)):
    x = list3[w] + prime[w]
    #print(x)
    final_list.append(x)

listing = []
for u in final_list:
    new = u[:7]
    d = new[0:1]
    if d == "G":
        n1 = "C"
        a = new + n1
        listing.append(a)
    elif d == "C":
        n1 = "G"
        a = new + n1
        listing.append(a)
    elif d == "U":
        n1 = "A"
        a = new + n1
        listing.append(a)
    elif d == "A":
        n1 = "U"
        a = new + n1
        listing.append(a)

print(listing)
print(len(listing))
df = pd.DataFrame(listing)
df.to_csv("all_3x0_bulges_test_2.csv")