class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s
    
    def isEmpty(self):
        return self.head == None
         
    def Insert2(self,item):
        new_node = Node(item)
        new_cursor = Node('|')
        if self.isEmpty():
            self.head = new_node
            self.tail = new_cursor
            self.tail.previous = new_node
            self.head.next = self.tail
            
        elif self.tail.value == '|':
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            current_node = self.head
            while current_node.next :
                if current_node.next.value == '|':
                    current_node.next.next.previous = current_node
                    current_node.next = current_node.next.next
                current_node = current_node.next
            new_cursor = Node('|')
            new_cursor.previous = self.tail
            self.tail.next = new_cursor
            self.tail = new_cursor
            
        else:
            current_node = self.head
            while current_node.next :
                if current_node.next.value == '|':
                    new_node.next = current_node.next
                    new_node.previous = current_node
                    current_node.next = new_node
                    current_node.next.next.previous = new_node
                    break
                current_node = current_node.next    
                        
    def swap(self, x, y):
        # print('Before : ',end='')
        # print(f'HEAD:{self.head} <---------> TAIL:{self.tail}')
        # self.PrintAll()
        # Edge Cases
        if self.head == None or self.head.next == None or x == y:
            return
 
        # Finding the Nodes
        Node1 = x
        Node2 = y
 
        if Node1 == self.head:
            self.head = Node2
        elif Node2 == self.head:
            self.head = Node1
        if Node1 == self.tail:
            self.tail = Node2
        elif Node2 == self.tail:
            self.tail = Node1

        # Swapping Node1 and Node2
        temp = Node1.next
        Node1.next = Node2.next
        Node2.next = temp
 
        if Node1.next != None:
            Node1.next.previous = Node1
        if Node2.next != None:
            Node2.next.previous = Node2
 
        temp = Node1.previous
        Node1.previous = Node2.previous
        Node2.previous = temp
 
        if Node1.previous != None:
            Node1.previous.next = Node1
        if Node2.previous != None:
            Node2.previous.next = Node2
            
        # print('After : ',end='')
        # print(f'HEAD:{self.head} <---------> TAIL:{self.tail}')
        # self.PrintAll()
        
    def shiftleft(self):
        cursor = self.head
        if self.isEmpty() or self.head.value == '|':
            return
        elif self.tail.value == '|':
            self.swap(self.tail,self.tail.previous)
        else:
            while cursor.next :
                if cursor.next.value == '|':
                    self.swap(cursor,cursor.next)
                cursor = cursor.next
            
    def shiftright(self):
        cursor = self.head
        if self.isEmpty() or self.tail.value == '|':
            return
        elif self.head.value == '|':
            self.swap(self.head,self.head.next)
        
        else:
            while cursor :
                if cursor.value == '|':
                    self.swap(cursor.next,cursor)
                cursor = cursor.next
            
    def deleteleftCursor(self):
        cursor = self.head
        if self.isEmpty() or self.head.value == '|':
            return 
        elif self.head.next.value == '|':
            self.head = self.head.next
            self.head.previous = None
        else:
            while cursor.next.next:
                if cursor.next.next.value == '|':
                    cursor.next.next.previous = cursor
                    cursor.next = cursor.next.next
                    break
                cursor = cursor.next

    def deleterightCursor(self):
        cursor = self.head
        if self.isEmpty() or self.tail.value == '|':
            return 
        elif self.tail.previous.value == '|':
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            while cursor:
                if cursor.value == '|':
                    cursor.next.next.previous = cursor
                    cursor.next = cursor.next.next
                    break
                cursor = cursor.next
    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    c = i.split()
    if c[0] == 'I':
        L.Insert2(c[1])
    elif c[0] == 'L':
        L.shiftleft()
    elif c[0] == 'R':
        L.shiftright()
    elif c[0] == 'B':
        L.deleteleftCursor()
    elif c[0] == 'D':
        L.deleterightCursor()
    # print(i)
    # print(f'Link -> {L}')
    # print(f'Reverse -> {L.reverse()}')
    # print('-------------------------')
print(L)

'''
กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

***** อธิบาย Input 5 แบบ *****

1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร


Enter Input : I Apple,I Bird,I Cat
Apple Bird Cat | 

Enter Input : I Apple,I Bird,I Cat,L
Apple Bird | Cat 

Enter Input : I Apple,I Bird,I Cat,L,L
Apple | Bird Cat 

Enter Input : I Apple,I Bird,I Cat,L,L,L,L,L
| Apple Bird Cat 

Enter Input : I Apple,I Bird,I Cat,L,L,R
Apple Bird | Cat 

Enter Input : I Apple,I Bird,I Cat,L,L,R,B
Apple | Cat 

Enter Input : I Apple,I Bird,L,L,R,D,D
Apple | 

Enter Input : L,R,I ABC,I DE,L,I FGHI
ABC FGHI | DE 

Enter Input : I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L
| BCD 

Enter Input : I I,I KMITL,L,L,R,I Love
I Love | KMITL 

Enter Input : I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
I Hate | DataStructure 


I Apple,I Bird,I Cat
I Apple,I Bird,I Cat,L
I Apple,I Bird,I Cat,L,L
I Apple,I Bird,I Cat,L,L,L,L,L
I Apple,I Bird,I Cat,L,L,R
I Apple,I Bird,I Cat,L,L,R,B
I Apple,I Bird,L,L,R,D,D
L,R,I ABC,I DE,L,I FGHI
I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L
I I,I KMITL,L,L,R,I Love
I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
'''