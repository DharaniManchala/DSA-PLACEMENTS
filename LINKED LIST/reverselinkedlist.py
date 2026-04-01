class Solution:
    def reverse_linkedlist(self,head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
# Example usage:
if __name__=="__main__":
    sol=Solution()
    # Creating a linked list: 1 -> 2 -> 3 -> None
    class ListNode:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # Reversing the linked list
    new_head = sol.reverse_linkedlist(head)
    # Printing the reversed linked list: 3 -> 2 -> 1 -> None
    current = new_head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are using only a constant amount of extra space

                  