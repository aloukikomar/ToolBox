import json
from bins.write import writeline


def formdata(use,Data,Flag):
    writeline(use,Data,"tmp/execute.py")
    

def fetchdata(Data,IncludeData,lookfor):
    for DataSet in IncludeData:
        try:
            return Data[DataSet][lookfor]
        except:
            pass
        

def accureData(Site,includs):
    Fdata={}
    for dataSource in includs:
        
        json_data=open("Data/{}".format(dataSource)).read()
        data = json.loads(json_data)
        Fdata[dataSource]=data[Site]
    return Fdata 

def convert(Story):
    includs=[]
    for lines in Story:
        line=lines.replace("\n","")

        if "include" in line:
            IncludeData=line.split(" ")[1].split(",")
            print(IncludeData)
            file=open("tmp/execute.py","a+")
            file.write("\ntime.sleep(5)\n")
            file.close()
            if "And" not in line :
                formdata("include",IncludeData,1)

        if "test" in line:
            DriverType=line.split(" ")[1]
            print(DriverType)
            if "And" not in line :
                formdata("test",DriverType,1)


        if "open" in line:
            Site=line.split(" ")[1]
            Data=accureData(Site,IncludeData)
            with open('tmp/Data.json', 'w') as fp:
                json.dump(Data, fp)
            if "And" not in line :
                formdata("open",Data,1)


        if "LookFor" in line:
            lookfor=line.split(" ")[1]
            xpathforelement=fetchdata(Data,IncludeData,lookfor)
            if "And" not in line :
                formdata("LookFor",xpathforelement,1)


        if "Enter" in line:
            Enter=line.split("Enter")[1].split(" ")[1]
            Details=fetchdata(Data,IncludeData,Enter)
            if "And" not in line :
                formdata("Enter",Details,1)
        
        if "Click" in line:
            '''Click=line.split("Click")[1].split(" ")[1]'''
            Details=fetchdata(Data,IncludeData,"Click")
            if "And" not in line :
                formdata("Click",Details,1)

        if "Start" in line:
            file=open("tmp/execute.py","w")
            file.write("import time")
            file.close()

        if "Continue" in line:
            with open('tmp/Data.json', 'r') as fp:
                Data=json.load(fp)
            print("Continue with Data {}".format(Data))