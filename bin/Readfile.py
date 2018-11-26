import paramiko

print "connecting"

try:
    hostname="10.10.30.23"
    username="root"
    password="C@VAdmin123!!"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,username=username , password=password)
    print "Conncet to %s"%hostname
    print "connected"
except Exception as e :
    print e.message

try:
    print "Following is the readers file"
    stdin, stdout, stderr = ssh.exec_command('cat /net/cvsroot/CVSROOT/readers')
    err = ''.join(stderr.readlines())
    out = ''.join(stdout.readlines())
    final_output = str(out) + str(err)
    print final_output

except Exception as e:
    print e.message

