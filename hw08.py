import csv
import sqlite3
#import os

conn = sqlite3.connect('hw08.db')
c = conn.cursor()


#os.remove("hw08.db")
#print("File Removed!")

# Drop IF EXISTS table
dropTableStatement1 = "DROP TABLE IF EXISTS project"
c.execute(dropTableStatement1)
dropTableStatement2 = "DROP TABLE IF EXISTS tasks"
c.execute(dropTableStatement2)
# Create table1
c.execute('''CREATE TABLE IF NOT EXISTS project
                (
                name text PRIMARY KEY, 
                description text, 
                deadline date
                )
        ''')
       
# Create table2
c.execute('''CREATE TABLE tasks
                (
                id number PRIMARY KEY, 
                priority integer, 
                details date,
                status text,
                deadline date,
                completed date,
                project text,
                FOREIGN KEY(project) REFERENCES project(name)
                )
        ''')
        
first = csv.reader(open('project.csv'))
for row1 in first:                                                          
        c.executemany("INSERT INTO project VALUES (?,?,?)", first)


second = csv.reader(open('tasks.csv'))
for row8 in second:                                                          
        c.executemany("INSERT INTO tasks VALUES (?,?,?,?,?,?,?)", second)

for row in c.execute("select t.status, t.deadline, p.name, p.description from project p join tasks t on p.name=t.project where t.status='done'"):
        print(row)
conn.commit()
c.close()
conn.close()