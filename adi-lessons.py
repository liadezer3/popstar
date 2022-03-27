
# #################--שיעור יום שני 14/3/22 #########################################################
# input_1=input("Insert somthing...")
# input_2=input()
# input_3=input()
# ...

# # insert something...1

# # The procedure of repeating a certain functionor process is called literation (חזרה על פעולה מסוימת)
# # ישל נו שני סוגי לולאות
# # 1. לולאת while
# # 2. לולאת for

# # יכולים להיות שני מקרים בהם מתקיימת הלולאה תעבוד עד שעה מסוימת עד שהדואר ייסגר או עד שייגמר הדיו או עד  שיישבר לך החוד בעיפרון
# # אנחנו לא יודעיפ כמה זמן תימשך הלולאה אבל אנו יודעים מתי היא תיעצר

# # while loop
# # A while loop can be translated to : as long as.
# # we use while loop to iterate a certain amounth of commands as long as condition...

# # syntax 
# # in[]: while(cond):
# #     do something with

# # 1. while --> keyword
# # 2.(condition)--> As long as the condition
# # 3. colon (:)
# # 5. do something 

# # in[]: while(cond):
# # do something
# #     else: 
# #     do something with 

# # in[2]:num=0
# # while(num<10):## keyword,condition,colon
# #     print("Num:", num) ##ident, do something
# #     num=num+1
# #     print("End of while loop")

# # infinite loop = infinite                 

# # write a while loop, that reads 20 inputs from a user, and inserts the values into a list.

# while(x>20):
#     insert ("list")
#     x=x+1

#     # פיתרון :
#     num=0
#     while(num<20):
#         lst =[]
#         num =+ 1
#         lst.append(int(input('insert a number')))
#         print(len(lst))

#         num=0
# l=[]
# while num<20:
#     num+=1
#     l.append(int(input("please enter a number : ")))
# print(l)

# length=len(lst)
# i=0
# print("List",lst)
# print("Length of list:", length)
# print("iteration number:", i)

# while i<length:
#     print("Item:",lst[i])

# # for loops help us to repeat a grouop of statements a specified number of times
# # a for loop goes throuth items that are in sequence
# # a sequence can be anything  we can iterate on
# # collection/data structures

# # syntax:

# # for iterate_var in sequence: 
# #     do something 

# # 1.for ---> keyword 
# # iterate_var -->iteration
# # in(boolean condition)
# # sequence--> collection/ data structures

# for i in [0,1,2,3,4,5,6,7,8,9]:
#     print("i", i)
# for k in [0,1,2,3,4,5,6,7,8,9]:
#     print("k", k)

# # enumerate for
# # in[] for index, value in enumerate(values):
# # for index value in enumerate(values).

#     print(index,value)

# 0,2,4

# 0- 

import random
from tkinter import EXCEPTION
random=randrange(0-10)

#תיקון
num_to_guess = randrange(1,11)
trys = 0
print("welcome to guessing game")
guess = input("Guess a number(1-10):\n")
try ## int (guess)
    while guess != num_to_guess:
        if guess>0 or guess<11:
            trys+=1
    guess=input("Guess a number(1-10):\n")
try:
    guess=int(guess)
except ValueError as e:
    raise str(e)
else:
    guess=int(guess)
    except ValueError as e:'
    print("please insert a number between 1-11")
    raise str(e)
    print("congrats! you have won the game with {trys} attemots")

except ValueError as e:
    raise str(e)

num_to_guess = randrange(1,11)
trys = 1
print("Welcome to guessing game")
guess = input("Guess a number(1-10):\n")
try: ## Input validation
    guess = int(guess)
    while  guess != num_to_guess:
        if guess > 0 and guess < 11:
            trys +=1
            guess = input("Guess a number(1-10):\n")
            try:
                guess = int(guess)
            except ValueError as e:
                print("Please insert whole numbers only")
        else:
            guess = input("Please guess a number between 1-10 only:\n")
            try:
                guess = int(guess)
            except ValueError as e:
                print("Please insert whole numbers only")
    else:
        print(f"Congrats! You have won the game with {trys} attempts")
        
        
