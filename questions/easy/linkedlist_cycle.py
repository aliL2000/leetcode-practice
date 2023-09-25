#Question can be found here:
#https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        result = set()
        while head:
            if head in result:
                return True
            else:
                result.add(head)
            head = head.next
        return False