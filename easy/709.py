# -*- coding: UTF-8 -*-
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #解法一
        # str=str.lower()
        # return str
        #解法二
        n=len(str)
        temp=list(str) # list()方法用于将元组或字符串转换为列表
        for i in range(n):
            if temp[i]>='A' and temp[i]<='Z':
                x= ord(temp[i])+32 # ord()返回对应字符的 ASCII 数值
                temp[i]=chr(x) # chr()返回当前整数对应的ascii字符
        return ''.join(temp) #join()返回通过指定字符连接序列中元素后生成的新字符串