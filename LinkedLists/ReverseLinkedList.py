class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
         
    head = prev
    return head

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        if head.next:
            res.append("->")
        head = head.next
        
    return ''.join(res)
        


linkedList = ListNode(0)
linkedList.next = ListNode(1)
linkedList.next.next = ListNode(2)
linkedList.next.next.next = ListNode(3)

print(print_list(linkedList.next))
linkedList.next = reverse(linkedList.next)
print(print_list(linkedList.next))
#(reversed.val)