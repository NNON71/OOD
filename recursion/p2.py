def findD(i,j):
    # print(arr)
    # print(arr[j][i],i,j)
    if j > 0 and arr[j-1][i] == '#':
        arr[j-1][i] = 'x'
        findD(i,j-1)
    if j < y-1 and arr[j+1][i] == '#':
        arr[j+1][i] = 'x'
        findD(i,j+1)
    if i > 0 and arr[j][i-1] == '#':
        arr[j][i-1] = 'x'
        findD(i-1,j)
    if i < x-1 and arr[j][i+1] == '#':
        arr[j][i+1] = 'x'
        findD(i+1,j)

x,y = list(map(int,input('Enter input: ').split()))
arr = []
count = 0
for _ in range(y):
    arr.append(input().split())
for j in range(y):
    for i in range(x):
        if arr[j][i] == '#':
            findD(i,j)
            count += 1
print(count)

'''
ณ เมืองแห่งหนึ่งมีปีศาจร้ายจำนวนมาก ทำให้ชวนบ้านไม่สามารถอยู่อย่างสงบสุขได้ จึงได้ทำการจ้างนักล่าปีศาจมาจัดการ นักล่าปีศาจอยากรู้จำนวนที่แน่นอนของปีศาจก่อน เพื่อจะได้เตรียมอุปกรณ์ในการจัดการพวกมัน โดยชิ้นส่วนของปีศาจ '#' ที่อยู่ติดกันนับเป็นตัวเดียวกัน

โดย x y คือ ความกว้าง และความสูงของหมู่บ้านตามลำดับ หลังจากนั้นอีก y บรรทัด รับตำแหน่งต่างๆของหมู่บ้าน x ตัว

งานของคุณ คือ หาจำนวนปีศาจทั้งหมดในหมู่บ้าน โดย '#' แทนชิ้นส่วนของปีศาจ และ '.' แทนพื้นที่ว่าง

Example 1:
Input:
Enter input: 3 3
. # .
# . #
. # .

Output:
4

อธิบาย:
มีจำนวนปีศาจทั้งหมด 4 ตัว

Example 2:
Input:
Enter input: 3 3
# # #
. . .
# # #

Output:
2

อธิบาย:
มีจำนวนปีศาจทั้งหมด 2 ตัว

Example 3:
Input:
Enter input: 2 2
# #
# #

Output:
1

อธิบาย:
มีจำนวนปีศาจทั้งหมด 1 ตัว

Enter input: 4 4
. # # . 
# . . .
. . # .
# # . .
4

Enter input: 5 5
. # # # # 
# . . # .
. # # . #
# # # . #
. # . . #
4

Enter input: 8 6
# . # . . # . #
. . # # # . . #
# . # . # # . #
# # # # # # . #
. . # # . . # .
. . # . . . . .
5
'''