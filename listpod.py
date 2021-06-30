#!/usr/bin/python3

import cgi 
import subprocess as sp

print("content-type: text/html")
print()

#print ("Hello World")
fs=cgi.FieldStorage()

out=sp.getoutput("sudo kubectl get pod --kubeconfig  /root/admin.conf")

print(out)
