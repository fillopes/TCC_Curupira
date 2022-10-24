import subprocess, sys, re, getopt

host = ""
directory = ""
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

matchSSLv2 = re.findall(r'SSLv2 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchSSLv2 != []:
    print("Problema com SSLv2 ativado")

matchSSLv3 = re.findall(r'SSLv3 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchSSLv3 != []:
    print("Problema com SSLv3 ativado")

matchTLS10 = re.findall(r'TLSv1\.0 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchTLS10 != []:
    print("Problema com TLSv1.0 ativado")

matchTLS11 = re.findall(r'TLSv1\.1 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchTLS11 != []:
    print("Problema com TLSv1.1 ativado")
