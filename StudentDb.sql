DROP database IF EXISTS StudentDatabase;
create database StudentDatabase; 
use StudentDatabase; 

DROP TABLE IF EXISTS books;

create table books (
    book_name varchar(20),
    author_name varchar(20),
    isbn_number int(11)
    );

DROP TABLE IF EXISTS students;

create table students (
    student_name varchar(20), 
    roll_number int,
    primary key(roll_number)
    );
    
DROP TABLE IF EXISTS borrowings;

create table borrowings (
    roll_number varchar(20), 
    book_name varchar(20),
    primary key (roll_number, book_name)
    );