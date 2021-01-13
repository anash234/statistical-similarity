'''
This program takes any two sets of data input by the user and:
1) outputs a mean and standard deviation for each set
2) outputs an overall weighted mean and standard deviation
3) compares the groups to assess whether they are statistically similar
'''

#The first section prompts the user for input for both sets and stores the integer input in lists
set1 = []
set2 = []
inp = input('Would you like to enter data for set 1 or set 2? ')
while inp != '1' and inp != 'set 1' and inp != '2' and inp != 'set 2':
    inp = input('Would you like to enter data for set 1 or set 2? ')
if str.lower(inp) == '1' or 'set 1':
    n = ''
    while n != 'done':
        n = input('Enter one value at a time. When you are done, enter done. ')
        if n != 'done':
            set1.append(int(n))
    n = ''
    while n != 'done':
        n = input('Now enter data for set 2. Enter one value at a time. When you are done, enter done. ')
        if n != 'done':
            set2.append(int(n))
elif str.lower(inp) == '2' or 'set 2':
    n = ''
    while n != 'done':
        n = input('Enter one value at a time. When you are done, enter done. ')
        if n != 'done':
            set2.append(int(n))
    n = ''
    while n != 'done':
        n = input('Now enter data for set 1. Enter one value at a time. When you are done, enter done. ')
        if n != 'done':
            set1.append(int(n))

#The second section defines functions for mean and standard deviation
#A mean is defined as sumx/n
#A standard deviation is defined as sqrt((sumx^2 - (sumx)^2/n)/(n -1))
import math

def mean(x):
    sumx = 0
    n = 0
    for i in x:
        sumx += i
        n += 1
    return sumx / n

def S(x):
    sumx = 0
    sumxsqr = 0
    n = 0
    for i in x:
        sumx += i
        sumxsqr += i ** 2
        n += 1
    return math.sqrt((sumxsqr - (sumx ** 2) / n) / (n - 1))

#The third section calculates a weighted mean and standard deviation across both sets
#A weighted mean can incorporate data from sets of different sizes
#It is calculated as (x1*n1 + x2*n2)/(n1 + n2) where x1 and x2 are the means of each group
#It can also be calculated as (sumx1 + sumx2)/(n1 + n2)
def weightedMean(x, y):
    sum = 0
    n = 0
    for i in x:
        sum += i
        n += 1
    for i in y:
        sum += i
        n += 1
    return sum / n

def weightedS(x, y):
    sum = 0
    sumsqr = 0
    n = 0
    for i in x:
        sum += i
        sumsqr += i ** 2
        n += 1
    for i in y:
        sum += i
        sumsqr += i ** 2
        n += 1
    return math.sqrt((sumsqr - (sum ** 2) / n) / (n - 1))

#The fourth section finds the range within which the central 95% of each set falls
#Calculated as x +- 2S where x is the set mean
#The section also defines a function to compare whether two sets are statistically similar
#If the central 95% ranges overlap, the sets are considered similar
#The comparison is imperfect because it rounds the upper and lower bounds of each range to the nearest integer
central1 = []
mean1 = mean(set1)
S1 = S(set1)
central1.append(mean1 - 2 * S1)
central1.append(mean1 + 2 * S1)

central2 = []
mean2 = mean(set2)
S2 = S(set2)
central2.append(mean1 - 2 * S2)
central2.append(mean1 + 2 * S2)

def compare(a, b):
    for i in range(int(a[0]), int(a[1])):
        for j in range(int(b[0]), int(b[1])):
            if i == j:
                return True
            else:
                return False

#The final section assesses the sets and prints the following results:
#1) The mean and standard deviation for each set
#2) The overall weighted mean and standard deviation
#3) A statement of whether or not the groups are similar
print('The mean of set 1 is {0} and its standard deviation is {1}.'.format(mean(set1), S(set1)))
print('The mean of set 2 is {0} and its standard deviation is {1}.'.format(mean(set2), S(set2)))
print('The total weighted mean is {0} and total standard deviation is {1}.'.format(weightedMean(set1, set2), weightedS(set1, set2)))
print()
if compare(central1, central2) == True:
    print('The two groups are statistically similar.')
elif compare(central1, central2) == False:
    print('The two groups are not statistically similar.')