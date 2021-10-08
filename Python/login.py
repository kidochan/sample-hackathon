#!C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe
#C:\Users\user\AppData\Local\Programs\Python\Python39\Scripts
#import mysql.connect.connector
import pymysql
#import cgi and cgitb
import cgi, cgitb 

form = cgi.FieldStorage() 
#import the mysql
#import mysql.connector


mydb =pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="crofters"
)
mycursor = mydb.cursor()

#Get data from midterm.html
username = form.getvalue('username')
password = form.getvalue('password')
