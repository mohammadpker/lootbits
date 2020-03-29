from mechanize import *
from time import sleep

br = Browser()
br.set_header(header ='user-agent')
br.set_handle_robots(False)
br.open('https://lootbits.io/login.php?')
br.select_form(nr=0)
br.form['username']='azazeil'
br.form['password']='123456789'
br.submit()
s=0
while s==0:
    sleep(3600)
    for ii in br.links():
        if 'claim' in ii.url:
            m = ii.url
            br.open('https://lootbits.io/dashboard.php'+m)
