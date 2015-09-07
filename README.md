# Simple.cgi

SUMMARY

HTML Page (simple.html) with a button and input fields for first and last name. After entering values into the fields and clicking "submit", the (python)cgi script (simple.cgi) will take the input, create another simple html page that includes a greeting with the name entered in simple.html, the directory path to the cgi script, and a youtube video.

Initial Commit 9/6 to open Repo

Commit 9/6 with instructer example and simple html page

Commit 9/6 renamed my files to simple.cgi and simple.html
            added a form in html page
            
Commit 9/6 - used a perl cgi script to return state capitals based on hyperlink pressed in the html page

Commit 9/7 - ditched perl, switched to python. HTML page contains a button. When pressed, the cgi script generates an html page with the file path of the script and a youtube video.

Commit 9/7 - added name fields to html page, which are passed to the cgi script and printed in an html page generated by the cgi script. 

Commit 9/7 - added simpleSteve.html that points to http://www.csun.edu/~steve/cgi-bin/simple.cgi?simple.cgi

INSTRUCTIONS

simple.cgi should be placed in /cgi-bin/

simple.html should be modified to point to /~steve/ instead of /~ht250268/

The submit button First/Last name fields

<code>form action = "http://www.csun.edu/~ht250268/cgi-bin/simple.cgi" method = "get"</code>


OR

simpleSteve.html should be used as it is already pointing to /~steve/


Open the simple.html (or simpleSteve.html). 
Enter your first and last name
Click "Submit"

The simple.cgi script will generate a new html page with the path to the simple.cgi file, your name, and a youtube video that will auto play. 


Resource used to use get method to pass first and last name to cgi script: http://www.tutorialspoint.com/python/python_cgi_programming.htm
