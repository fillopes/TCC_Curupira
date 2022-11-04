import subprocess, sys, re, getopt
from colorama import Fore, Back, Style

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

print (Fore.GREEN + "==============================================================================")
print ("Verificando criptografia SSL")
print(Style.RESET_ALL)

sslscan_output = subprocess.check_output(["sslscan", "--no-colour", host])
sslscan_outputd = sslscan_output.decode()

matchSSLv2 = re.findall(r'SSLv2 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchSSLv2 == []:
    print("Problema com SSLv2 ativado")
    print("DROWN (Decrypting RSA with Obsolete and Weakened eNcryption). O ataque DROWN explora uma falha no protocolo SSLv2, afim de desencriptar sessões no protocolo TLS. No caso em questão, nem o servidor nem o usuário precisam utilizar o SSLv2, o protocolo só precisa estar habilitado no servidor para que o atacante explore uma falha que o auxilia a desencriptar o protocolo TLS.")

matchSSLv3 = re.findall(r'SSLv3 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchSSLv3 != []:
    print("Problema com SSLv3 ativado")
    print("Google anunciou a descoberta de uma falha no SSLv3 – protocolo SSL que tem mais de 15 anos de uso, mas ainda está ativo para atender usuários que utilizam versões mais antigas dos navegadores. Conhecida como Poodle (sigla para Padding Oracle On Downgraded Legacy Encryption), a vulnerabilidade pode permitir a interceptação e roubo de dados enquanto eles viajam pela rede, no caminho entre servidores e usuários. ")

matchTLS10 = re.findall(r'TLSv1\.0 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchTLS10 != []:
    print("Problema com TLSv1.0 ativado")

matchTLS11 = re.findall(r'TLSv1\.1 +enabled', sslscan_outputd, flags=re.I | re.M)
if matchTLS11 != []:
    print("Problema com TLSv1.1 ativado")

if matchSSLv2 and matchSSLv3 and matchTLS10 and matchTLS11 == []:
    print("tudo ok!")


print (Fore.GREEN + "==============================================================================")
print ("Verificando Portas administrativas abertas")
print(Style.RESET_ALL)

urlNMAP = re.compile(r"https?://(www\.)?")
urlNMAP = urlNMAP.sub('', host).strip().strip('/')

nmap_output = subprocess.check_output(["nmap", urlNMAP])
nmap_outputd = nmap_output.decode()

matchNMAPPort22= re.findall(r'22/[a-zA-Z]cp  open  http', nmap_outputd, flags=re.I | re.M)
if matchNMAPPort22 != []:
    print("Não é interessante que a porta de ssh esteja aberta na internet. Essa porta é muito visada por cybercriminosos para ataques de força bruta. A recomendação é de que seja restrito no firewall o acesso para apenas IPs confiáveis")

matchNMAPPort80= re.findall(r'80/[a-zA-Z]cp  open  http', nmap_outputd, flags=re.I | re.M)
if matchNMAPPort80 != []:
    print("A porta 80 está aberta e usar esse porta para trafegar dados não é seguro. Por padrão, o protocolo usado essa porta é o http e todos os pacotes trafegando usando esse protocolo não possuem criptografia e podem se facilmente interceptados e lidos por softwares de proxy ou sniffing.")

print (Fore.GREEN + "==============================================================================")
print ("Verificando criptografia SSL")
print(Style.RESET_ALL)

header_output = subprocess.check_output(["shcheck", "--colors=none", host])
header_outputd = header_output.decode()

matchHSTS = re.findall(r'\[!]\sMissing\ssecurity\sheader: [a-zA-Z]trict-Tr[a-zA-Z]nsport-Security', header_outputd, flags=re.I | re.M)
if matchHSTS != []:
    print("O cabeçalho HTTP Strict Transport Security informa ao navegador que ele nunca deve carregar um site usando HTTP e deve converter automaticamente todas as tentativas de acessar o site usando HTTP para solicitações HTTPS.")

matchXFrame = re.findall(r'[a-zA-Z]-Frame-O[a-zA-Z]tions', header_outputd, flags=re.I | re.M)
if matchXFrame != []:
    print("O cabeçalho de resposta HTTP X-Frame-Options pode ser usado para indicar se o navegador deve ou não renderizar a página em um <frame> (en-US), <iframe>, <embed> ou <object> (en-US). Sites podem usar isso para evitar ataques click-jacking (en-US), assegurando que seus conteúdos não sejam embebedados em outros sites")

matchXContentType = re.findall(r'X-Con[a-zA-Z]ent-Type-Options', header_outputd, flags=re.I | re.M)
if matchXContentType != []:
    print("Este header foi incluído pela Microsoft no IE 8 como uma maneira de webmasters serem capazes de bloquear o sniffing de conteúdo que acontecia na época, e podia transformar tipos MIME não executáveis em tipos executáveis. Desde então, outros browsers acataram a ideia mesmo que seus algoritmos de definição de MIME fossem menos agressivos.")

matchXContentSecurity = re.findall(r'Content-Security-Policy', header_outputd, flags=re.I | re.M)
if matchXContentSecurity != []:
    print("Content Security Policy (Política de Segurança de Conteúdo, também conhecida como CSP (en-US)) é uma camada adicional de segurança que facilita a detecção e mitigação de certos tipos de ataques, incluindo Cross Site Scripting (XSS (en-US)) e ataques de injeção de dados. Esses ataques são utilizados para diversos fins, e eles vão desde roubo de dados até desfiguração do site para distribuição de malware.")

