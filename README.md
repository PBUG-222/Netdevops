# Netdevops常用模块
## telnetlib
[docs文档](https://docs.python.org/zh-cn/2.7/library/telnetlib.html)

**class telnetlib.Telnet([host[, port[, timeout]]])**

```
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
```
## paramiko
[doc文档](https://www.worldlink.com.cn/osdir/netmiko.html)  
```
from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_command('show ip int brief')
print(output)
``` 

## netdev
```
import asyncio 
import netdev 
     async def task(param):async with netdev.create(**param) asios:
	 # Testing sending simple  command
	 out=awaitios.send_command("show ver")
	 print(out)
	 # Testing sending configuration set
	 commands=["line console 0","exit"]
	 out=awaitios.send_config_set(commands)
	 print(out)
	 # Testing sending simple command with long output
	 out=awaitios.send_command("show run")
	 print(out)
	 # Testing interactive dialog
	 out=awaitios.send_command("conf",pattern=r'\[terminal\]\?',strip_command=False)
	 out+=awaitios.send_command("term",strip_command=False)
	 out+=awaitios.send_command("exit",strip_command=False,strip_prompt=False)
	 print(out)
	 async def run():
	     dev1={'username':'user','password':'pass','device_type':'cisco_ios','host':'ip address',}
		 dev2={'username':'user','password':'pass','device_type':'cisco_ios','host':'ip address',} 
		 devices=[dev1,dev2] 
		 tasks=[task(dev) for dev in devices]
		 awaitasyncio.wait(tasks)
		 loop=asyncio.get_event_loop()
		 loop.run_until_complete(run())
```
