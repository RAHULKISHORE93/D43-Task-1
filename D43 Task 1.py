# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:17:05 2022

@author: GV62


"""

import re
def solve(s):
   pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pattern,s):
      return True
   return False

username = str(input("Enter the username/email address: "))
flag=True

while flag:
    if solve(username):
       flag=False
    else:
       print("Username not valid")
       username = str(input("Enter the username/email address: "))

password = str(input("Enter your password: "))
userinfo={}
result = re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{5,16}', password)

flag2=True
while flag2:
    if result:
       flag2=False
       userinfo[username]=password
       with open('Userinfo.txt','w') as f:
         print(userinfo,file=f)
    else:
       print("Password not valid")
       password = str(input("Enter the password: "))
       
       
       
       
       
       