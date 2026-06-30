## Two Sums
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

nums=[2,7,11,15]
target=9
sum=0
for i in nums:
  for j in nums:
    if i!=j and i+j==target:
      print([nums.index(i) , nums.index(j)])

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

import numpy as np
nums1=[1,3]
nums2=[2]
arr=nums1+nums2
median=np.median(arr)
print(median)

# Given an integer x, return true if x is a palindrome, and false otherwise.

x=(input("Enter a number to check palindrome or not "))
if str(x)==str(x[::-1]):
  print("True")
else:
  print("False")

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

l1=[1,1,2,3,4]
l2=[2,5,6,7,9]
m=l1+l2
m.sort()
print(m)

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8  , Then the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n=int(input("Enter a number "))
d={}
for i in range(1,n+1):
  d[i]=i*i
print(d)

# Write a Python function that takes a list of numbers as input and 
# returns a new list containing only the even numbers from the original list.

l1=[]
l2=[]
n=int(input("How many numbers you want to enter in list ?"))
for i in range(n):
  num=int(input(f"Enter the numbers to put in lists {i+1} :"))
  l1.append(num)
for j in l1:
  if j%2==0:
    l2.append(j)
print(l2)

n=int(input("Enter a number "))
d={}
for i in range(1,n+1):
  d[i]=i*i
print(d)

# Write a Python function that takes a list of strings as input and returns a new list 
# containing only the strings that have a length greater than a given value.

l1=[]
l2=[]
length=4
n=int(input("How many strings you want to enter in list ?"))
for i in range(n):
  str=input(f"Enter the strings to put in lists {i+1} :")
  l1.append(str)
for j in l1:
  if len(j)>length:
    l2.append(j)
print(l2)


