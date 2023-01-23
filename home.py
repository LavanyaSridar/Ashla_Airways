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


print("<table border=2 align=center>")

print("<tr>")

print("<td>")

print("<table cellspacing=10>")

print("<tr><td colspan=3><h1>Booking Information</h1></td></tr>")

print("<tr><td>From:</td><td colspan=1><input type='text'>")

print("<tr><td>To:</td><td colspan=1><input type='text'>")

print("</form>")

print("<tr><td colspan=2>")

print("<label for='Departure Date'>Departure Date:</label>")

print(" <input type='date' id='Departure Date' name='Departure Date'>")

print("</form>")

print("<br>")

print("<form>")

print("<tr><td colspan=2>")

print("<label for='Returning Date'>Returning Date:</label>")

print(" <input type='date' id='Returning Date' name='Returning Date'>")

print("</form>")

print("<form>")

print("<tr><td colspan=2>")

print("<label for='Adults 12+years'>Adults 12+years</label>")

print("<select id='Adults 12+years' name='Adults 12+years' form='Adults 12+years'>")

print("<option value='0'>0</option>")

print("<option value='1'>1</option>")

print("<option value='2'>2</option>")

print("<option value='3'>3</option>")

print("<option value='4'>4</option>")

print("<option value='5'>5</option>")

print("<option value='6'>6</option>")

print("<option value='7'>7</option>")

print("<option value='8'>8</option>")

print("<option value='9'>9</option>")

print("</form>")

print("<form>")

print("<tr><td colspan=2>")

print("<label for='Children'>Children</label>")

print("<select id='Children' name='Children' form='Children'>")

print("<option value='0'>0</option>")

print("<option value='1'>1</option>")

print("<option value='2'>2</option>")

print("<option value='3'>3</option>")

print("<option value='4'>4</option>")

print("<option value='5'>5</option>")

print("<option value='6'>6</option>")

print("<option value='7'>7</option>")

print("<option value='8'>8</option>")

print("<option value='9'>9</option>")

print("</form>")

print("<form>")

print("<tr><td colspan=2>")

print("<label for='Class'>Class</label>")

print("<select id='Class' name='Class' form='Class'>")

print("<option value='Economy'>Economy</option>")

print("<option value='Business'>Business</option>")

print("<option value='First'>First</option>")

print("</select>")

print("</form>")

print("</td>")

print("</tr>")

print("<tr>")

print("<td>")
      
print("</td>")

print("<td>")

print("</td>")

print("</tr>")

print("<form>")

print("<tr><td colspan=2>")

print("<label for='Payment'>Payment</label>")

print("<select id='Payment' name='Payment' form='Payment'>")

print("<option value='Mastercard'>Mastercard</option>")

print("<option value='Visa'>Visa</option>")

print("<option value='American Express'>American Express</option>")

print("<tr><td colspan=2>")

print("</select>")

print("</form>")

print("<tr><td colspan=2>")

print("<form method='post' action='Pay.py'>")

print("<input type='submit' value='Next'>")

print("</form>")

print("</table>")

print("</body>")

print("</html>")
