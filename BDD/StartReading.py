import os
from bins.Functions import convert 
ToReadFile="ToRead.txt"

def ReadPage(Page):
    Story=open("Pages/{}.txt".format(Page),"r").readlines()
    convert(Story)

def ReadChapter(Chapter):
    PageList=open("Chapters/{}/PageIndex.txt".format(Chapter),"r").readlines()
    for Pages in PageList:
        Page=Pages.replace("\n","")
        print("lets Read {}".format(Page))
        ReadPage(Page)

def ReadNovel(novel):
    NovelName=novel.split(" ")[0]
    print("Lets Read the novel \"{}\"".format(NovelName))
    ChapterList=open("Novels/{}/ChapterIndex.txt".format(NovelName),"r").readlines()
    print("The following is the Chapter list \n {}".format(ChapterList))
    for Chapter in ChapterList:
        Chapter=Chapter.replace("\n","")
        print("Lets begin with chapter \"{}\"".format(Chapter))
        ReadChapter(Chapter)

def ToRead():
    data=open(ToReadFile,"r").readlines()
    for novel in data:
        ReadNovel(novel.replace("\n",""))






ToRead()