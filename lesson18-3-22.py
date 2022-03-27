##################################################
#####   שיעור עם עדי פייתון mySQL server ######

# working with sql3
# import sqlite3

# # setting up path:
# path = "C:\\Users\\user\\Greenpath\\"
# FileName = "Database.db"
# FILE = path +FileName

# # Create Connection
# det set_sql

# select from database
def get_users():
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
    

# get users()
#     ID
#     USERNAME
#     Password
#     email
#     notes
#     [(1), 'admin','admin@admin.com','Administrator'],(2,'adi','adi','adi@adi,+.com', ' ')

#     sorting data from SQL table in a dict
#     def sort_as_dict(cur,data):
#         """
#         This function recieved cur, data, where
#         1. cur will be used to retrieve columns
#         2.data will be used to retrieve values
#         this function will return a list  of dictionary values.
#         """
        
#         ##List comprehension
#         columns - [desc[0] for desc in cur.desrcription]
#         result = []
#         for row in data:
#                 row = dict(zip(column, row))
#                 result.append(row)

#         return result

# help(zip)

##is Exist???
### רק במקרים מסוימים אני אוכל ליצור דטא מסוג מסוים שחסרה לי כדי שלא תיווצר לי כפילות
# before inserting a new record to a DB we sometimes want to check if a certain value exists or not.

# get_users()
# [username:"liad_ezer",age:"28",birthdate:"7.11.93",living-city:"maale-adumim",sex:"male",password:"1234567"][0-5,-1]