#!/bin/python

"""
 Create the hosts file and give the path in 'hosts' parameter
 <ipadd1>#<hostname1>#<username>#<password>
 <ipadd2>#<hostname2>#<username>#<password>
 <ipadd3>#<hostname3>#<username>#<password>
"""

import paramiko

ssh = paramiko.SSHCLient()
hosts = open('<hosts-file-path>','r')

commands = '''
hostname
pwd
cd /opt/simility/bin
sh shutdown_cassandra.sh
sh startup_cassandra.sh
'''

for i in hosts.readlines:
	lines = i.strip()
	split_line = lines.split('#')
	print(split_line)

#subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#stdout, stderr = process.communicate(commands.encode('utf-8'))
#print.stdout()
ssh.set_missing_host.key_policy(paramiko.AutoAddPOlicy())
ssh.connect('%s' %split_line[0], port = 22, username = '%s' %split_line[2], password = '%s' %split_line[3])
stdin, stdout, stderr = ssh.exec_command(commands.encode('utf-8')
output = stdout.readlines()
output = "".join(output)
print(output)