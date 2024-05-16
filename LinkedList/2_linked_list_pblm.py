class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def pop_first(self):
        popped_node = self.head
        if self.head is None:
            return None 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        current = self.head
        while current.next is not popped_node:
            current = current.next
        current.next = None
        self.tail = current
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def reverse(self):
        prev_node = None 
        current_node = self.head 
        while current_node is not None:
            next_node = current_node.next 
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node 
        self.head, self.tail = self.tail, self.head

    def find_middle(self):
        index = int(self.length / 2)
        if self.length % 2 == 0:
            middle_node = self.get(index-1)
            return middle_node.value + middle_node.next.value
        else:
            return self.get(index).value
        
    def remove_deuplicates(self):
        if self.head is None:
            return
        node_values = set()
        current_node = self.head 
        node_values.add(current_node.value)
        while current_node.next is not None:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next 
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

linkedlist = LinkedList()
linkedlist.append(10)
linkedlist.append(20)
linkedlist.append(30)
linkedlist.append(20)
print(linkedlist)
print(linkedlist.remove_deuplicates())
print(linkedlist)
