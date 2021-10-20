#!/usr/bin/python37all
import cgi
import cgitb
cgitb.enable()

data = cgi.FieldStorage()
b = data.getvalue('option')
s1 = data.getvalue('slider1')

with open('led-pwm.txt', 'w') as f:  
  f.write(str(s1))

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="option" value="a" checked> LED 1 <br>')
print('<input type="radio" name="option" value="b"> LED 2 <br>')
print('<input type="radio" name="option" value="c"> LED 3 <br>')
print('<input type="submit" value="Submit"><br>')
print('<input type="range" name="slider1" min ="0" max="100" value ="0"><br>')
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('</html>')