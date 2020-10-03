# common TCP Ports
# . Telnet(23)-Login
# . SSH (22) - Secure Login
# . HTTP (80)
# . HTTPS (443)
# . SMTP (25) (Mail)
# . IMAP (I43/220/993) - Mail Retrieval
# . POP(109/110) - Mail Retrieval
# . DNS (53) - Domain Name
# . FTP (21) - File Transfer

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()
