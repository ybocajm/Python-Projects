
"""
oneTuple = ('one',)
multiTuple = ('two', 'three', 'four')

result = oneTuple + multiTuple
print(result)
"""

"""
In Python, we can add specific elements from a
multiple-element tuple to a database. 

assignment:
Your database will require 2 fields: an auto-increment primary integer
field and a field with the data type "string".

Your script will need to read from the supplied list of file names at the
bottom of this page and determine only the files from the list which end
with a “.txt” file extension.

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
            
Next, your script should add those file names from the list ending
with “.txt” file extension within your database.

your script should legibly print the qualifying text files to the console.
"""

import sqlite3
conn = sqlite3.connect("files.db")
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_a185(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filename TEXT)")
    conn.commit()

conn = sqlite3.connect('files.db')

# files list
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

"""
To add the names to test.db, we create a for loop that analyzes the
tuple of names and finds only those that end with “.txt”, and then splits
the names we want into one-element list.
"""

# loop through names that end in e
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the list therefore (x,)
        # will denote a one element list for each name ending with e.
            cur.execute("INSERT INTO tbl_a185 (col_filename) VALUES (?)", (x,))
            print(x)
conn.close()

