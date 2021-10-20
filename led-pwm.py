#!/usr/bin/python37all
import cgi
import cgitb
cgitb.enable()

data1 = cgi.FieldStorage()
b = data1.getvalue('option')

data2 = cgi.FieldStorage()
s1 = data2.getvalue('slider1')

with open('led-pwm.txt', 'w') as f:  
  f.write(str(s1))

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="option" value="a" checked> option A <br>')
print('<input type="radio" name="option" value="b"> option B <br>')
print('<input type="radio" name="option" value="c"> option C <br>')
print('<input type="submit" value="Submit">')
print('</form>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="range" name="slider1" min ="0" max="100" value ="0"><br>')
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('</html>')