#!/usr/bin/python

import cgi, cgitb
import MySQLdb

db = MySQLdb.connect("localhost",'root','750925','eventdb');
cursor = db.cursor();

form = cgi.FieldStorage();

name  = form.getvalue('name');
password = form.getvalue('pass');
print "Content-type:text/html \n";

try:
	cursor.execute("select * from udetails where Name='%s' and Password='%s'" %(name,password));
	x = cursor.fetchall();
	for  result  in x:
		print "<html><head><title>result</title>";
		print "<body bgcolor='gray' text='orange'>";
		print "<h1> NAME	:  %s </h1>" %result[1];
		print "<h1> PHONE	:  %s </h1>" %result[5];
		print "<h1> ADDRESS	:  %s </h1>" %result[4];
		print "<h1> CITY	:  %s </h1>" %result[6];
		print "<h1> VENUE	:  %s </h1>" %result[8];
		print "<h1> DATE	:  %s </h1>" %result[7];
		print "<hr><hr></body></html>"
	db.close();

except:
	print "<html><head><title>result</title></head>";
	print "<script> alert('Invalid User'); location.href='/events/login.html'; </script>";
	print "</html>"	
	db.close();









