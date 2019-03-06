
import re

s = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

l1 = s.split('\n')
dc1 = {}

for x in l1:
    r = re.match(
        '.+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)\s*Teacher\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+).+bytes\s*(\d+).+flags\s*(\w*)\s*',
        x).groups()
    key1 = r[0],r[1],r[2],r[3]
    value1 = r[4],r[5]
    dc1[key1] = value1

print('\n打印字典\n')
print(dc1)
print('\n格式化输出\n')
print('='*100)

for key1,value1 in dc1.items():
    print('{0:>8} : {1:<15}|{2:>9} : {3:<6}|{4:>7} : {5:<18}|{6:>9} : {7:<12}|'.format('src', key1[0], 'src_p', key1[1],
                                                                                       'dst', key1[2], 'dst_p',
                                                                                       key1[3]))
    print('{0:>8} : {1:<15}|{2:>9} : {3:<6}|{4:^28}|{4:^24}|'.format('bytes', value1[0], 'flags', value1[1],' '))
    print('=' * 100)

