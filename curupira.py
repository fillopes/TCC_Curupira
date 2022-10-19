import subprocess, sys, re

output = subprocess.check_output(["sslscan", "--no-colour", "https://google.com"])
outputd = output.decode()
#print(outputd)
match = re.findall(r'SSLv2 +enabled', outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com SSLv2 ativado")
match = re.findall(r'SSLv3 +enabled', outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com SSLv3 ativado")
match = re.findall(r'TLSv1\.0 +enabled', outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com TLSv1.0 ativado")
match = re.findall(r'TLSv1\.1 +enabled', outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com TLSv1.1 ativado")