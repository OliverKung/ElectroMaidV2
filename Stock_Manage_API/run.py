import os

if __name__ == "__main__":
    choose=input("中文输入ch，For English please type \"en\"\r\n")
    if(choose.find("ch")!=-1):
        os.system("python UI_cn.py")
    else:
        os.system("python UI.py")
