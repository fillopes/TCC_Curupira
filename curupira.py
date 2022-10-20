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


sslscan_output = subprocess.check_output(["sslscan", "--no-colour", host])
sslscan_outputd = sslscan_output.decode()
#print(outputd)
match = re.findall(r'SSLv2 +enabled', sslscan_outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com SSLv2 ativado")
match = re.findall(r'SSLv3 +enabled', sslscan_outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com SSLv3 ativado")
match = re.findall(r'TLSv1\.0 +enabled', sslscan_outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com TLSv1.0 ativado")
match = re.findall(r'TLSv1\.1 +enabled', sslscan_outputd,flags=re.I|re.M)
if match != []:
    print ("Problema com TLSv1.1 ativado")