except ValueError as e:
    print("Please insert whole numbers only")

# שיעור עם עדי פייתון 16/3/22
# כתוב פונקציה שנקבלת אות אחת ומחזירה אמת אם פרמטר יחיד ומחזירה טרו אם ואר הוא םלואט ופולס בכל מקרה אחר
1==1.0
# => true
1 is 1.0
# =>False
1 is 1.0

###############################################
# write a function that recieved a sequence and returns the following:
# -minimum value in the sequence
# -maximum value in the sequence
# מדובר בסדרה מספרית. עם כמה מקומות.

def returns_min_and_max(seq)
    """
    This function recieved a sequence and returns:
    1.lowest value in seq
    2.highest value in seq
    This function returns values in tuple --> (min,max)
    """
    return min(seq), max(seq)
lst3=list('abcde')
lst3
out['a','b','c','d','e','f']

def retuens (min_and_max(lst3))
out('a','f')

lowest = 9999999999999
for item in seq:
    if item <lowest:
        lowest=items
return lowest

write a function that recived a string as an input:
-if the string is in lower - case letters returns the string in upper-case.
-if the string is in upper - case letters returns the string in lower - case.

1.built-in functions/methods
2.ascii

def switch_cases(string)
if string.lower()==string:
    ###ALL lower-case      
    return string.upper()
elif string.upper()==string.lower()
    return string.lower()

def switch_cases2(string)
if string.lower()==string:
    ###ALL lower-case      
    return string.upper():
elif string.isupper()==string.lower()
    return string.lower()

