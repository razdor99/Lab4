#!/usr/bin/python37all
import cgi
import cgitb
cgitb.enable()

data = cgi.FieldStorage()
b = data.getvalue('option')
s1 = data.getvalue('slider1')

with open('led-pwm.txt', 'w') as f:  
  f.write(str(s1))
with open('led-pwm1.txt', 'w') as d:  
  d.write(str(b))
print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="option" value="1" checked> LED 1 <br>')
print('<input type="radio" name="option" value="2"> LED 2 <br>')
print('<input type="radio" name="option" value="3"> LED 3 <br>')
print('<input type="range" name="slider1" min ="0" max="100" value ="0"><br>')
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('</html>')