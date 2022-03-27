# # # def salary():
# # #     hoursRPH=input("Please enter your working hours:")
# # #     inputRPH=input("Please enter your rate per hour:")
# # #     ratePerHour=int (inputRPH)
# # #     hours=int (hoursRPH)
# # #     print("Your work payment is:",ratePerHour * hours)

# # # salary()

# # # def ageAndName():
# # #     name=input("Please type your name:")
# # #     age=input("Please type your age:")
# # #     print(name +  " " + age)
# # #     print(type(name))
# # #     print(type(age))
# # #     age=int(age)
# # #     print(age,type(age))
# # #     age=float(age)
# # #     print(age,type(age))
# # #     over18=age>=18
# # #     print("Is age legal? ",over18)

# # # ageAndName()    

# # # 4.	Write a program that asks the user for a sentence.
# # # -	Print out the length of the sentence (Using len()).
# # # -	Print out how many words are in the sentence. (teach yourself the split method – no loops! Remember the help of ‘dir’ function)
# # # -	Print out the sentence in lower-case letters.
# # # -	Print out the sentence in upper-case letters.

# # # sentence=input("today is a day")
# # # print(len(sentence))
# # # numOfWords=len(sentence.split())
# # # print(numOfWords)
# # #print.sentence.lower()    
# # # print.sentence.upper()    

# # #Python3 code to demonstrate
# # #to count words in string
# # # using split()

# # # # initializing string
# # # test_string = "Geeksforgeeks is best Computer Science Portal"

# # # # printing original string
# # # print ("The original string is : " + test_string)

# # # # using split()
# # # # to count words in string
# # # res = len(test_string.split())

# # # # printing result
# # # print ("The number of words in string are : " + str(res))

# # # test_string = "Tutorials point is a learning platform"
# # # #original string
# # # print ("The original string is : " + test_string)
# # # # using split() function
# # # res = len(test_string.split())
# # # # total no of words
# # # print ("The number of words in string are : " + str(res))

# # # print('sentence'.upper())
# # # print('sentence'.lower())
# # # len('sentence'.split())

# # #5.	Write a program that asks the user for 3 different sentences. 
# # # -	Print each sentence in reverse.
# # # -	Print all of the sentences concatenated.
# # # -	Print all of the sentences concatenated in reverse.

# # # #sentences
# # # # 1.today we are celebrating hanucka holiday.
# # # # 2. I need to do homework to stay in business.
# # # # 3. when you're confused pinky up

# # str1=input["Today we are celebrating hanucka holiday."][0:41:-1]
# # str2=input["I need to do homework to stay in business"][0:41:-1]
# # str3=input["When you're confused pinky up"][0:29:-1]
# # str1[len][0:41:-1]
# # str2[len][0:41:-1]
# # str3[len][0:29:-1]

# # sentence1=input("Please enter a sentence")
# # sentence2=input("Please enter a sentence")
# # sentence3=input("Please enter a sentence")
# # lenthOfSentence1=len(sentence1)
# # lenthOfSentence2=len(sentence2)
# # lenthOfSentence3=len(sentence3)
# # print(len(sentence1)+len(sentence2)+len(sentence3))

# # print(sentence1sentence2sentence3)
# # print(sentence1sentence2sentence3[::-1])

# #6 ######################################  #6
# # Three sides of the triangle is a, b and c:  
# from ast import keyword
# from asyncore import loop
# from base64 import decode
# from doctest import OutputChecker
# from importlib.metadata import files
# from msvcrt import LK_LOCK
# from re import A
# from socket import close
# import sqlite3
# from turtle import mode
# from unittest import result
# from uu import encode

# # from argon2 import PasswordHasher


# a = float(input('Enter first side: '))  
# b = float(input('Enter second side: '))  
# c = float(input('Enter third side: '))  
  
# # calculate the semi-perimeter  
# area1 = (a + b + c) / 2  
  
# # calculate triangle area  
# area1 = (area1*(area1-a)*(area1-b)*(area1-c)) ** 0.5  
# print('The area of the triangle is :' ,area1) 

# #calculating rectangle area
# #two length of the rectangle and height
# a = float(input('Enter first side : '))
# h = float(input('Enter height : '))
# area2 = (a * h)
# print('the area of the rectangle is :',area2)

# #calculating square area of square
# #one side a
# a = float(input('Enter the side of the square : '))
# area3 = a * a
# print('the area of the square is :' ,area3) 

# #calculating paralellogram (מקבילית)
# a = float(input('Enter long side : '))
# h = float(input('Enter height : '))
# area4=float('The area of the rectangle is :' ,h*a)

# ## /question 1
# name = input('what is your name?\n')
# print("Hello, name")

#answer
# what is your name?
# Adi
# Hello, Adi

# question 4
sen = input("insert any sentence:\n")
# insert any sentence :
# hello class good morning
print("Sentence:", sen)
print("Length:", len(sen))

# sentence: Hello class good morning
length:24
print("total words:",len(sen.split(' ')))
# total words:4
print("sentence in lower-case:", sen.lower())

# sentence in lower-case: 4
print("sentence in lower-case:", sen.upper())

empty_lst = []
print("List:", empty_lst)
print("Type:",type(empty_lst))
print("Length:",type(empty_lst))

List:[]
Type:#class "list"
length:10

lst_of_str = [a,b,c,d,e,f,g,h,i,j]
ty[e class list]
length:10

list = [7.0, 0.5,5.0]
type: #class# 'list'
length:3

###index
lst_of_mix = [5,'Hey', 7.5, 5**3, True, False]
print("List, lst_of_mix:",lst_of_mix)
print("type",type lst_of_mix)
print("Length",len(lst_of_mix))

list[5,'Hey',7.5,125,true,true]
print("list:")

a = 50
b = 50.0
c = 'abcdefg'
d = True

list(c)
['a','b','c','d','e','f','g']


# how to check if a value is  inside a list
# the in operator vcheck if an object is inside another object and returns true

lst=['fiodor', 'liad', 'Yohay', 'irit', 'michael']
in lst= 'fiodor'

list.append("Tal")
# דוחף את הערך לסוף הרשימה

list.remove()
#מוחק ערך מהרשימה

list.pop()
#מוחק ערך מהרשימה לפי אינדקס
# לפי המיקום בליסט

lst=[1,2,3,4,5]
print('List:', lst )
print('Type:', lst )
print('Length:', lst )

l+print