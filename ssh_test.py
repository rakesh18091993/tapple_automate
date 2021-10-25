# import time
# from subprocess import Popen, PIPE
# def run_ssh_cmd(host, cmd):
#     cmds = ['ssh', '-t', host, cmd]
#     return Popen(cmds, stdout=PIPE, stderr=PIPE, stdin=PIPE)

# results = run_ssh_cmd('root@', 'ls -l').stdout.read()
# print(results)


import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='165.232.191.99', username='root')
stdin, stdout, stderr = ssh_client.exec_command('amiok')
lines = stdout.readlines()
print(lines)