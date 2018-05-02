#this file is calculating the probability of each class

with open(r'train1.txt') as f:
        words = [word for line in f for word in line.split()]
        first_num = len(words)
        #print("The total word count is:", first_num)


with open(r'train12.txt') as f:
        words = [word for line in f for word in line.split()]
        second_num = len(words)
        #print("The total word count is:", second_num)


def firstclassprob():
    c1prob = first_num/(first_num+second_num)
    return (c1prob)


def secondclassprob():
    c2prob = second_num/(first_num+second_num)
    return (c2prob)

#firstclassprob()
#secondclassprob()