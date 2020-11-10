#!/usr/bin/python
import cgi, cgitb
import MySQLdb

db=MySQLdb.connect("localhost",'root','redhat','eventdb');

cursor=db.cursor();

form=cgi.FieldStorage();

name=form.getvalue('name');
password=form.getvalue('pass');
email=form.getvalue('email');
address=form.getvalue('address');
phone=form.getvalue('number');
city=form.getvalue('city');
date=form.getvalue('date');
venue=form.getvalue('venue');
zipcode=form.getvalue('Zip');

print "Content-type:text/html \n";
try:
	cursor.execute("insert into udetails (Name,Password,Email,Address,PNumber,City,Booking_date,Venue,Zip) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"  %(name,password,email,address,phone,city,date,venue,zipcode));
	print "<html><head><title>result</title></head>";
	print "<script> alert('Booking Ticket successfully generated. Please pay respective booking amount and collect your ticket. Thank You!!'); location.href='/Manage_Events/index3.html'; </script>";
	print "</html>";
	db.commit();
	db.close();

except:
	print "<html><head><title>result</title></head>";
	print "<script> alert('Booking Failed'); location.href='/Manage_Events/booking_step1.html'; </script>";
	print "</html>"	
	db.close();



