class Solution:
    def middle_element(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
# Example usage:
if __name__=="__main__":
    sol=Solution()
    # Creating a linked list: 1 -> 2 -> 3  -> None
    class ListNode:
        def __init__(self,value=0,next=None):
            self.value=value
            self.next=next
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    # head.next.next.next=ListNode(4)
    # Finding the middle element    middle_node=sol.middle_element(head)
    middle_element=sol.middle_element(head)

    print("Middle element:", middle_element.value)
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are using only a constant amount of extra space
# 