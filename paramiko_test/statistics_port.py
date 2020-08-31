#!/usr/bin/python2.7
#coidng:utf-8

import paramiko
import time
import re
import getpass
from datetime import datetime

class statistics_port():
    now = datetime.now()
    data = "%s-%s-%s" %(now.month, now.day, now.year)
    time = "%s-%s-%s" %(now.hour, now.minute, now.second)

    total_up_port = 0 

    def __init__(self):
        self.login()
        self.summary()

    def login(self):
        self.f = open("reachable_ip.txt")
        self.num_of_open_switch = len(self.f.readlines())
        print self.num_of_open_switch
        self.f.seek(0)
          
        for line in self.f.readlines():
            try:
                self.ip = line.strip()
                self.ssh_client = paramiko.SSHClient()
                self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                
                self.ssh_client.connect(hostname=self.ip, username='root', password='cisco123')
                print "\nconnect to " +self.ip

                self.command = self.ssh_client.invoke_shell()
                self.check_up_port()

                self.ssh_client.close
            except paramiko.ssh_exception.NoValidConnectionsError:
                print "cat't connect to "+self.ip

            except paramiko.ssh_exception.AuthenticationException:
                print self.ip+" password eer"
            
            
            



    def check_up_port(self):
        self.command.send("en\n")
        self.command.send("cisco123\n")
        self.command.send("sh ip int brief | include up\n")
        
        time.sleep(1)
        output = self.command.recv(65535)
        print output
        
        self.search_up_port = re.findall(r'FastEthernet', output)
        self.number_up_port = len(self.search_up_port)
        print self.ip + " has "+str(self.number_up_port)+" port up"
        print "###################"
        self.total_up_port += self.number_up_port
        

    def summary(self):
        self.total_port = self.num_of_open_switch * 2
        print "\n"
        print "****************************"
        print self.data + ' ' + self.time+'\n'
        print "There are "+str(self.total_port)+" port "+str(self.total_up_port) + " is up"
        print "****************************"
        

if __name__ == "__main__":
    statistics_port()
