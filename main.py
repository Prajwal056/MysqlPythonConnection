from secrets import choice
from tkinter import W
import mysql.connector as c # import the mysql connector
con = c.connect(host="localhost", user="root", password="root", database="studentdatabase") # connect to the database

print('*'*50)
print("Welcome to the Student Database")
print('*'*50)

cursor = con.cursor() # create a cursor
while True:
    choice= int(input("1-> Insert Book\n2-> Insert Student\n3-> insert Borrowing\n4-> Exit\n Your Choice: "))
    if choice == 1:
        book_name = input("Enter the book name: ")
        author = input("Enter the author name: ")
        isbn = input("Enter the isbn number: ")
        query = "INSERT INTO books (book_name, author_name, isbn_number) VALUES (%s, %s, %s)"
        values = (book_name, author, isbn)
        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()
        print("Book inserted successfully")
    elif choice == 2:
        name = input("Enter the name: ")
        roll = input("Enter the roll number: ")
        query = "INSERT INTO students (student_name, roll_number) VALUES (%s, %s)"
        values = (name, roll)
        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()
        print("Student inserted successfully")
    elif choice == 3:
        roll = input("Enter the roll number: ")
        book_name = input("Enter the book name: ")
        query = "INSERT INTO borrowings (roll_number, book_name) VALUES (%s, %s)"
        values = (roll, book_name)
        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()
        print("Borrowing inserted successfully")
    elif choice == 4:
        break
    else:
        print("Invalid choice") 
cursor.close()
con.close()
print("Connection closed")





  
