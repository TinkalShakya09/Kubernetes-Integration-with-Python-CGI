#!/usr/bin/python3

import cgi 
import subprocess as sp

print("content-type: text/html")
print()

#print ("Hello World")
fs=cgi.FieldStorage()
pod=fs.getvalue("x")
out=sp.getoutput("sudo kubectl delete pod "+pod+" --kubeconfig  /root/admin.conf")

print("Successfully deleted "+out)
