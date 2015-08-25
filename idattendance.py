import re
import mechanize

#Creating the Browser and opening Moodle
br = mechanize.Browser()
br.open("https://courses.iitm.ac.in/login/index.php")

#Logging into Moodle
br.select_form(nr = 0)

#Put username and password

br["username"] = "PUT_USERNAME"
br["password"] = "PUT_PASSWORD"
logged_in = br.submit()

# Open the ID1200 page
r=br.open("https://courses.iitm.ac.in/course/view.php?id=1783")
    
# Open the most recent attendance link
for item in br.links():
   if 'Attend' in str(item):
      br.open(item.url)
      break

br.select_form(nr=0)
br.form['q807']=['y']
br.submit()
print 'Your attendance for today has been given.'
