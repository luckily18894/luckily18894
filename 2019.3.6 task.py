
department1='Security'
department2='Python'
manager1='cq_bomb'
manager2='qinke'
CF_SEC=456789.12456
CF_Python=1234.3456

# 老  中文标点
line1='Department1 name：%-10s Manager：%-9s COURSE FEES：%-10.2f The End！'%(department1,manager1,CF_SEC)
line2='Department2 name：%-10s Manager：%-9s COURSE FEES：%-10.2f The End！'%(department2,manager2,CF_Python)

# 新  英文标点
line3='Department1 name:{0:<10s} Manager:{1:<9s} COURSE FEES:{2:<10.2f} The End!'.format(department1,manager1,CF_SEC)
line4='Department2 name:{0:<10s} Manager:{1:<9s} COURSE FEES:{2:<10.2f} The End!'.format(department2,manager2,CF_Python)

length1=len(line1)
print('='*length1)
print(line1)
print(line2)
print('='*length1)
length2=len(line3)
print('='*length2)
print(line3)
print(line4)
print('='*length2)

