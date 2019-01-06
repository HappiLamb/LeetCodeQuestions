""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. """

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carryOver = False
        beginNode = None
        currNode = None
        while (True):
            currValue = 0
            #EDGE: Checks if there is a carry over and there is no other values in l1 and l2
            if l1 == None and l2 == None and not carryOver:
                break
            elif l1 == None and l2 == None and carryOver:
                tmp = ListNode(1)
                currNode.next = tmp
                currNode = tmp
                break
                
            #If there is carry over increase by 1
            if carryOver:
                carryOver = False
                currValue += 1
                
            if l1 != None:
                currValue += l1.val
            if l2 != None:
                currValue += l2.val
                
            #Checks for carryover and removes 10 from current value
            if currValue >= 10:
                carryOver = True
                currValue -= 10
            
            #Repositions curr node to the newest one
            if beginNode == None:
                beginNode = ListNode(currValue)
                currNode = beginNode
            else:
                tmp = ListNode(currValue)
                currNode.next = tmp
                currNode = tmp
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return beginNode
            