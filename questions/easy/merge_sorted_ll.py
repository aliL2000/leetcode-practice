class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #NON-ORIGINAL SOLUTION
        #This solution isn't too optimized.
        # res = ListNode()
        # tail = res

        # while (list1 and list2):
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next

        # #If one of the lists have become empty, just append it to the output
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2

        # return res.next


        head = cur = ListNode()
        while l1 and l2:
            #Initialize two variables to hold the current heads of l1 and l2
            v1 = l1.val
            v2 = l2.val
            #Compare and append the lowest value to the head of the list, it's ascending right?
            if v1 <= v2:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            #Change the head of the output linked list
            cur = cur.next
        #If any of the lists is done, append the other
        cur.next = l1 if l1 else l2
        return head.next