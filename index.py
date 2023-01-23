#!C:\Users\LAVANYA\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb

cgitb.enable()

a=cgi.FieldStorage()




print ("Content-type:text/html\n")

print("<html>")

print("<frameset rows='30%,*'>")

print("<frame src='new.py'>")

print("<frame name='f3'>")

print("</frameset>")

print("</html>")
