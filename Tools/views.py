# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import os
import paramiko

def connect(hostname,username,password,command):
	try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname,username=username , password=password)
                print("Conncet to %s"%hostname)
                print("connected")
                connectionR="Connected"
	except Exception as e :
                print(e.message)
                connectionR="Error To Connect"
	try:
                stdin, stdout, stderr = ssh.exec_command(command)
                err = ''.join(stderr)
                out = ''.join(stdout)
                final_output = str(out) + str(err)
	except Exception as e:
                print(e.message)
                commandR="Command Failed"
	
	return connectionR,commandR,final_output


TestCasesDir="/home/automation/workbench/automation/netocean/smoke/testcases/"
LogToolBoxRunTests="/tmp/LOG_TOOLBOX_RUNTESTS"
hostname="10.10.30.185"
username="cavisson"
password="cavisson"
readersFile="/home/automation/webapp/ToolBox/tmp/readers"
writersFile="/home/automation/webapp/ToolBox/tmp/writers"
hostname="10.10.30.23"
username="root"
password="C@VAdmin123!!"
readersFile="/net/cvsroot/CVSROOT/readers"
writersFileOrig="/net/cvsroot/CVSROOT/writers"
writersFile="/tmp/writers_tools"


def index(request):
	return HttpResponse("<h1>Tools</h1>")

def home(request):
	open('tmp/processLog', 'a+').write("Rebuild Home Page\n")
	open('tmp/processLogAll', 'a+').write("Rebuild Home Page\n")
	try:
    		ssh = paramiko.SSHClient()
    		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    		ssh.connect(hostname,username=username , password=password)
    		print("Conncet to %s"%hostname)
    		print("connected")
	except Exception as e :
    		print(e.message)
	
	try:
    		print("Following is the readers file")
    		stdin, stdout, stderr = ssh.exec_command('cat {}'.format(readersFile))
    		err = ''.join(stderr)
    		out = ''.join(stdout)
    		final_output = str(out) + str(err)
	except Exception as e:
                print(e.message)
                final_output="error to cat"

	try:
                print("Following is the writers file")
                stdin, stdout, stderr = ssh.exec_command('cat {}'.format(writersFile))
                err = ''.join(stderr)
                out = ''.join(stdout)
                final_outputW = str(out) + str(err)

	except Exception as e:
    		print(e.message)
        	
	listofreaders=final_output.split("\n")
	listofWriters=final_outputW.split("\n")
	print(request.POST.get('formlabel', None))
	processLog=open('tmp/processLog', 'r').readlines()
	processLogAll=open('tmp/processLogAll', 'r').readlines()[::-1]
	open('tmp/processLog', 'w').write("") 
	return render(request,'Tools/home.html',{'listofreaders':listofreaders,'listofWriters':listofWriters,'processLog':processLog,'processLogAll':processLogAll})

def enableS(request):
	if request.method == 'POST':
		print("Found request enable")
		name=request.POST['UserNameE']
		time=request.POST['UserTime']
		try:
                	ssh = paramiko.SSHClient()
                	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                	ssh.connect(hostname,username=username , password=password)
                	print("Conncet to %s"%hostname)
                	print("connected")
		except Exception as e :
                	print(e.message)
                	final_output="error to connect"

		try:
	                print("peerforming enable for single persone")
        	        stdin, stdout, stderr = ssh.exec_command("sed -i '/{}$/d' {} && echo '{}' >>{}".format(name,readersFile,name,writersFile))
                	err = ''.join(stderr)
                	out = ''.join(stdout)
                	final_output2 = str(out) + str(err)
	                print(final_output2)
                	print("Following is the writers file")
	                open('tmp/processLogAll', 'a+').write("enabled for {}\n".format(name))
	                open('tmp/processLog', 'w').write("enabled for {}\n".format(name))
		except Exception as e:
                	print(e.message)
                	final_output="error to cat"
	                print(name)
	return HttpResponseRedirect("/Tools/home")


def disableS(request):
        if request.method == 'POST':
                print("in")
                name=request.POST['UserNameD']
                try:
                	ssh = paramiko.SSHClient()
                	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                	ssh.connect(hostname,username=username , password=password)
                	print("Conncet to %s"%hostname)
                	print("connected")
                except Exception as e :
                	print(e.message)
                	final_output="error to connect"

                try:
                        print("peerforming enable for single persone")
                        stdin, stdout, stderr = ssh.exec_command("echo '{}' >>{} && sed -i '/{}$/d' {}".format(name,readersFile,name,writersFile))
                        err = ''.join(stderr)
                        out = ''.join(stdout)
                        final_output2 = str(out) + str(err)
                        print(final_output2)
                        print("Following is the writers file")
                        open('tmp/processLogAll', 'a+').write("disabled for {}\n".format(name))
                        open('tmp/processLog', 'w').write("disabled for {}\n".format(name))
                except Exception as e:
                        print(e.message)
                        final_output="error to cat"
                        print(name)
        return HttpResponseRedirect("/Tools/home")

def enableAll(request):
	if request.method == 'POST':
                try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(hostname,username=username , password=password)
                        print("Conncet to %s"%hostname)
                        print("connected")
                except Exception as e :
                        final_output="error to connect"
                try:
        	        print("Going to enable commit on CVS server")
        	        stdin, stdout, stderr = ssh.exec_command('cat {} >{} && bash /net/cvsroot/CVSROOT/commit_write'.format(writersFileOrig,writersFile))
        	        err = ''.join(stderr.readlines())
        	        out = ''.join(stdout.readlines())
                	final_output = str(out) + str(err)
	                print(final_output)
        	        open('tmp/processLogAll', 'a+').write("enabled for All\n")
                	open('tmp/processLog', 'w').write("enabled for All\n")
                except Exception as e:
                        print(e.message)
                        final_output="error to cat"
                        print(final_output)
                        open('tmp/processLogAll', 'a+').write("enabled for All\n")
                        open('tmp/processLog', 'w').write("enabled for All\n")
	return HttpResponseRedirect("/Tools/home")

def disableAll(request):
	if request.method == 'POST':
                try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(hostname,username=username , password=password)
                        print("Conncet to %s"%hostname)
                        print("connected")
                except Exception as e :
                        print(e.message)
                        final_output="error to connect"
                
	return HttpResponseRedirect("/Tools/home")

# Create your views here.
