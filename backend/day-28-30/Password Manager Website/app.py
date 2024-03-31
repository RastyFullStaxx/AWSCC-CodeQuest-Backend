from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.template_folder = '.'

# Database connection
conn = sqlite3.connect(r'C:\Users\MSI\OneDrive\Desktop\Python\FInalProject\password.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY AUTOINCREMENT, website TEXT, email TEXT, password TEXT)''')
conn.commit()

@app.route('/')
def index():
    
    c.execute("SELECT * FROM passwords")
    passwords = c.fetchall()
    return render_template('index.html', passwords=passwords)

@app.route('/add_password', methods=['POST'])
def add_password():
    if request.method == 'POST':
        website = request.form['website']
        email = request.form['email']
        password = request.form['password']
        
        print(f"Received Data: Website={website}, Email={email}, Password={password}")
        
        try:
            c.execute("INSERT INTO passwords (website, email, password) VALUES (?, ?, ?)", (website, email, password))
            conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")
            conn.rollback()  
        return redirect(url_for('index'))
    
@app.route('/delete_password/<int:id>', methods=['POST'])
def delete_password(id):
    c.execute("DELETE FROM passwords WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/update_password/<int:id>', methods=['GET', 'POST'])
def update_password(id):
    if request.method == 'POST':
        website = request.form['website']
        email = request.form['email']
        password = request.form['password']
        c.execute("UPDATE passwords SET website=?, email=?, password=? WHERE id=?", (website, email, password, id))
        conn.commit()
        return redirect(url_for('index'))
    else:
        c.execute("SELECT * FROM passwords WHERE id=?", (id,))
        password = c.fetchone()
        return render_template('update.html', password=password)



if __name__ == '__main__':
    app.run(debug=True)
