#this is for vowpal wabbit

from hazm import sent_tokenize
from hazm import Normalizer

def readData(fileName):
    file = open(fileName, 'r')
    data = file.read().split(u".")
    sample_set = []
    for sample in data:
        if sample.__len__() > 1:
            sample_set.append(sample)
    return sample_set

file=open("result.txt","w")
#reading data
file1 = 'book1.txt'
file2 = "book2.txt"
sample_set1 = readData(file1)
sample_set2=readData(file2)

#Normalizind data
n = Normalizer()
for sample in sample_set1:
    sample = n.normalize(sample)

n = Normalizer()
for sample2 in sample_set2:
    sample2 = n.normalize(sample2)

#SENTENCE TOKENIZATION

all_sentences1 = []
for sample in sample_set1:
    sentences1 = sent_tokenize(sample)
    all_sentences1.extend(sentences1)
#print(all_sentences)

all_sentences2 = []
for sample in sample_set2:
    sentences2 = sent_tokenize(sample)
    all_sentences2.extend(sentences2)

size2=all_sentences2.__len__()
size1=all_sentences1.__len__()

if(size1> size2):
        num = size2
elif(size1< size2):
        num = size1


all_words = {}
cnt1 =1
cnt2 = 0
print(num)
for s in all_sentences1:
    all_words[cnt1] = s
    cnt1 += 2
    if (cnt1 > 2*num):
        break

for s in all_sentences2:
    all_words[cnt2] = s
    cnt2 += 2
    if (cnt2 > 2*num):
        break

for k , v in all_words.items():
    m = divmod(k,2)
    if m[1]==0:
        file.write("-1" + '|' + v + "\n")
    else:
        file.write(str(m[1]) + '|' + v + "\n")

file.close()








