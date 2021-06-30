#!/usr/bin/python3

import cgi 
import subprocess as sp

print("content-type: text/html")
print()

#print ("Hello World")
fs=cgi.FieldStorage()
pod=fs.getvalue("y")
rep=fs.getvalue("z")
out=sp.getoutput("sudo kubectl scale deployment "+pod+" --replicas="+rep+" --kubeconfig  /root/admin.conf")

print("Successfully ")
