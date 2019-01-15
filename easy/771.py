# -*- coding: UTF-8 -*-
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str 宝石
        :type S: str 拥有的石头
        :rtype: Return type int 
        """
        n=0
        for i in J: 
            n+=S.count(i) #该方法返回i在S中出现的次数
        return n