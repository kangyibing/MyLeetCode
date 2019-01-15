# -*- coding: UTF-8 -*-
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = A[i][j]^1# 按位异或运算符：当两对应的二进位相异时，结果为1
            A[i] = A[i][::-1]
        return A