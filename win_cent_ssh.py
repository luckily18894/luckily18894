
import paramiko
# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('172.16.1.102',port=22,username='root',password='Cisc0123',timeout=5,compress=True)
# stdin,stdout,stderr = ssh.exec_command('ls')
# x = stdout.read().decode()
# print(x)


def py_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password, port=port, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()

    return x


if __name__ == '__main__':
    print(py_ssh('192.168.241.128', 'root', 'xxxxxx'))
    print(py_ssh('192.168.241.128', 'root', 'xxxxxx', cmd='pwd'))

