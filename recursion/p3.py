def way(n,i):
    global short_path
    if n == 0:
        if i < short_path:
            short_path = i
        return 1
    elif n < 0 or n%14 == 0:
        return 0
    return way(n-1,i+1)+way(n-5,i+1)+way(n-7,i+1)

short_path = 999
n = int(input('Input number : '))
result = way(n,0)
if result == 0:
    print('Mission Failed')
    exit()
print(f'Minimum Distance is {short_path}')
print(f'Maximum Way is {result}')

'''
กบเขียวเคโรโระ ต้องการกระโดดจากช่องหมายเลข 0 ไปเลขต่างๆ ไม่เกิน 40 เคโรโระ ต้องการทราบวิธีการไปทั้งหมด และจำนวนครั้งที่กระโดดน้อยที่สุด เมื่อเคโรโระสามารถกระโดดได้ทีละ 1 5 7 ช่อง

เช่น ไปช่อง 7 จะมี 5 วิธีคือ

โดด 7 ครั้ง 1 1 1 1 1 1 1

โดด 3 ครั้ง  5 1 1

โดด 3 ครั้ง  1 5 1

โดด 3 ครั้ง  1 1 5

โดด 1 ครั้ง  7  น้อยสุด

ไปช่อง 7 จะมี 5 วิธี โดดน้อยสุด 1

แต่ว่ากบแดงกิโรโระจะดักโจมตีช่องที่หารด้วย14ลงตัว ทำให้เคโรโระไม่สามารถผ่านช่องเหล่านั้นได้ ถ้าเคโรโระไม่สามารถไปถึงจุดหมายได้ ให้แสดง mission failed

Input number : 3
Minimum Distance is 3
Maximum Way is 1

Input number : 10
Minimum Distance is 2
Maximum Way is 12

Input number : 14
Mission Failed

Input number : 20
Minimum Distance is 4
Maximum Way is 203

Input number : 28
Mission Failed

Input number : 35
Minimum Distance is 7
Maximum Way is 15291

'''