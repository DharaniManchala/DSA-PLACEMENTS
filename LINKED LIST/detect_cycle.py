class Solution:
    def detect_cycle(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
# Example usage:
if __name__=="__main__":
    sol=Solution()
    # Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
    class ListNode:
        def __init__(self,value=0,next=None):
            self.value=value
            self.next=next
    head=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node4=ListNode(4)
    head.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node2  # Creates a cycle
    # Detecting the cycle
    has_cycle=sol.detect_cycle(head)
    print("Cycle detected:", has_cycle)

    # time complexity: O(n) where n is the number of nodes in the linked list
    # space complexity: O(1) since we are using only a constant amount of extra