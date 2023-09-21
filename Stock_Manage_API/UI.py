import ERP
import os

def take_a_chip():
    while True:
        print("Now is \033[1mtake mode\033[0m,input you command,type exit to exit")
        print("\033[7mwhere\033[0m to find stock,\033[7mtake\033[0m to take chip from stock")
        command=input()
        if(command.find("exit")!=-1):
            os.system("clear")
            break
        if(command.casefold().startswith("where")==True):
            while(True):
                modelNumber=input("Enter the model number you want to find\r\n")
                os.system("clear")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                ERP.whereis(modelNumber)
        if(command.casefold().startswith("take")==True):
            while(True):
                modelNumber=input("Which part you wanna take?\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                takenumber=input("How many chips do you wanna take?\r\n")
                os.system("clear")
                ERP.takechip(modelNumber, int(takenumber))
        if(command.casefold().startswith("what")==True):
            while(True):
                modelNumber=input("Which part you wanna ask?\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                os.system("clear")
                ERP.askchip(modelNumber)


def add_a_chip():
    while True:
        print("Now is \033[1madd mode\033[0m,input you command,type exit to exit")
        print("\033[7madd\033[0m to add stock,\033[7mnew\033[0m to new inventory")
        command=input()
        if(command.find("exit")!=-1):
            os.system("clear")
            break
        if(command.casefold().startswith("add")==True):
            while(True):
                
                modelNumber=input("Which part you wanna add?\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                addnumber=input("How many chips do you wanna add?\r\n")
                os.system("clear")
                ERP.addchip(modelNumber, int(addnumber))

        if(command.casefold().startswith("new")==True):
            while(True):
                modelNumber=input("\033[7mModel Number?\033[0m\r\n")
                if(modelNumber=="exit"):
                    os.system("clear")
                    break
                package=input("\033[7mPackage?\033[0m\r\n")
                sale=input("\033[7mSale?\033[0m\r\n")
                if(sale!=""):
                    saleNumber=input("\033[7mSale Number?\033[0m\r\n")
                else:
                    saleNumber=""
                quantity=input("\033[7mQuantity?\033[0m\r\n")
                caseNumber=input("\033[7mCase Number?\033[0m\r\n")
                location=input("\033[7mLocation?\033[0m\r\n")
                description=input("\033[7mDesctiption?\033[0m\r\n")
                ERP.newchip(modelNumber, package, int(quantity), location, caseNumber,sale,saleNumber,description)
                os.system("clear")
                
if __name__=="__main__":
    os.system("clear")
    print("Welcome to CompomentCase V1")
    print("Please input you command,do you wanna take a chip or add a chip? T for Take and A for Add")
    take_or_add=input()
    if(take_or_add.casefold().startswith("t")==True or take_or_add.casefold().find("take")!=-1):
        os.system("clear")
        take_a_chip()
    if(take_or_add.casefold().startswith("a")==True or take_or_add.casefold().find("add")!=-1):
        os.system("clear")
        add_a_chip()