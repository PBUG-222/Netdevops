#!/usr/bin/python3.8
#coding:utf-8

import asyncio
import netdev
import time

async def task(dev):
    try:
        async with netdev.create(**dev) as ios:
            print("Successfully connect to "+dev['host'])
            commands = ['router ospf 66','end','show ip int brief ']
            output = await ios.send_config_set(commands)
            print(output)
    except :
                print ("cat't connect to "+dev['host'])

    #axcept paramiko.ssh_exception.AuthenticationException:
                #rint(dev['ip']+" password eer")

    
   

async def run():
    devices = []
    f = open("ip_list.txt","r")
    for line in f.readlines():
        ip = line.strip()
        dev={
             'device_type' :'cisco_ios',
             'host' : ip,
             'username' :"root",
             'password' : "cisco123",
             'secret' : "cisco123"
        }
        devices.append(dev)
    
    tasks = [task(dev) for dev in devices]
    
    await asyncio.wait(tasks)

start_time = time.time()
# 获取EventLoop:
print (111)
#loop = asyncio.get_event_loop()
# 执行coroutine
#loop.run_until_complete(run())
#loop.clos
asyncio.run(run())

print ('Spend %.2f '%(time.time()-start_time))
         
