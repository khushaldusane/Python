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


# Write a Python function that takes a string as input and counts the frequency of each character in the string. 
# The function should return a dictionary where the keys represent the characters and the values represent their corresponding frequencies.

dict1={}
a=input(f"Enter a string")
for i in a:
  dict1[i]=a.count(i)
print(dict1)


# Write a code that takes a sentence as input and returns the sentence with the order of words reversed. 
# Each word in the sentence should remain unchanged, but the order of the words should be reversed.

sentence=input(f"Enter the sentence")
words=sentence.split()
sent=[]
for i in words:
  sent.append(i)
sent.reverse()
print(sent)


# Write a code that takes a list as input and returns a new list with duplicate elements removed. 
# The order of the elements should be maintained in the new list.

num=[1,5,4,2,9,4,1,5,7,7,1,4,3,1]
newlist=[]
for i in num:
  if num.count(i)<2:
    newlist.append(i)
    newlist.sort()
print(newlist)

# Write a function called find_missing_number that takes a list of integers from 1 to N (inclusive), 
# with one number missing, and returns the missing number. For example, if the input list is [1, 2, 3, 5], 
# the missing number is 4, so the function should return 4.

def find_missing_number(list_):
  missing_num=[]
  max_num=max(list_)
  for i in range(max_num+1):
    if i not in list_:
      missing_num.append(i)
  return missing_num    

print(find_missing_number(list_))
list_=[1,5,4,7,2,4,3,2,6,0]


# Write a function called common_elements that takes two lists as input and returns a new list containing 
# the common elements between the two input lists


def common_elements(l1,l2):
  common_ele=[]
  for i in l1:
    for j in l2:
      if i==j:
        common_ele.append(i)
  return(common_ele)

l1=[1,2,3,4,8]
l2=[3,5,6,8]  
common_ele_list=common_elements(l1,l2)
print(common_ele_list)


# Write a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string

def count_vowels(user_input):
  vowels_list=[]
  vowels=['a','e','i','o','u']

  for i in user_input:
    if i in vowels:
      vowels_list.append(i)
  total=len(vowels_list)
  return total


user_input=input(f"Enter the sentence: ")
print(count_vowels(user_input))


# Write a Python function that takes a list of integers as input and returns a 
# new list that contains only the even numbers from the input list.

def even_numbers(nums):
  even_num=[]
  for i in num:
    if i%2==0:
      even_num.append(i)
  return even_num

num=[1,2,3,4,5,6,8,4,12,14,15]
print(even_numbers(num))


# Write a Python function that takes a string as input and returns the number of words in the string. 
# Assume that words in the string are separated by spaces.

def count_words(text):
  words=text.split()
  return len(words)

text="My name is Khushal"
print(count_words(text))

# Write a Python function that takes a list of strings as input and 
# returns a new list containing the lengths of the strings in the input list.

def string_length(string):
  string_len=[]
  for i in string:
    string_len.append(len(i))
  return string_len


string=["Hello","How","are","you"]
print(string_length(string))


# Write a Python function that takes a list of integers as input and 
# returns a new list containing only the odd numbers from the input list.

def odd_numbers(num):
  odd_nums=[]
  for i in num:
    if i%2>0:
      odd_nums.append(i)
  return odd_nums

num=[1,5,4,7,6,2,45,95,74]
print(odd_numbers(num))


# Write a Python function called average_grade that takes a list of grades (integers) as input and returns the average grade. 
# The average should be calculated as the sum of all grades divided by the total number of grades

def average_grade(grades):
  average=[]
  sum=0
  for i in grades:
    sum+=i
  avg=(sum/len(grades))
  average.append(avg)
  return average
 
grades=[80, 90, 75, 85, 95]
print(average_grade(grades))


#  Write a Python function called find_max that takes a list of numbers as input and returns the maximum number from that list.

def find_max(nums):
  max_num=max(nums)
  return max_num

nums=[1,51,44,84,54,62,0]  
print(find_max(nums))

# Write a Python function to check if a given string is a palindrome.
# Implement the function is_palindrome(s) that takes a string s as input and returns True if s is a palindrome, and False otherwise

def is_palindrome(text):
    if i==i[::-1]:
      return True
    else:
      return False



text=['Hello','How','are','you','radar']
for i in text:
  print(is_palindrome(i))


# Python Program to Check if a Number is Odd or Even.

def even_odd(list1):
  result=[]
  for i in list1:
    if i%2==0:
      result.append((i,"Even"))
    else:
      result.append((i,"Odd"))
  return result

list1=[12,54,95,20,37]
print(even_odd(list1))

# Write python program to find the area of a triangle when 3 side of trianle given.

import numpy as np
def triangle_area():
  a=int(input("length of side a: "))
  b=int(input("length of side b: "))
  c=int(input("length of side c: "))
  s=((a+b+c)/2)
  Area=round(np.sqrt(s*(s-a)*(s-b)*(s-c)),2)
  return Area

print(triangle_area())


# Write python Program to Check Leap Year

def leap_year(year):
  if year%4==0 and year%100!=0:
    return "It is leap year"
  else:
    return "It is not a leap year"

year=int(input("Enter the year to check if it is leap year or not : "))
print(leap_year(year))
