#!/usr/local/bin/python3
import mysql.connector

''' Jason Cheung
Final Project
Class: AS.410.712.81.SU22 Advanced Practical Computer Concepts for Bioinformatics
Due Date: 8/15/22
Description: A script to create a table in MySQL
'''

# connecting to MySQL
conn = mysql.connector.connect(user = 'jcheung9', password = 'password', host = 'localhost', database = 'jcheung9')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE 1USU (
atom varchar(25),
atom_number int,
atom_type varchar(25),
residue varchar(25),
chain varchar(25),
residue_number int,
x_coord decimal(10,3),
y_coord decimal(10,3),
z_coord decimal(10,3),
occupancy double,
beta_factor decimal(10,2),
element varchar(25))
''')

conn.commit()
cursor.close()
conn.close()
