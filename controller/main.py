
import pymysql
from model.tableUser import Results as Results_User
from model.tableAnimal import Results as Results_Animal
from model.tableDonator import Results as Results_Donator
from app import app
from model.db_config import mysql
from flask import flash, render_template, request, redirect
from werkzeug.security import *


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/teste")
def index():
    return render_template('users.html')


@app.route('/new_user')
def add_user_view():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _password and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)

            # save edits
            sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
            data = (_name, _email, _hashed_password,)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User added successfully!')
            # return redirect('/')
            return render_template('users.html')
        else:
            return 'Error while adding user'
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/users')
def users():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user")
        rows = cursor.fetchall()
        table = Results_User(rows)
        table.border = True
        return render_template('users.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit/<int:id>')
def edit_view(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _id = request.form['id']
        # validate the received values
        if _name and _email and _password and _id and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            print(_hashed_password)
            # save edits
            sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (_name, _email, _hashed_password, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>')
def delete_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
        conn.commit()
        flash('User deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Animal functions above:

@app.route('/new_animal')
def add_animal_view():
    return render_template('add_animal.html')


@app.route('/add_animal', methods=['POST'])
def add_animal():
    conn = None
    cursor = None
    try:
        _animalname = request.form['inputAnimalName']
        _rescdate = request.form['inputRescueDate']
        _gender = request.form['inputGender']
        # validate the received values
        if _animalname and _rescdate and _gender and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_animal(animal_name, animal_rescue_date, animal_gender) VALUES(%s, %s, %s)"
            data = (_animalname, _rescdate, _gender,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Animal added successfully!')
            return render_template('animals.html')
        else:
            return 'Error while adding Animal'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/animals')
def animals():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_animal")
        rows = cursor.fetchall()
        table = Results_Animal(rows)
        table.border = True
        return render_template('animals.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit_animal/<int:id>')
def edit_animal_view(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_animal WHERE animal_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit_animal.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_animals():
    conn = None
    cursor = None
    try:
        _name = request.form['inputAnimalName']
        _rescdate = request.form['inputRescueDate']
        _gender = request.form['inputGender']
        _id = request.form['animalid']
        # validate the received values
        if _name and _rescdate and _gender and _id and request.method == 'POST':
            # save edits
            sql = "UPDATE tbl_animal SET animal_name=%s, animal_rescue_date=%s, animal_gender=%s WHERE animal_id=%s"
            data = (_name, _rescdate, _gender, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Animal updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating Animal'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_animal/<int:id>')
def delete_animal(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_animal WHERE animal_id=%s", (id,))
        conn.commit()
        flash('Animal deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#Donators below

@app.route('/new_donator')
def add_donator_view():
    return render_template('add_donator.html')


@app.route('/add_donator', methods=['POST'])
def add_donator():
    conn = None
    cursor = None
    try:
        _donatorname = request.form['inputDonatorName']
        _donatordocument = request.form['inputDonatorDocument']
        _donatoremail = request.form['inputDonatorEmail']
        # validate the received values
        if _donatorname and _donatordocument and _donatoremail and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_donator(donator_name, donator_document, donator_email) VALUES(%s, %s, %s)"
            data = (_donatorname, _donatordocument, _donatoremail,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Donator added successfully!')
            return render_template('donators.html')
        else:
            return 'Error while adding Donator'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/donators')
def donators():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_donator")
        rows = cursor.fetchall()
        table = Results_Donator(rows)
        table.border = True
        return render_template('donators.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run()
