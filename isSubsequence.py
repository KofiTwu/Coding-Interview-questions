'''
Given two strings s and t, return true if s is a subsequence of t,
or false otherwise.

A subsequence of a string is a new string that is formed from 
the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the 
remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

s = "abc"
t = "ahbgdc"



def isSub(arr, sub):
    arrIdx = 0
    subIdx = 0
    while arrIdx < len(arr):
        if sub[subIdx] == arr[arrIdx]:
            subIdx += 1
        arrIdx += 1
    return subIdx == len(sub)
    

#print(isSub(t, s))