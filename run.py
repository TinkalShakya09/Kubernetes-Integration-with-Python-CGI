#!/usr/bin/python3

import cgi 
import subprocess as sp

print("content-type: text/html")
print()

#print ("Hello World")
fs=cgi.FieldStorage()
pod=fs.getvalue("x")
img=fs.getvalue("y")
out=sp.getoutput("sudo kubectl run "+pod+" --image="+img+" --kubeconfig  /root/admin.conf")

print("Successfully run "+out)
