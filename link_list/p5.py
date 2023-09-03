class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.visited = False
        self.l = 0

    def del_head(self):
        temp = self
        self.next = self.next.next
        return temp

    def size(self):
        cur,i = self,0
        while cur and not cur.visited:
            cur.visited = True
            i+=1
            cur =cur.next 
        cur = self
        while cur and cur.visited:
            cur.visited = False
            cur = cur.next
        return i

    def print(self):
        cur = self
        result = ""
        while cur and not cur.visited:
            cur.visited = True
            result += str(cur.val)
            result += '['
            result += str(cur.l)
            result += '] ->'
            cur =cur.next 
        cur = self
        while cur and cur.visited:
            cur.visited = False
            cur =cur.next 
        return result

    def print_result(self):
        cur = self
        result = ""
        while cur:
            cur.visited = True
            result += str(cur.val)
            result += ' -> '
            cur =cur.next 
        return result

    def __str__(self):
        return f'Node({self.val}, size={self.size()})'

inp = [list(map(int,p.split('>'))) for p in input('Enter edges: ').split(',')]
node_dict = {}
for f,s in inp:
    if f not in node_dict:
        node_dict[f] = Node(f)
    if s not in node_dict:
        node_dict[s] = Node(s)
        node_dict[f].next = node_dict[s]
        node_dict[s].l += 1
    else:
        node_dict[f].next = node_dict[s]
        node_dict[s].l += 1

intersect = []
for v in node_dict.values():
    if v.l > 1:
        intersect.append(v)
intersect.sort(key= lambda v : v.val)

if intersect == []:
    print("No intersection")
    exit()

for i in intersect:
    print(i)
print("Delete intersection then swap merge:")

for v in node_dict.values():
    if v.next != None and v.next.l > 1 :
        v.next = None
    if v.next != None and v.l > 1 :
        v.next.l -= 1
        v.next = None

n_head = []
for k,v in node_dict.items():
    if v.l == 0:
        n_head.append(node_dict[k])
n_head.sort(key= lambda v : v.val)
result = Node(0)

stxt = []
while len(n_head) != 0:
    txt = []
    size = len(n_head)
    for i in range(size):
        x = n_head.pop(0)
        txt.append(x.val)
        if x.next != None:
            n_head.append(x.next)
    for i in txt:
        stxt.append(str(i))

print(" -> ".join(stxt)) 