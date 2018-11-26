# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import os
import json

BaseBDDDir="C:\\git\\cavisson\\automation\\ToolBox\\BDD\\"
ToReadFile= BaseBDDDir+"ToRead.txt"

LogToolBoxRunTests="tmp/LOG_TOOLBOX_RUNTESTS"
lockFile="tmp/lock"
message="Hit and Run !!"
def index(request):
	return HttpResponse("<h1>Run</h1>")

def home(request,*messag):
	ToDoList=open(ToReadFile,"r").readlines()
	ToDoLists="".join(ToDoList).replace("\n"," ").split(" ")
	print(ToDoLists)
	return render(request,'RunTests/home.html',{'ToDoLists':ToDoLists})

def RunTest(request):
    
    return render(request,'RunTests/home.html')

def GetNovel(request):
    NovelContent=request.GET.get("novel")
    NovelContent=open(BaseBDDDir+"Novels\\"+NovelContent+"\\ChapterIndex.txt","r").readlines()
    NovelContent="".join(NovelContent).replace("\n"," ").split(" ")
    return render(request,'RunTests/novelContent.html',{'NovelContent':NovelContent})

def GetChapter(request):
    ChapterContent=request.GET.get("Chapter")
    ChapterContent=open(BaseBDDDir+"Chapters\\"+ChapterContent+"\\PageIndex.txt","r").readlines()
    ChapterContent="".join(ChapterContent).replace("\n"," ").split(" ")
    return render(request,'RunTests/ChapterContent.html',{'ChapterContent':ChapterContent})

def GetPage(request):
    PageContent=request.GET.get("Page")
    PageContent=open(BaseBDDDir+"Pages\\"+PageContent+".txt","r").readlines()
    PageContent="".join(PageContent).replace("\n","|").split("|")
    return render(request,'RunTests/PageContent.html',{'PageContent':PageContent})
# Create your views here.
