

import sqlite3

#Connecting to database
conn = sqlite3.connect('dbSubmission.db')

#Creating a table if it dosent exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_items(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_items TEXT)")
    conn.commit()

# Tuple of items to process
items_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#Print items that end with '.txt'
for x in items_tuple:
    if x.endswith('txt'):
        print(x)


#Close
conn.close()

