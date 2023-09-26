


class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        l2 = []
        #Append values from each LL to a list of integers
        while list1 or list2:
            if list1:
                l1.append(list1.val)
                list1 = list1.next
            if list2:
                l2.append(list2.val)
                list2 = list2.next
        
        reverse_int = int("".join(map(str, l1[::-1])))+int("".join(map(str, l2[::-1])))
        reverse = [int(x) for x in str(reverse_int)]
        #Combine and reverse the sum of the two int arrays, and attempt to create LL of those reversed int values from the sum
        dummy = ListNode
        for num in reverse[::-1]:
            dummy.val = num
            dummy.next = ListNode(num)
            dummy = dummy.next

        #Above is where the error begins to start, I cannot even start making this smh
        return dummy.next