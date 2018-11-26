# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
import os

filedata="No File Selected"
TestCasesDir="C:\\git\\cavisson\\automation\\"
LogToolBoxRunTests="/tmp/LOG_TOOLBOX_RUNTESTS"
path=TestCasesDir+"ToolBox\\BDD\\ToRead.txt"
def index(request):
	return HttpResponse("<h1>AddCases</h1>")

def home(request):

	filetoopen=open(path,"r")
	outputfile=filetoopen.readlines()
	
	return render(request,'AddCases/home.html',{'filedata':filedata,'outputfile':outputfile,})

def AddNovelForm(request):
    	ChapterAvailable=os.listdir("C:\\git\\cavisson\\automation\\ToolBox\\BDD\\Chapters")
    	print(ChapterAvailable)
    	return render(request,'AddCases/AddNovel.html',{'ChapterAvailable':ChapterAvailable})
# Create your views here.
