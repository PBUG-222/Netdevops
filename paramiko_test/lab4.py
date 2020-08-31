#!/usr/bin/python2.7
#coding:utf-8

#增加多台设备登入时的异常处理

import paramiko
import getpass
import sys
import time

username = "root"
password = getpass.getpass('input passwoed:')


f = open("ip_list.txt","r")
for line in  f.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip, username=username, password=password)
        print "successfully connect to "+line
        command = ssh_client.invoke_shell()
        command.send("en\n")
        command.send(password + "\n")
        command.send("show ip int brief\n")
        
        time.sleep(2)
        print command.recv(65535)
   
        f.close
        ssh_client.close
        
    except paramiko.ssh_exception.NoValidConnectionsError:
        print "cat't connect to "+ip

    except paramiko.ssh_exception.AuthenticationException:
        print ip+" password eer"
