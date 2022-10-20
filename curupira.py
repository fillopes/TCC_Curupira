import subprocess, sys, re, getopt


host =""
directory =""
argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "h:d:", ["host =", "directory ="])
except:
    print("Error Message ")
 
for name, value in options:
    if name in ['-h', '--host']:
        host = value
    elif name in ['-d', '--directory']:
        directory = value


output = subprocess.check_output(["sslscan", "--no-colour", host])
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