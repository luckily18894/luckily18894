
import os

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

l1 = []
l2 = os.listdir()
luckily = 0
print(l2)

for x in l2:
    # if os.path.isdir(x):
    #     os.chdir(x)
    #       l3 = os.listdir(x)
    #       for q in l3:
    #      if os.path.isfile(q):
    #         for y in open(q):
    #             if 'qytang' in y:
    #                 l1.append(q)

    if os.path.isfile(x):
        for z in open(x):
            if 'qytang' in z:
                l1.append(x)

print('文件中包含"qytang"关键字的文件为:')
for a in l1:
    print(' '*5,a)

os.remove('qytang1')
os.remove('qytang2')
os.remove('qytang3')
os.rmdir('qytang4')
os.rmdir('qytang5')
os.chdir('..')
os.rmdir('test')

