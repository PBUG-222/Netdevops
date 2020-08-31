#!/usr/bin/python2.7
#coding:utf-8

import time 
import subprocess
import os

class Test_Reachable(object):
    four_byte = ['1','11','111','22']

    def __init__(self):
        self.ping()
    
    def ping(self):
        if os.path.exists("reachable_ip.txt"):
            os.remove("reachable_ip.txt")

        for ip4 in self.four_byte:
            self.ipaddress = "172.16.10."+ip4
            print "test "+ self.ipaddress
            self.ping_result = subprocess.call(['ping','-c','2','-w','2',self.ipaddress])
            time.sleep(1)

            self.f = open('reachable_ip.txt', 'a')
            
            if self.ping_result == 0:
                self.f.write(self.ipaddress + "\n")
        self.f.close

if __name__ == '__main__':
    script1_1 = Test_Reachable()
