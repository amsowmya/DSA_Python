class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class LinkedList():
    def __init__(self):
        self.head=None 
        
    def print(self):
        llstr=''
        itr=self.head
        while itr:
            llstr += str(itr.data) + "-->"
            itr=itr.next 
            
        print(llstr)
        
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next 
        return count
        
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head=node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr=self.head 
        while itr.next:
            itr=itr.next 
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
            
        count=0
        itr=self.head 
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1
                
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        count = 0
        itr = self.head 
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next 
            count += 1
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["hi", "how", "are", "you"])
    ll.insert_at(2, "king")
    ll.remove_at(3)
    ll.print()
    print("length: " , ll.get_length())