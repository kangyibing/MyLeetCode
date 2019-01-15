# -*- coding: UTF-8 -*-
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        alist = []
        alist2 = []
        for i in A:
            if i % 2 == 0:
                alist.append(i)
            else:
                alist2.append(i)
        alist.extend(alist2)# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        return alist