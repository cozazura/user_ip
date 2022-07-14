#! /usr/bin/env python

import paramiko
print( "Introduceti numele pentru user-ul pe care doriti sa-l creati: " )
user= str(input())
print( "Introduceti parola pentru user-ul pe care doriti sa-l creati: " )
parola= str(input())
with open(r'ip.txt','r') as f:
    ip = f.read().splitlines()
with open(r"ip.txt", 'r') as f:
    for count, line in enumerate(f):
        pass
for i in range(0,count):
    print( "nume user pentru ip ", ip[i] , ":")
    nume_c= str(input())
    print( "parola pentru ip ", ip[i] , ":")
    parola_c= str(input())
    command= "sudo useradd -p $(openssl passwd -1 " +parola+") "+ user 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip[i], username=nume_c, password=parola_c)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    ssh.close()
