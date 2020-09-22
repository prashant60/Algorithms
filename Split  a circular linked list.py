class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.head=None
        
    def create(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
            return
        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=Node(data)
            curr.next.next=self.head

    def split(self):
        slow=self.head
        fast=self.head.next

        while fast.next!=self.head:
            slow=slow.next
            if fast.next.next!=self.head:
                fast=fast.next.next
            else:
                fast=fast.next
        head2=slow.next
        fast.next=head2
        slow.next=self.head

        return self.head,head2

    
    def print(self,head):
        if head is None:
            return
        curr=head
        while curr.next!=head:
            print(curr.data,end=" --> ")
            curr=curr.next
        print(curr.data)

        
link=Linked()
link.create(10)
link.create(15)
link.create(12)
link.create(13)
link.create(20)
#link.create(14)

link.print(link.head)

x,y=link.split()
link.print(x)
link.print(y)



