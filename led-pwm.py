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
print("selection = " + data1.getvalue("option"))
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')