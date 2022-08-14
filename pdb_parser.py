#!/usr/local/bin/python3
import pandas as pd
import mysql.connector
import argparse
import os


''' Jason Cheung
Final Project
Class: AS.410.712.81.SU22 Advanced Practical Computer Concepts for Bioinformatics
Due Date: 8/15/22
Description: A script to parse a pdb file and import it into MySQL database
'''

list = []

parser = argparse.ArgumentParser

parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to an input file to be read' )
args = parser.parse_args()

# to collect the coordinates of the 3D structure
for line in open(args.input_file):
    if not line.startswith(('ATOM', 'HETATM', 'TER')):
        continue
    cols = line.split()
    list.append(cols)

# can easily export data to MySQL if in dataframe format
df = pd.DataFrame(list)
df.columns = ['atom', 'atom_number', 'atom_type', 'residue', 'chain', 'residue_number', 'x_coord', 'y_coord', 'z_coord', 'occupancy', 'beta_factor', 'element']


# connecting to MySQL
conn = mysql.connector.connect(user = 'jcheung9', password = 'password', host = 'localhost', database = 'jcheung9')

cursor = conn.cursor()

# to iterate to export data to MySQL
for i, row in df.iterrows():
    sql = "INSERT INTO pdb VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    conn.commit()

cursor.close()
conn.close()
