from operator import truediv
import os,sys
sys.path.append('./Stock_Manage_API')
import UI_cn
if __name__=="__main__":
    while(True):
        os.system("cls")
        print("给电子工程师的赛博女仆 V1P0")
        print("功能列表")
        print("\t1.测试助手\n\t2.焊接辅助\n\t3.计算辅助\n\t4.X-RAY\n\t5.元件追踪\n\t6.元件分类\n\t7.库存管理")
        mode_str = input("选择功能：")
        if(mode_str == "3"):
            break
        if(mode_str == "exit"): 
            break
        if(mode_str == "7"):
            UI_cn.run()
        