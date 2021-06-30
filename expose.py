#!/usr/bin/python3

import cgi 
import subprocess as sp

print("content-type: text/html")
print()

#print ("Hello World")
fs=cgi.FieldStorage()
pod=fs.getvalue("x")
port= fs.getvalue("y")

out=sp.getoutput("sudo kubectl expose deployment "+cmd+" --type=LoadBalancer "+port+" --kubeconfig adimn.conf")

print("Your service expose Successfully"+out)
