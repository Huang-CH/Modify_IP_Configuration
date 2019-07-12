#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 此脚本已在CentOS 7 上测试通过
# 作者：H&C

import os

print('='*50)
print('本程序将自动设置CentOS 7的IP地址')
print('='*50)

os.system('yum -y update')
print('='*50)
os.system(ifconfig)
print('='*50)

net_card = input('请输入网卡名称：')
ipaddr = input('请输入需要设置的IP地址：').strip()
prefix = input('请输入需要设置子网掩码位数：').strip()
gateway = input('请输入网关地址：').strip()
dns1 = input('请输入DNS1地址：').strip()
dns2 = input('请输入DNS2地址：').strip()

net_card_add = ('''
IPADDR=%s
PREFIX=%s
GATEWAY=%s
DNS1=%s
DNS2=%s 
''') %(ipaddr,prefix,gateway,dns1,dns2)

with open(r'/etc/sysconfig/network-scripts/%s' %(net_card),mode='r',encoding='utf-8') as read_file,\
        open(r'/etc/sysconfig/network-scripts/%s_swap' %(net_card),mode='w',encoding='utf-8') as write_file:
    for line in read_file:
        if 'dhcp' in line:
            line.replace('static')
        write_file.write(line)
    write_file.write(net_card_add)
    os.remove('%s' %(net_card))
    os.rename('%s_swap' (net_card),'%s' (net_card))

os.system('/etc/init.d/network restart')
