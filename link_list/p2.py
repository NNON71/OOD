class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

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

    def append(self, item):
        #Code Here
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, item):
        #Code Here
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, pos, item):
        #Code Here
        i = 0
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
        elif pos == 0 :
            self.addHead(item) 
        elif pos > 0 :
            current_node = self.head
            if pos >= self.size():
                self.append(item)
                return
            while current_node.next and i < pos-1:
                i += 1
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next.previous = new_node
            current_node.next = new_node
        else:
            current_node = self.tail
            pos = abs(pos)
            if pos >= self.size():
                self.addHead(item)
                return
            while i < pos-1:
                i+=1
                current_node = current_node.previous
            new_node.previous = current_node.previous
            new_node.next = current_node
            current_node.previous.next = new_node
            current_node.previous = new_node
            

    def search(self, item):
        #Code Here
        if self.isEmpty():
            return 'Not Found'
        current_node = self.head
        while current_node :
            if current_node.value == item:
                return 'Found'
            current_node = current_node.next
        return 'Not Found'

    def index(self, item):
        #Code Here
        i = 0
        if self.isEmpty():
            return -1
        current_node = self.head
        while current_node :
            if current_node.value == item:
                return i
            i+=1
            current_node = current_node.next
        return -1

    def size(self):
        #Code Here
        s = 0
        if self.isEmpty():
            return 0
        else:
            current_node = self.head
            while current_node :
                s+=1
                current_node = current_node.next
            return s
            
    def pop(self, pos):
        #Code Here
        if self.isEmpty() or abs(pos) >= self.size():
            return 'Out of Range'
        current_node = self.head
        current_tail = self.tail
        if pos == 0:
            if self.size() == 1:
                self.head = self.tail = None
                return 'Success'
            elif self.size() > 1:
                nextCur = current_node.next
                nextCur.previous = None
                self.head = nextCur
                return 'Success'
        elif pos == self.size()-1:
            current_tail.previous.next = None
            self.tail = current_tail.previous
            return 'Success'
        elif pos > 0:   
            while pos != 0:
                current_node = current_node.next
                pos -= 1
            prevN = current_node.previous
            nextN = current_node.next
            prevN.next = nextN
            nextN.previous = prevN
            return 'Success'
        elif pos < 0:
            npos = self.size() + pos 
            if npos == 0:
                nextCur = current_node.next
                nextCur.previous = None
                self.head = nextCur
                return 'Success'
            elif npos == self.size()-1:
                current_tail.previous.next = None
                self.tail = current_tail.previous
                return 'Success'
            while npos != 0:
                current_node = current_node.next
                npos -= 1
            prevN = current_node.previous
            nextN = current_node.next
            prevN.next = nextN
            nextN.previous = prevN
            return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())


'''
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้
1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
9. size           คืนค่าเป็นขนาดของ Linked List
10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

ถ้าน้องยังไม่ค่อยเข้าใจการทำงานของ insert ให้น้องลองกับ List บน Python ได้  เช่น
1.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(0,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]
2.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(999,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , 2 , 3 , "T" ]
3.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-2,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , "T" , 2 , 3 ]  
4.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-10,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]

โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO
7. insert       ->   IS

โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

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

    def append(self, item):
        #Code Here

    def addHead(self, item):
        #Code Here

    def insert(self, pos, item):
        #Code Here

    def search(self, item):
        #Code Here

    def index(self, item):
        #Code Here

    def size(self):
        #Code Here

    def pop(self, pos):
        #Code Here

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())



AP I,AP Love,AP KMITL,AP 2020
PO -999,PO 999,PO 0,AP KMITL,PO 999,PO 0
SI,AH 2020,SI,AH KMITL,SI,AH LOVE,SI,AH I,SI
SI,IS 0 KMITL,SI,SE 0,SE KMITL,ID 0,ID KMITL,PO 0,SI,IS -999 CE,SI
AP 0,AP 1,AP 2,AP 3,SI,IS 999 KMITL,SI
AH 3,AH 2,AH 1,AH 0,SI,IS -3 KMITL,SI
AP 0,AP 1,AP 2,AP 3,SI,IS -999 KMITL,SI

AP 0,SI,AH 1,SI,AP 2,SI,AH 3,SI,IS 5 KMITL,SI
AP 0,SI,AH 1,SI,AP 2,SI,AH 3,SI,IS 5 KMITL,SI,ID KMITL,PO 0,ID KMITL
AH Soldier,AP IN,SI,SE Overwatch,ID Soldier,PO 2,IS -1 76,SI,IS 999 Overwatch,SI,SE Overwatch
'''