# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:46:45 2020

@author: yanyu
"""

from datetime import datetime, timedelta
import os,sys
import ArithmeticItem


class Exam:
     def __init__(self,N,MAX):
         # 1.试题数目，2.开始时间/结束时间，3. 分数 4.试题列表（题干，答案，回答，是否正确），
         self.n_item = N
         self.start_time = None
         self.end_time = None
         self.score = None
         self.lst_items = []
         for i in range(self.n_item):
             self.lst_items.append(ArithmeticItem.ArithmeticItem(MAX))
         
     def show_exam_info(self):
         os.system("cls")
         # number of test items
         print("答题数:{}".format(self.n_item))
     
        #start time and end time, duration
         if self.start_time != None and self.end_time != None:
             print('-'*30)
             print("开始时间:{}".format(self.start_time))
             print("结束时间:{}".format(self.end_time))           
             print("用时 :{} 秒".format((self.end_time-self.start_time).seconds))  
             
        #score
         if self.score != None:
             print('-'*30)
             print("得分:{}".format(self.score))
        
        #detail items 
         print('-'*30)
         for i in self.lst_items:
             print(i)
        
     def start_test(self):
         self.start_time = datetime.now()
         for i in self.lst_items:
             print(i)
             input_raw = input("请输入答案(quit退出游戏):")
             if input_raw.upper() in ["QUIT","Q"]:
                 sys.exit(0)    
             elif input_raw.isdigit():
                 i.set_answer(int(input_raw))
             else:
                 i.set_answer(-1)
             
             
         self.end_time = datetime.now()
         
         # 计算得分
         n_correct = 0 
         for i in self.lst_items:
             n_correct += i.is_correct
         self.score = round(n_correct*100/self.n_item,0)
         return None
         
     def save_file(self):
        if self.score is None: 
            return None
        
        fn = str(datetime.now().strftime("%Y%m%d_%H%M%S")) +".txt"
        report = ["答题数:{}".format(self.n_item)+'\n',
                  "用时 :{} 秒".format((self.end_time-self.start_time).seconds)+'\n',
                  "得分:{}".format(self.score)+'\n']
        
        
        with open(fn,'w') as f:
            f.writelines(report)
            for i in self.lst_items:
                f.writelines(str(i)+'\n')
        
        return None
     
# tp = Exam(N=3, MAX=99)
# tp.start_test()
# tp.show_exam_info()

# tp.save_file()



