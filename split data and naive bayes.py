#!/usr/bin/env python
# -*- coding: utf-8 -*-

#this file split data to train and test

import random,math
from collections import Counter
import random
from classprob import firstclassprob,secondclassprob
from sklearn.metrics import  precision_score, recall_score

file1 = open("train1.txt", "r")
class1={}
counter1=0
for line in file1:
    counter1+=1
    class1[counter1]=line

file2 = open("train2.txt", "r")
class2={}
counter2=0
for line in file2:
    counter2+=1
    class2[counter2]=line

testout=open("randomtest.txt" ,"w")
train1=open("randomtrain1.txt" ,"w")
train2=open("randomtrain2.txt" ,"w")
x=(random.randint(0,9))
y=(x+1)/10
x=x/10
y1=int(y*counter1)
x1=int(x*counter1)

x=(random.randint(0,9))
y=(x+1)/10
x=x/10
y2=int(y*counter2)
x2=int(x*counter2)



for i in range (1,counter1):
    if (i>=x1 and i<=y1):
        testout.write("1"+"\t"+class1[i]+"\n")
    else:
        train1.write(class1[i]+"\n")

for j in range (1,counter2):
    if (j>=x2 and j<=y2):
        testout.write("2"+"\t"+class2[j]+"\n")
    else:
        train2.write(class2[j]+"\n")




first = {}
with open(r'randomtrain1.txt') as f:
    words = [word for line in f for word in line.split()]
    first_num = len(words)
    print("The total word count is:", first_num)
    c = Counter(words)
    for word, count in c.most_common():
            #print(word)

        first[word] = (math.log10(count/first_num))
        #first[word] = (math.log10(count+1/first_num+counter1))     #for smoothing



second = {}
with open(r'randomtrain2.txt') as f:
    words = [word for line in f for word in line.split()]
    second_num = len(words)
    print("The total word count is:", second_num)
    c = Counter(words)
    for word, count in c.most_common():
            #print(word)

        second[word] = (math.log10(count/second_num))
        #second[word] = (math.log10(count+1/second_num+counter2))     #for smoothing





smoothing1=math.log10(1/(first_num+counter1))
smoothing2=math.log10(1/(second_num+counter2))

cnttemp1 = 0
cnttemp2 = 0
cnt1 = 0
cnt2 = 0
tp1=0
tp2=0
fp2=0
fp1=0
featureimpact={}
f=open("randomtest.txt","r")
for line in f:
    summing1=0
    summing2=0
    for obj in line.split("\t"):
        if(obj == "1" or obj=="2"):
            real = obj
        else:
            print(obj)
            for word in obj.split(" "):
                #print(word,"\n")
                if word in first:
                     summing1+=first[word]
                else:
                    #summing1 +=smoothing1
                    summing1+=-7
                if word in second:
                    summing2+=second[word]
                else:
                    summing2+=-7
                    #summing2 +=smoothing2


    #print("real:" + real)
    if(real == "1"):
        cnt1 +=1
    if(real == "2"):
        cnt2 +=1
    p1=summing1*(1/firstclassprob())
    p2=summing2*(1/secondclassprob())
    """print("class1:")
    print(p1)
    print(summing1)
    print(1/firstclassprob())
    print("class2:")
    print(p2)
    print(summing2)
    print(1/secondclassprob())"""

    if (p1<p2):
        #print("class2")
        cnttemp2 +=1
        if real =="2" :
            tp2+=1
        else:
            fp2+=1

    elif(p1==p2):print("it is equal")
    else:
        #print("class1")
        cnttemp1 +=1
        if real =="1" :
            tp1+=1
        else:
            fp1+=1





print("cnt1:",cnt1)  #real
print("cnt2:" ,cnt2) #real
print("cnttemp1:",cnttemp1)
print("cnttemp2" ,cnttemp2)

#print (cnttemp1 / cnt1)
#print(cnttemp2/ cnt2)
print(tp1)
print(fp1)

#print("precision is :",(tp1/(tp1+fp1)))

print("recall1 is :",(tp1/(tp1+tp2)))
print("recall2 is :",(tp2/(tp1+tp2)))
print("precision1 is :",(tp1/(tp1+fp1)))
print("precision2 is :",(tp2/(tp2+fp2)))





"""
print(precision_score(cnt1, cnttemp1, average="macro"))
print(recall_score(y_test, p1, average="macro"))"""

