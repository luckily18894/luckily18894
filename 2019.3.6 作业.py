
import re

ifcfg = 'eno33554944: flags=4163 mtu 1500\n inet 202.100.1.138 netmask 255.255.255.0 broadcast 202.100.1.255\n inet6 fe80::20c:29ff:fe8d:5cb6 prefixlen 64 scopeid 0x20\n ether 00:0c:29:8d:5c:b6 txqueuelen 1000 (Ethernet)\n RX packets 0 bytes 0 (0.0 B)\n RX errors 0 dropped 0 overruns 0 frame 0\n TX packets 33 bytes 4290 (4.1 KiB)\n TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0\n\n'
ifcfg1 = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifcfg)

for ip in ifcfg1:
    if ip[-1] == '0':
        mask = ip
    elif ip[-3:] == '255':
        brodcast = ip
    else : ipadd = ip

print(ifcfg1)
print('{0:>13} : {1:<}'.format('Network Mask', mask))
print('{0:>13} : {1:<}'.format('Broadcast', brodcast))
print('{0:>13} : {1:<}'.format('IPv4 Addr', ipadd))

