import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# -------------------------------
# MySQL Configuration
# -------------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''      # Put your MySQL password here if you have one
app.config['MYSQL_DB'] = 'employee_db'

mysql = MySQL(app)


# -------------------------------
# Home Page
# -------------------------------
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    cur.close()
    return render_template('index.html', employees=employees)


# -------------------------------
# Add Employee
# -------------------------------
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']

        cur = mysql.connection.cursor()
        cur.execute(
            """
            INSERT INTO employees (name, email, department)
            VALUES (%s, %s, %s)
            """,
            (name, email, department)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/')

    return render_template('add_employee.html')


# -------------------------------
# Delete Employee
# -------------------------------
@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect('/')


# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
