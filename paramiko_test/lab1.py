#!/usr/bin/python3.6
#coding:utf-8
#登入设备
import paramiko
import time

def login(hostname,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)
    print("sucessfully login to "+ hostname)

    command = ssh_client.invoke_shell()
    
    command.send("en\n")
    command.send("cisco123\n")
    

    return ssh_client,command


def add_vlan(command,start, end, step=1):
     command.send("config t\n")
     
     for i in range(start, end, step):
         command.send("vlan "+str(i)+"\n")
    

if __name__ == "__main__":
    hostname = '192.168.10.33'
    username = 'root'
    password = 'cisco123'

    ssh_client,command = login(hostname,username,password)
    
    add_vlan(command, 10, 50, 5)

    time.sleep(2)

    output = command.recv(65535)
    print output
    
    ssh_client.close

    





