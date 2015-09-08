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
print "<h2>Hello %s %s<h2/>" %(f_name, l_name)

print "<HTML>"
print "<center>"
#embed youtube video in html page
print "<iframe width=420 height=315 src=http://www.youtube.com/embed/ye5BuYf8q4o?autoplay=1>"
print "</iframe>"


print "<br/>"
print "<br/>"

#email me link
print "<a href=mailto:harout.ter-papyan.41@my.csun.edu>Email Me</a>"

print "<br/>"
print "<br/>"

#google search form
print "<form method=get action=https://www.google.com/search>"
print "<label> Search Google: <input type=text name=q></label>"
print "<input type=submit value=Submit>"

print "</center>"
print "</HTML>"
