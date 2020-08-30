#!/usr/bin/env python3.63.63.6

import sys
import getopt,getpass
from netmiko import ConnectHandler

def Usage():
    print("Usage: %s[option]" %sys.argv[0])
    print("-H :hostname")
    print("-u :username")
    print("-p :password")
    print("-h :help information")
    
def handler_opts():
    device = {
        'device_type': 'cisco_ios',
        'username': 'root',
        'port': 22
        }
    
    try:
        opts,args = getopt.getopt(sys.argv[1:],"H:p:u:h",["hostname=","port=","username=","help"])
        
        
        if len(sys.argv) == 1:
            Usage()
            sys.exit(1)
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                Usage()
              #  sys.exit(1)
            elif opt in ("-H", "--hostname"):
                device["host"] = arg
              #  sys.exit(1)
            elif opt in ("-p","--port"):
                device["port"] = int(arg)
            elif opt in ("-u","--username"):
                device ["username"] = arg
          
    except getopt.GetoptError:
        Usage()
        sys.exit(1)
    return device


  
        
if __name__ == "__main__":
    print("dede")
    device = handler_opts()
    print("input enable password")
    device["password"] = getpass.getpass()
    device["secret"]   = getpass.getpass()
    net_connect = ConnectHandler(**device)
    
    #要配置的命令
    config_commands = ['interface f0/0','noshutdown']
    #提交要配置的命令，input为提交的真实内容
    input = net_connect.enable()
    print(input)
