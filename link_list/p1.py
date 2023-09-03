class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return self.val


class Linklist:
    def __init__(self):
        self.head = self.tail = None 
        self._size = 0

    def __str__(self):
        final_string = ''
        current_node = self.head
        while current_node :
            final_string += str(current_node.val)
            if current_node.next != None :
                final_string += ' <- '
            current_node = current_node.next   
        return final_string

    def size(self):
        return self._size
    
    def addHead(self,val):
        self._size += 1
        new_Node = Node(val)
        new_Node.next = self.head
        self.head = new_Node

    def append(self,val):
        self._size += 1
        new_Node = Node(val)
        if self.head is None:
            self.head = new_Node
        else:
            current_node = self.head
            while current_node.next :
                current_node = current_node.next
            current_node.next = new_Node
            self.tail = new_Node
    
    def search(self,val):
        current_node = self.head
        if self.isEmpty():
            return 'Not Found'
        while current_node.next :
            if current_node.val == val:
                return 'Found'
            current_node = current_node.next
        if current_node.val == val:
            return 'Found'
        return 'Not Found'

    def isEmpty(self):
        return self.head == None

    def delete_head(self):
        self._size -= 1
        self.head = self.head.next
        
    def delete_tail(self):
        self._size -= 1
        current_node = self.head
        while current_node.next.next :
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
    
    def delete_node(self,val):
        self._size -= 1 
        current_node = self.head
        while current_node.next :
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            current_node = current_node.next
    

print(' *** Locomotive ***')
l = Linklist()
inp = list(input('Enter Input : ').split())
for i in inp:
    l.append(i)
print(f'Before : {l}')
while int(l.head.val) != 0:
    l.append(l.head)
    l.head = l.head.next
print(f'After : {l}')

'''

มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)

 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1


 *** Locomotive ***
Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3

 *** Locomotive ***
Enter Input : 1 0
Before : 1 <- 0
After : 0 <- 1

 *** Locomotive ***
Enter Input : 5 4 3 2 1 0 9 8 7 6
Before : 5 <- 4 <- 3 <- 2 <- 1 <- 0 <- 9 <- 8 <- 7 <- 6
After : 0 <- 9 <- 8 <- 7 <- 6 <- 5 <- 4 <- 3 <- 2 <- 1


 *** Locomotive ***
Enter Input : 0 1 2 3 4 5 6 7 8 9
Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9

 *** Locomotive ***
Enter Input : 2 0 1
Before : 2 <- 0 <- 1
After : 0 <- 1 <- 2
'''