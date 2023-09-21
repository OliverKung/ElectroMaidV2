from operator import truediv
import ERPcn as ERP
import os

def take_a_chip():
    while True:
        print("现在是\033[1mtake 模式\033[0m,输入 exit 可推出当前模式")
        print("\033[7mwhere\033[0m指令查询库存位置,\033[7mtake\033[0m指令取用库存")
        print("\033[7mwhat\033[0m指令查询库存功能")
        command=input()
        if(command.find("exit")!=-1):
            os.system("clear")
            break
        if(command.casefold().startswith("where")==True):
            while(True):
                modelNumber=input("输入你想要查询的型号\r\n")
                os.system("clear")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                ERP.whereis(modelNumber)
        if(command.casefold().startswith("take")==True):
            while(True):
                modelNumber=input("你想要取用哪个型号？\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                
                takenumber=input("你想要取用多少片？\r\n")
                while(takenumber.isdigit()!=True):
                    print("你输入的数量不是数字，请重新输入")
                    takenumber=input("\033[7m数量?\033[0m\r\n")
                os.system("clear")
                ERP.takechip(modelNumber, int(takenumber))
        if(command.casefold().startswith("what")==True):
            while(True):
                modelNumber=input("你想问什么芯片？\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                os.system("clear")
                ERP.askchip(modelNumber)


def add_a_chip():
    while True:
        print("现在是\033[1madd 模式\033[0m,输入exit指令以推出当前模式")
        print("\033[7madd\033[0m指令可以填补库存，\033[7mnew\033[0m指令可以新建库存")
        command=input()
        if(command.find("exit")!=-1):
            os.system("clear")
            break
        if(command.casefold().startswith("add")==True):
            while(True):
                
                modelNumber=input("你想要填补什么型号？\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                addnumber=input("你想要填补多少片？\r\n")
                while(addnumber.isdigit()!=True):
                    print("你输入的数量不是数字，请重新输入")
                    addnumber=input("\033[7m数量?\033[0m\r\n")
                os.system("clear")
                ERP.addchip(modelNumber, int(addnumber))

        if(command.casefold().startswith("new")==True):
            while(True):
                modelNumber=input("\033[7m型号？\033[0m\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                package=input("\033[7m封装？\033[0m\r\n")
                sale=input("\033[7m经销商?\033[0m\r\n")
                if(sale!=""):
                    saleNumber=input("\033[7m经销商编号?\033[0m\r\n")
                else:
                    saleNumber=""
                quantity=input("\033[7m数量?\033[0m\r\n")
                while(quantity.isdigit()!=True):
                    print("你输入的数量不是数字，请重新输入")
                    quantity=input("\033[7m数量?\033[0m\r\n")
                caseNumber=input("\033[7m盒编号?\033[0m\r\n")
                location=input("\033[7m位置?\033[0m\r\n")
                description=input("\033[7m描述?\033[0m\r\n")
                ERP.newchip(modelNumber, package, int(quantity), location, caseNumber,sale,saleNumber,description)
                os.system("clear")
                
if __name__=="__main__":
    os.system("clear")
    print("可能还挺好用的元件盒V1")
    print("你想要拿片子走还是放片子进来？A代表放片子进来，T代表把片子拿走")
    take_or_add=input()
    if(take_or_add.casefold().startswith("t")==True or take_or_add.casefold().find("take")!=-1):
        os.system("clear")
        take_a_chip()
    if(take_or_add.casefold().startswith("a")==True or take_or_add.casefold().find("add")!=-1):
        os.system("clear")
        add_a_chip()