def switch_cases3(string)
lowerstr = 
upperstr = 
for letter in string:
  if ord(letter)>64 and ord(letter<91:
      lowerstr+=letter.lower()
      #lowerstr
    return string.upper():
elif string.isupper()==string.lower()
    return string.lower()

    # כל פעם ניקח ערך של תו ונתרגם אותו לערך אסקי ומשם לערך דצימלי המחשב יודע לתרגם אותו לבינארי. 
#     # https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg
# הפונקציה שלי שהופכת ערך דצימלי לערך של סטרינג ע"י שימוש בפונקציה של ord. פעולה הפוכה של chr מדצימלי חזרה לתו. אם הערך של 65 גדול מ-64 וגם קטן מ-91 אז אז אני אוסיף לטמפ

# לוקל סקופ וגלובל סקופזה על אותו עיקרון של מה מוכר לי ומה לא מוכר לי אם אני אהיה בתוך הסקופ הוא יוכל להכיר אותי אבל פונקציה מבחוץ לא תוכל להכיר אותי. לעומת זאת פונקציות מנחוץ תמיד יהיו מוכרות
# פרמטר לוקלי יוגדר כפרמטר בתוך הסוגריים בתוך הסקופ, הוא יכיר פרמטרים גלובליים מחוץ לסקופ. לעומת זאת פרמטר גלובלי לא יכיר את הפרמטר הלוקלי. 
/*
files
bit
bit represents set/unset in binary

set - 1
unset - 0

byte
A single byte consists of 8 bits
1
11110000
כל ביט עובר תהליך קידוד לבייט שנקרא encode
תהליך הפוך מבייט לסטרינג decode
כל תהליך של קריאת קוד כשאנו כותבים משהו אנו צריכים ח=לעבור תהליך דיקודינג וכשאנו קוראים אנו צריכים לעבור תהליך שנקרא אנקודינג
*/

in[]: type('a')
out[]:str
in[]:A
out[]:A
in[]:a
out[]:a
in[]:'a'.endode
out[]:b'a'
in[]:type('a'.encode())
out[]:b'a'
in[]:type('a'.encode())
out[]:bytes


######  PATH  #####
in[]: path ='C:/Users/user/greenpath/'
in[11]:print("Path:", path)
Path: 'C:\Users\user\greenpath'

path= 'C:\Users\user\greenpath\'
    print(path)
    path = ''C:\\Users\\user\\greenpath\\''

Working with files:

1. read files
if you wish to read a file you sould use this method:
    1.Mode 'r' : 'read'
    2. mode 'rb': 'read binary'

    2. write file
if you wish write a new file, you should use this method :
1. 
2. 

path = 'C:\\Users\\97250\\Pictures\\ControlCenter4\\OCR    '

reading from filles
to read file we should use read() method 
file = open(f"{path}actors.txt")## file opened and saved in file variable
text = file.read()
print(text)
James Bond
binary_file = open(f"{path}actors.txt", "rb") ##file opened any saved in file variable
text_in_bytes=bynary_file_read()
print(text_in_bytes)
b'James Bond', 'Johnney Depp', 'Angelina Julie'
text=text_in_bytes.decode
print(text)
James Bond
Johnney Depp
Angelina julie

files
writing files
we use writing mode, when we write a new file
when we write a file we overwride any existing file with the same name.

setting file in writing mode
path = 'C:\\Users\\97250\\Pictures\\ControlCenter4\\OCR    '

openinig a file in writing mode
file =  open=(path+'actors.txt','wb')

writing into a file
file.write(b'hello')

out[]:5

file.write(b'hello'.encode)
out[];8

closing a file
file.close

creating a new file in path that doesnt exist
path = 'C:\\Users\\97250\\Pictures\\ControlCenter4\\OCR'
file=open+(path+'actors.txt','wb')
try:
    file=open(path+'actors.txt','wb')

Dealing with a specific bytes
path = 'C:\\Users\\97250\\Pictures\\ControlCenter4\\OCR'
try:
    file=open(path+'actors.txt','rb')
expect fileNotFoundError as e:
    ##WRITE FAIL long  
    print(str(e))

first_byte = file.read(1)
h
print(second_byte)
e
print(third)
b'll

#classes
classname

##################################################

#####   שיעור עם עדי פייתון mySQL server ######
working with sql3
import sqlite3

setting up path:
path = "C:\\Users\\user\\Greenpath\\"
FileName = "Database.db"
FILE = PATH +FileName

Create Connection
det set_sql

select from database
def get users():
    """
    this functiom retrieves all users information from the database
    IN:
    OUT: Values from DB as dict
    Type:DICT
 
    """
    con = set sql_connection() #### creates connection
    cur = set_cursor(con) ##create cursor
    query = "select from users" ##SQL query
    data = v+cur.execute(query).fetchall() ##excecuting SQL QUERY
    dct = sort_as_dict(cur,data)
    sort_as_dict(cur,data)
    print(data)
    close_sql_connection(con) ##Closing connection
    return dct

    key:ID
    value:1
    key:USERNAME
    value:Admin
    key: email
    value : Admin@Admin.com
    key: notes
    valuees : administrator
    

get users()
    ID
    USERNAME
    Password
    email
    notes
    [(1), 'admin','admin@admin.com','Administrator'],(2,'adi','adi','adi@adi,+.com', ' ')

    sorting data from SQL table in a dict
    def sort_as_dict(cur,data):
        """
        This function recieved cur, data, where
        1. cur will be used to retrieve columns
        2.data will be used to retrieve values
        this function will return a list  of dictionary values.
        """
        
        ##List comprehension
        columns - [desc[0] for desc in cur.desrcription]
        result = []
        for row in data:
                row = dict(zip(column, row))
                result.append(row)

        return result

help(zip)

##is Exist???
### רק במקרים מסוימים אני אוכל ליצור דטא מסוג מסוים שחסרה לי כדי שלא תיווצר לי כפילות
# before inserting a new record to a DB we sometimes want to check if a certain value exists or not.
