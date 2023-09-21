from operator import mod
import pandas as pd
global database
database=pd.read_excel("./InCase.xlsx", "List")

def whereis(modelNumber:str):
    number_of_stock=0
    for index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            print("有"+str(row["数量"])+"个"+row["型号"]+"在"+row["元件盒编号"]+"的"+row["位置编号"])
            number_of_stock=number_of_stock+1
    if(number_of_stock==0):
        print("\033[1m库存里没有"+modelNumber+"\033[0m")
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
        print('库存里已经有'+modelNumber+"了，请添加库存(使用Add指令)")

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
        print("\033[1m库存里没有"+modelNumber+"\033[0m")
        return 0
    elif case_of_stock==1:
        database.iloc[stock_index[0],4]=current_stock[0]-takenumber
        if(current_stock[0]-takenumber<=0):
            print(modelNumber+"用完了")
        else:
            database.to_excel("./InCase.xlsx", "List",index=False)
            print("从"+database["元件盒编号"][stock_index[0]]+"的"+database["位置编号"][stock_index[0]]+"拿了"+str(takenumber)+"片"+database["型号"][stock_index[0]])
            print("库存里还有"+str(database["数量"][stock_index[0]]))
            # quantity minus take number and save
            # database.
        return 1
    else:
        print("查到了不止一个库存")
        for index in stock_index:
            print(database[index:index+1])
        print("你想要拿走哪个？")
        select_index=input()
        database.iloc[int(select_index),4]=current_stock[stock_index.index(int(select_index))]-takenumber
        if(current_stock[stock_index.index(int(select_index))]-takenumber<=0):
            print(modelNumber+"用完了")
        else:
            # print("Take "+str(takenumber)+" "+database["型号"][int(select_index)]+" from "+database["位置编号"][int(select_index)]+" of "+database["元件盒编号"][int(select_index)])
            # print("There are "+str(database["数量"][int(select_index)])+" left")
            print("从"+database["元件盒编号"][int(select_index)]+"的"+database["位置编号"][int(select_index)]+"拿了"+str(takenumber)+"片"+database["型号"][int(select_index)])
            print("库存里还有"+str(database["数量"][int(select_index)]))
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
        print("库存里没有"+modelNumber+"，请新建一个")
        return 0
    elif case_of_stock==1:
        database.iloc[stock_index[0],4]=current_stock[0]+addnumber
        database.to_excel("./InCase.xlsx", "List",index=False)
        print("向"+database["元件盒编号"][stock_index[0]]+"的"+database["位置编号"][stock_index[0]]+"填补了"+str(addnumber)+"片"+database["型号"][stock_index[0]])
        print("现在有"+str(database["数量"][stock_index[0]])+"片")
        # quantity minus take number and save
        # database
        return 1
    else:
        print("找到了不止一个库存")
        for index in stock_index:
            print(database[index:index+1])
        print("你想要填补哪个？")
        select_index=input()
        database.iloc[int(select_index),4]=current_stock[stock_index.index(int(select_index))]+addnumber
        # print("Add "+str(addnumber)+" "+database["型号"][int(select_index)]+" from "+database["位置编号"][int(select_index)]+" of "+database["元件盒编号"][int(select_index)])
        # print("There are "+str(database["数量"][int(select_index)])+" left")
        print("向"+database["元件盒编号"][int(select_index)]+"的"+database["位置编号"][int(select_index)]+"填补了"+str(addnumber)+"片"+database["型号"][int(select_index)])
        print("现在有"+str(database["数量"][int(select_index)])+"片")
        database.to_excel("./InCase.xlsx", "List",index=False)

def askchip(modelNumber:str):
    for row_index,row in database.iterrows():
        if(row["型号"].casefold().find(modelNumber.casefold())!=-1):
            print(row["型号"]+"是"+row["描述"])


if __name__=="__main__":
    addchip("388", 2)