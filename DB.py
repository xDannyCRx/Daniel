import sqlite3
conn=sqlite3.connect('user.db')
c=conn.cursor()
c.execute('CREATE TABLE user(name text, age integer)')
c.execute('INSERT INTO user VALUES("user A" , 42)')
conn.commit()
c.execute('SELECT * FROM user')
print(c.fetchall())
conn.close()