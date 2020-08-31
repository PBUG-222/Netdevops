#!/usr/bin/python3.6
#coding:utf-8
#登入多台设备
import paramiko
import time
import getpass
#from netaddr import IPAddress,IPNetwork

def login(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password)
 
    print("successful login to "+hostname)

    command = ssh_client.invoke_shell()
    command.send("en\n")
    command.send(password+"\n")
    command.send("config t\n")

    return ssh_client,command


if __name__ == "__main__":
    username = "root"
    password = getpass.getpass("input passwoed:")
    
    f = open("ip_list.txt","r")
    for line in f.readlines():
        ip =  line.strip()
        ssh_client,command = login(ip, username,password) 

        command.send("router ospf 1\n")
        #command.send("network " +ip+" " + str(IPNetwork(ip).hostmask))  
    
        time.sleep(2)

        output = command.recv(65535)
        print output

    f.close
    ssh_client.close


