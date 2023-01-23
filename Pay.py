#!C:\Users\LAVANYA\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb

cgitb.enable()

form=cgi.FieldStorage()

if form.getvalue("name"):
      name = form.getvalue("name")



print ("Content-type:text/html\n")

print("<html>")

print("<head>")

print("<title> Hey </title>")

print("</head>")



print("<body>")

if form.getvalue("Submit"):
      print("Happy Journey")

print("<style>")

print('''body {
    background-image: url('https://www.informalnewz.com/wp-content/webp-express/webp-images/uploads/2022/08/Flight-Ticket-696x464.jpg.webp');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
    
}''')

print("</style>")
print("<table>")

print("<table border=2 align=center>")

print("<table cellspacing=10>")

print("<tr>")

print("<td>")

print("<tr><td colspan=2>")

print("<form action='End.py' method='post'>")

print("<label for='card number'>card number:</label>")

print("<input type='text' id='card number' name='card number'>")

print("<tr><td colspan=2>")

print("<label for='cvv'>cvv:</label>")

print("<input type='text' id='cvv' name='cvv'>")

print("<tr><td colspan=2>")

print("<label for='Expiry date'>Expiry date:</label>")

print("<input type='date' id='Expiry date' name='Expiry date'>")

print("<input type='submit' value='Submit'>")
      
print("</form>")

print("</table")

print("</body>")

print("</html>")
      


