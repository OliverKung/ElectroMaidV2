from operator import mod
import pandas as pd
global database
database=pd.read_excel("./InCase.xlsx", "List")

def whereis(modelNumber:str):
    number_of_stock=0
    for index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            print("there is "+str(row["数量"])+" "+row["型号"]+" loacte at "+row["位置编号"]+" of "+row["元件盒编号"])
            number_of_stock=number_of_stock+1
    if(number_of_stock==0):
        print("\033[1mThere is no "+modelNumber+" in stock\033[0m")
    return number_of_stock

def newchip(modelNumber,package,quantity,location,caseNumber,sale="",saleNumber="",description=""):
    global database
    case_of_stock=0
    current_stock=[]
    stock_index=[]
    for row_index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            current_stock.append(row["数量"])#包含型号的格的数量
            stock_index.append(row_index)#包含型号的格的index
            case_of_stock=case_of_stock+1
    if case_of_stock==0:
        dataframe_to_add=pd.DataFrame([[modelNumber,package,sale,saleNumber,quantity,caseNumber,location,description]],\
            columns=['型号','封装','销售代理','销售商编号','数量','元件盒编号','位置编号',"描述"])
        database=pd.concat([database,dataframe_to_add]).reset_index(drop=True)
        database.to_excel("./InCase.xlsx", "List",index=False)
    else:
        print('There is already '+modelNumber+" in stock,please use add command")

def takechip(modelNumber:str,takenumber):
    global database
    case_of_stock=0
    current_stock=[]
    name_stock=[]
    location_stock=[]
    caseNumber_stock=[]
    stock_index=[]
    for row_index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            current_stock.append(row["数量"])#包含型号的格的数量
            stock_index.append(row_index)#包含型号的格的index
            case_of_stock=case_of_stock+1

    if case_of_stock==0:
        # no stock return falut
        print("There is no "+modelNumber+" in stock")
        return 0
    elif case_of_stock==1:
        database.iloc[stock_index[0],4]=current_stock[0]-takenumber
        if(current_stock[0]-takenumber<=0):
            print("run out of stock of "+modelNumber)
        else:
            database.to_excel("./InCase.xlsx", "List",index=False)
            print("Take "+str(takenumber)+" "+database["型号"][stock_index[0]]+" from "+database["位置编号"][stock_index[0]]+" of "+database["元件盒编号"][stock_index[0]])
            print("There are "+str(database["数量"][stock_index[0]])+" left")
            # quantity minus take number and save
            # database.
        return 1
    else:
        print("more than one stock is found")
        for index in stock_index:
            print(database[index:index+1])
        print("Which one do you wanna take?")
        select_index=input()
        database.iloc[int(select_index),4]=current_stock[stock_index.index(int(select_index))]-takenumber
        if(current_stock[stock_index.index(int(select_index))]-takenumber<=0):
            print("run out of stock of "+modelNumber)
        else:
            print("Take "+str(takenumber)+" "+database["型号"][int(select_index)]+" from "+database["位置编号"][int(select_index)]+" of "+database["元件盒编号"][int(select_index)])
            print("There are "+str(database["数量"][int(select_index)])+" left")
            database.to_excel("./InCase.xlsx", "List",index=False)

def addchip(modelNumber,addnumber):
    global database
    case_of_stock=0
    current_stock=[]
    stock_index=[]
    for row_index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            current_stock.append(row["数量"])#包含型号的格的数量
            stock_index.append(row_index)#包含型号的格的index
            case_of_stock=case_of_stock+1

    if case_of_stock==0:
        # no stock return falut
        print("There is no "+modelNumber+" in stock, please use new chip command")
        return 0
    elif case_of_stock==1:
        database.iloc[stock_index[0],4]=current_stock[0]+addnumber
        database.to_excel("./InCase.xlsx", "List",index=False)
        print("Add "+str(addnumber)+" "+database["型号"][stock_index[0]]+" from "+database["位置编号"][stock_index[0]]+" of "+database["元件盒编号"][stock_index[0]])
        print("There are "+str(database["数量"][stock_index[0]])+" left")
        # quantity minus take number and save
        # database
        return 1
    else:
        print("more than one stock is found")
        for index in stock_index:
            print(database[index:index+1])
        print("Which one do you wanna take?")
        select_index=input()
        database.iloc[int(select_index),4]=current_stock[stock_index.index(int(select_index))]+addnumber
        print("Add "+str(addnumber)+" "+database["型号"][int(select_index)]+" from "+database["位置编号"][int(select_index)]+" of "+database["元件盒编号"][int(select_index)])
        print("There are "+str(database["数量"][int(select_index)])+" left")
        database.to_excel("./InCase.xlsx", "List",index=False)

def askchip(modelNumber:str):
    for row_index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            print(row["型号"]+" is "+row["描述"])


if __name__=="__main__":
    addchip("388", 2)