import sqlite3 as sql
from flask import Flask, redirect,url_for, request, render_template

app=Flask(__name__,template_folder=r'C:\Users\manan\Desktop\Projects\Apartment Rental System', static_folder=r'C:\Users\manan\Desktop\Projects\Apartment Rental System')

con = sql.connect('login1.db', check_same_thread=False)
con.execute('CREATE TABLE IF NOT EXISTS tbl_l (ID INTEGER PRIMARY KEY AUTOINCREMENT,'
            + 'name TEXT, number TEXT, email TEXT, password TEXT, location TEXT)')

c =  con.cursor()
    
@app.route('/',methods=['POST',"GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        l_email = request.form['email']
        print(l_email)
        l_password = request.form['password']
        l_password = str(l_password)
        print(l_password)
       
        
        try:
            con = sql.connect('login.db')
            con.execute('CREATE TABLE IF NOT EXISTS tbl_l (ID INTEGER PRIMARY KEY AUTOINCREMENT,'
            + 'l_email TEXT, l_password TEXT)')
            c =  con.cursor() # cursor
            # insert data
            c.execute("INSERT INTO tbl_l (l_email, l_password) VALUES (?,?)",
                (l_email, l_password))
            con.commit() # apply changes

            if str(l_password) == "admin":
                return render_template('index.html')
            else:
                error = "Invalid Password, please try again"
                return render_template('login.html', error=error)
            
        except con.Error as err: # if error
            # then display the error in 'database_error.html' page
            return render_template('sign-up.html', error=err)
        finally:
            con.close() # close the connection
        
@app.route('/sign-up',methods=['POST',"GET"])
def signup():
    if request.method == 'GET':
        return render_template('sign-up.html')
    elif request.method == 'POST':
        name = request.form['name']
        print(name)
        number = request.form['number']
        print(number)
        email = request.form['email']
        print(email)
        password = request.form['password']
        print(password)
        location = request.form['location']
        print(location)
        insert = "INSERT INTO tbl_l (name, number, email, password, location) VALUES ('{}','{}','{}','{}','{}')".format(name, number, email, password, location)
        print(insert)
        c.execute(insert)
        con.commit() # apply changes
        return render_template('login.html')
        

app.run()