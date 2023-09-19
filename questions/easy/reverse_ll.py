class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Create a variable to hold the reversed LL, and asign the current head to current
        prev, current = None,head

        while current:
            #Create temp variables to store the values and pointer
            nxt = current.next
            
            current.next = prev
            #Swap the values
            prev = current
            # iterate through the forward linked list
            current = nxt
        return prev