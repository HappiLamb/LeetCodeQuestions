""" Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring. """

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        pt1 = 0
        hashAlpha = {}
        hadDupe = False
        #Catches the case if its one there cannot be any dupes thus it is 1
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            if s[i] in hashAlpha:
                hashAlpha[s[i]].append(i)
                #Only set the pointer if the duplicate was after the current pointers position
                if hashAlpha[s[i]][len(hashAlpha[s[i]]) - 2] > pt1:
                    pt1 = hashAlpha[s[i]][len(hashAlpha[s[i]]) - 2]
                hadDupe = True
            else:
                hashAlpha[s[i]] = [i]
                
            #Checks for dupes if it hasnt had one then it just counts from the current position
            if hadDupe:
                if i - pt1 > maxLen:
                    maxLen = i - pt1
            else:
                if i + 1 > maxLen:
                    maxLen = i + 1
            
        return maxLen                