#!C:\Users\LAVANYA\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb

cgitb.enable()

a=cgi.FieldStorage()




print ("Content-type:text/html\n")

print("<html>")

print("<body>")

print("<style>")

print('''body {
    background-image: url('https://www.informalnewz.com/wp-content/webp-express/webp-images/uploads/2022/08/Flight-Ticket-696x464.jpg.webp');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
    
}''')

print("</style>")


print("<form>")

print("<h1 align=center>Manage Your Trip</h1>")

print("<p align=center><u>Fare Details for Air India</u></p>")

print("<table align=center border=2 cellpadding=10>")

print("<tr>")

print("<th>Class</th>")

print("<th>Fare</th>")

print("</tr>")

print("<tr>")

print("<td>Economy</td>")

print("<td>10,000/-</td>")

print("</tr>")

print("<tr>")

print("<td>Executive</td>")

print("<td>20,000/-</td>")

print("</tr>")

print("<tr>")

print("<td>First</td>")

print("<td>30,000/-</td>")

print("</tr>")

print("</table>")

print("<h3 align=right><a href='home.py'>Home</a><h3>")

print("</form>")

print("</body>")

print("</html>")
