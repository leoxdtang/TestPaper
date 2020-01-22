# -*- coding: utf-8 -*-
"""
Test Paper程序功能：
1.生成n道100内整数加减法试题（不含0）。数字和计算符随机。如果是减法题，答案不为负数 
2.在console显示第一道试题，请求回答。 接受键盘输入作为答案，以回车结束。
3.显示下一道试题， 直至所以试题完成。 所有试题不允许修改答案。 
4.批改试卷
5.在console 输出
    a.试题分数、完成时间， 
    b。每道试题的题干、答案， 是否正确，如果错误则显示正确答案。 
6. 将（5）输出项保存在文件中。

author: Leo Tang
date : 2019.12.14
"""

import Exam

     
# 试卷程序测试
if __name__ == "__main__":
    tp = Exam.Exam(N=10, MAX=99)

    tp.start_test()
    tp.show_exam_info()
    tp.save_file()
    