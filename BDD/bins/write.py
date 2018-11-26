import json


def writecode(Fdata,file):
    codefile=open(file,"a+")
    if "driver" in Fdata:
        codefile.write("\ntime.sleep(1)\n")
    for code in Fdata:
        codefile.write(code)
    

def createVariable(lines,Data):
    line=lines.split("(")[1].split(")")[0].split(",")
    k =Data.keys()
    for variable in line:
        for key in k:
            val=Data.get(key)
            val=val.get(variable)
            if "None" not in val:
                 return "{}=\"{}\"".format(variable,val)
        
def writepera(use,Data,file,data):
    try:
        Fdata=data["pera"][use][Data]
        codefile=open(file,"a+")
        print(Fdata)
        for code in Fdata:
            codefile.write("\n")
            codefile.write(code)
            
    except:
        print("fata")

def writeline(use,Data,file):
    Fdata={}
    json_data=open("Data/CreateData.json").read()
    data = json.loads(json_data)
    if Data is None:
        Fdata=data["line"][use]
        writecode(Fdata,file)
        print(Fdata,use,Data,file)
        
    if type(Data) is dict:
        k =Data.keys()
        for key in k:
            try:
                val=Data.get(key)
                val=val.get("url")
                if "None" not in val:
                    Data=val
            except:
                pass

    try:
        Fdata=data["line"][use]
        Fdata=Fdata.replace("variable",Data)
        print(use,Fdata,Data)
        writecode(Fdata,file)
        print(Fdata,use,Data,file)
    except:        
        writepera(use,Data,file,data)
    return Fdata 
        
    