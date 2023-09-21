class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        tail = res

        while (list1 and list2):
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        #If one of the lists have become empty, just append it to the output
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return res.next