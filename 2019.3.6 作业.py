
import re

ifcfg = 'eno33554944: flags=4163 mtu 1500\n inet 202.100.1.138 netmask 255.255.255.0 broadcast 202.100.1.255\n inet6 fe80::20c:29ff:fe8d:5cb6 prefixlen 64 scopeid 0x20\n ether 00:0c:29:8d:5c:b6 txqueuelen 1000 (Ethernet)\n RX packets 0 bytes 0 (0.0 B)\n RX errors 0 dropped 0 overruns 0 frame 0\n TX packets 33 bytes 4290 (4.1 KiB)\n TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0\n\n'
ifcfg1 = re.findall('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifcfg)
ifcfg2 = re.findall('fe80::\w+:\w{4}:\w{4}:\w{4}',ifcfg)

print('{0:>7} : {1:>}'.format('MAC地址',ifcfg1[0]))
print('{0:>7} : {1:>}'.format('ipv6地址',ifcfg2[0]))

