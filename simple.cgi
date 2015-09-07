#!/usr/bin/python
#Harout Ter-Papyan
#Comp 490
#Primer Project
import cgi
import os
import cgitb

form = cgi.FieldStorage()

#get data and assign to var
f_name = form.getvalue('first_name')
l_name = form.getvalue('last_name')

print "Content-type: text/html"
print
print "<br/>"

#print file path
print ("File Path:")
print (os.getcwd())

print "<br/>"

#print name
print "<h2>Hello %s %s<h2/>" %(f_name. l_name)

print "<HTML>"

#embed youtube video in html page
print "<iframe width=420 height=315 src=http://www.youtube.com/embed/ye5BuYf8q4o?autoplay=1>"
print "</iframe>"

print "</HTML>"