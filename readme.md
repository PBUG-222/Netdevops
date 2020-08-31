#Netdevops常用模块  
##telnetlib  
[docs文档](https://docs.python.org/zh-cn/2.7/library/telnetlib.html)
*class telnetlib.Telnet([host[, port[, timeout]]])*
    <?python
import getpass
import sys
import telnetlib

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()

##paramiko  
##netmiko  

