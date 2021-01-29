import subprocess

#Below: open english dict and read each line/word into a list

pos = 0
f = open("words2.txt", 'r')
real_words = f.read().splitlines()
f.close()


#Below: open war and peace and word/element into a list.


f = open("war_and_peace.txt", "r", 1)
book = f.read().split(" ")
    #
war_peace_parts = []
war_peace_words = []
final_book = []
for i in book:
    for j in i:
    war_peace_parts.append(i.split(" "))

#Below: organize each element in all the lists in the book list of lists into a separate
# list of each word (final_book).

for j in war_peace_parts:
    for l in j:
        final_book.append(l)

#PROBLEMS- DOES NOT DISTINGUISH BETWEEN CAPITALIZATION AND LOWERCASE
# IF A WORD CONTAINS AN APOSTRAPHE OR OTHER NON-ALPHA CHACARCTER THE PROGRAM DOES NOT RECOGNIZE IT AS A REAL WORD

#Below: Checks if each element in final_book is in the english dict and adds them to a list if they are.

real_wp_words = []


for i in book:
  if i in real_words:
      real_wp_words.append(i)
  else:
      pass

#print(real_wp_words)

#Below: makes a list of all the word lengths in the real words from war and peace.

word_lengths = []
for e in real_wp_words:
    if len(e) not in word_lengths:
        word_lengths.append(len(e))
print(word_lengths)

#Below: checks each word
# then assigns true words of the longest four lengths in war and peace to their length list

longest_words = []
long1 = []
long2 = []
long3 = []
for ee in real_wp_words:
    if len(ee) == max(word_lengths):
        longest_words.append(ee)
    elif len(ee) == max(word_lengths)-1:
        long1.append(ee)
    elif len(ee) == max(word_lengths)-2:
        long2.append(ee)
    elif len(ee) == max(word_lengths) - 3:
        long3.append(ee)
    else:
        pass



print(longest_words, "Above are the longest real words in War and Peace.")
#print(long1)
#print(long2)
#print(long3)



