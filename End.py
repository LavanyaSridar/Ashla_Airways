#!C:\Users\LAVANYA\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb

cgitb.enable()

form=cgi.FieldStorage()

if form.getvalue("name"):
      name = form.getvalue("name")



print ("Content-type:text/html\n")

print("<html>")

print ("<head>")

print ("<title>First CGI Program</title>")

print ("</head>")

print("<body>")

print("<h1> Payment Successful </h1>")

print("<h2> Yass! Tickets has been booked </h1>")

print("<h2> Happy Journey </h2>")

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

print("</body>")

print("</html>")
