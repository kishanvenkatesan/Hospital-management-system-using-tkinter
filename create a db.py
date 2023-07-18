import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS appointments(
                    name text, 
                    age number, 
                    gender text,
                    phone number,
                    docname text,
                    docsp text,
                    time number
                )''')

cur.execute("INSERT INTO appointments VALUES (:name, :age, :gender, :phone, :docname, :docsp, :time)", {
                            'name': 'Arun',
                            'age': '19',
                            'gender': 'Male',
                            'phone': '12334568',
                            'docname': 'Ram',
                            'docsp': 'general',
                            'time' : '21-10 19:00'
            })

conn.commit()
conn.close()
