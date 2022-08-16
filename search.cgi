#!/usr/local/bin/python3

import jinja2
import mysql.connector
import cgi


def main():

	# jinja2 html templating
	templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

	env = jinja2.Environment(loader=templateLoader)
	template = env.get_template('final.html')
	
	form = cgi.FieldStorage()
	searchTerm = form.getvalue('search_residue')
	searchTerm2 = form.getvalue('search_atom_type')
	searchTerm3 = form.getvalue('search_p_id')
	
	# connecting to MySQL
	conn = mysql.connector.connect(user = 'jcheung9', password = 'password', host = 'localhost', database = 'jcheung9')

	# code to pass to template
	results = list()
	
	qry = """
	SELECT atom, atom_number, atom_type, residue, chain, residue_number, x_coord, y_coord, z_coord, occupancy, beta_factor, element, protein_id
	FROM pdb
	WHERE protein_id LIKE %s
	AND (residue LIKE %s OR atom_type LIKE %s);
	"""

	params = (searchTerm3, searchTerm, searchTerm2)
	cursor = conn.cursor()
	cursor.execute(qry, params)
	
	results = cursor.fetchall()

	print("Content-Type: text/html\n\n ")
	print(template.render(results = results,))

	cursor.close()
	conn.close()

if __name__ == '__main__':
	main()

