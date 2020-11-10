#!/usr/bin/python

import cgi, cgitb


form = cgi.FieldStorage();

city = form.getvalue('city');
date = form.getvalue('date');
print "Content-type:text/html \n";

try:
	result = cursor.fetchone(city);

	if result[0]==city:
		print "<html><head><title>result</title></head>";
		print "<script> location.href='/events/search-result.html'; </script>";
		print "</html>"
	elif result[0]==city:
		print "<html><head><title>result</title></head>";
		print "<script> location.href='/events/search-indore.html'; </script>";
		print "</html>"
	elif result[0]==city:
		print "<html><head><title>result</title></head>";
		print "<script> location.href='/events/search-delhi.html'; </script>";
		print "</html>"
	elif result[0]==city:
		print "<html><head><title>result</title></head>";
		print "<script> location.href='/events/search-mumbai.html'; </script>";
		print "</html>"
		
except:
	print "<html><head><title>result</title></head>";
	print "<script> alert('City not in range'); location.href='/Manage_Events/index3.html'; </script>";
	print "</html>"	
	









