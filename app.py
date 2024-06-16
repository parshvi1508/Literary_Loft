from flask import Flask, render_template, request, redirect, url_for
from db_details import get_db_connection

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/books')
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    print(books) 
    return render_template('books.html', books=books)

@app.route('/users')
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    print(users)  
    return render_template('users.html', users=users)



@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year_published = request.form['year_published']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, author, genre, year_published) VALUES (%s, %s, %s, %s);",(title, author, genre, year_published))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('get_books'))

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password_hash = request.form['password']  # Correct the name here
        email = request.form['email']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s);", (username, password_hash, email))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('get_users'))




    
if __name__ == '__main__':
    app.run(debug=True)
