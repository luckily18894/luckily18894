
s1='Port-channel1.189     192.168.189.254  YES   CONFIG  up'
import re
s2=re.match('\s*(.+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)\s*', s1).groups()

print('-'*50)
print(s2)
print('{0:<5s} : {1:<}'.format('接口',s2[0]))
print('{0:<5s} : {1:<}'.format('IP地址',s2[1]))
print('{0:<5s} : {1:<}'.format('状态',s2[4]))

