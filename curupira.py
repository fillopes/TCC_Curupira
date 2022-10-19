import subprocess, sys, re

output = subprocess.check_output(["sslscan", "--no-colour", "https://google.com"])
outputd = output.decode()
print(outputd)
match = re.findall(r'TLSv1\.1\s\s\senabled', outputd,flags=re.I|re.M)
print (match)