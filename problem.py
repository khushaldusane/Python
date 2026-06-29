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
