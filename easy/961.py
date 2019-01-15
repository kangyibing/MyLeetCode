# -*- coding: UTF-8 -*-
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 解法一
        dic = {} #创建一个字典
        for a in A:
            if a in dic:
                return a
            else:
                dic[a] = 1
        # 解法二
        # A.sort() #默认升序排序
        # for i in range(1,len(A)):
        #     if A[i-1] == A[i]:
        #         return A[i]