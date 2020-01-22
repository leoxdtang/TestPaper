# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:47:11 2020

@author: leotang

实现加减法试题类
1. 题干， 答案，回答，是否正确
2. 判断是否正确
3. 形成字符串，用于输出

"""
import random

class ArithmeticItem:
    def __init__(self,MAX):
         # 1.试题列表（题干，答案，回答，是否正确），
         self.MAX_INT = MAX
         self.operator = random.choice(['-','+'])
         self.expression = [random.randint(1,self.MAX_INT),random.randint(1,self.MAX_INT)]         
         self.answer = None
         self.is_correct =  None

         if self.operator == '-':
             self.expression = [max(self.expression),min(self.expression)]
    
    def set_answer(self,answer):
        self.answer = answer
        self.judge()
    
    def calculate(self):
        if self.operator == '-':
            return self.expression[0] - self.expression[1]
        elif self.operator == '+':
            return self.expression[0] + self.expression[1]
         
    def judge(self):
        if self.answer is None:
            self.is_correct =  None
        else:
            self.is_correct = (self.answer ==  self.calculate())
            
    
    def __str__(self):
        base_expr = "{0} {1} {2} = ".format(self.expression[0],self.operator,self.expression[1])
              
        if self.is_correct is None:
            return base_expr
        elif self.is_correct == True :
            addition_expr = str(self.answer) + " 正确"
            return base_expr + addition_expr
        elif self.is_correct == False :
            addition_expr = str(self.answer) + " 错误。正确答案是{0}".format(self.calculate())
            return base_expr + addition_expr    



# Test ArithmeticItem
            
# item = ArithmeticItem(99)
# print(item)
# item.set_answer(55)
# print(item)
# item.set_answer(item.calculate())
# print(item)
