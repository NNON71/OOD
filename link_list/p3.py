class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        self.value = data
        self.next = None
        
    def __str__(self):
        ### Code Here ###
        return str(self.value)

def createList(l=[]):
    ### Code Here ###
    head = node(l[0])
    current_node = head
    for i in range(1,len(l)):
        current_node.next = node(l[i])
        current_node = current_node.next
    return head

def printList(H):
    ### Code Here ###
    current_node = H
    while current_node :
        print(current_node,end = ' ')
        current_node = current_node.next
    print('')

def mergeOrderesList(p,q):
    ### Code Here ###
    head = node(0)
    current_node = head
    while p and q:
        if p.value <= q.value:
            current_node.next = p
            p = p.next
        else:
            current_node.next = q
            q = q.next
        current_node = current_node.next
    current_node.next = p or q
    return head.next
        

#################### FIX comand ####################   
# input only a number save in L1,L2
L1,L2 = list(input('Enter 2 Lists : ').split())
L1,L2 = list(map(int,L1.split(','))),list(map(int,L2.split(',')))
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)

'''
จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

****ห้ามสร้าง Class LinkList****

class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
    def __str__(self):
        ### Code Here ###

def createList(l=[]):
    ### Code Here ###

def printList(H):
    ### Code Here ###

def mergeOrderesList(p,q):
    ### Code Here ###

#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)

Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
LL1 : 1 3 5 7 10 20 22 
LL2 : 4 6 7 8 15 
Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 


Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10
LL1 : 1 4 5 5 6 7 
LL2 : 2 3 6 9 10 
Merge Result : 1 2 3 4 5 5 6 6 7 9 10 

Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
LL1 : 2 2 2 10 
LL2 : 1 1 1 1 5 5 5 6 7 8 
Merge Result : 1 1 1 1 2 2 2 5 5 5 6 7 8 10 
'''