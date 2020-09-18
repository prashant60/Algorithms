class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.head=None
        self.head1=None
        self.head2=None

    def create1(self,data):
        if self.head1==None:
            self.head1=Node(data)
            return
        curr=self.head1
        while(curr.next):
            curr=curr.next
        curr.next=Node(data)

    def create2(self,data):
        if self.head2==None:
            self.head2=Node(data)
            return
        curr=self.head2
        while(curr.next):
            curr=curr.next
        curr.next=Node(data)

    def printlist(self):
        curr=self.head
        while curr.next:
            print(curr.data, end=" --> ")
            curr=curr.next
        print(curr.data)

    def mergeList(self):
        if self.head1==None:
            self.head=self.head2
        elif self.head2==None:
            self.head=self.head1
        else:
            curr1=self.head1
            curr2=self.head2
            
            while curr1!=None and curr2!=None:
                if self.head==None:
                    if curr1.data<=curr2.data:
                        self.head=Node(curr1.data)
                        curr1=curr1.next
                    else:
                        self.head=Node(curr2.data)
                        curr2=curr2.next
                    curr=self.head
                    
                else:
                    if curr1.data<=curr2.data:
                        curr.next=Node(curr1.data)
                        curr1=curr1.next
                    else:
                        curr.next=Node(curr2.data)
                        curr2=curr2.next
                    curr=curr.next
            if curr1==None and curr2!=None:
                curr.next=curr2
            elif curr1!=None and curr2==None:
                curr.next=curr1
            else:
                return self.head



linked=Linked()
linked.create1(5)
linked.create1(7)
linked.create1(9)
linked.create1(35)
linked.create1(59)
linked.create1(544)

linked.create2(5)
linked.create2(6)
linked.create2(7)
linked.create2(59)
linked.create2(560)

linked.mergeList()

linked.printlist()
