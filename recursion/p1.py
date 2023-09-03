def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
n = int(input('Enter Number : '))
print(f'fibo({n}) = {fibo(n)}')
'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive

Enter Number : 1
fibo(1) = 1

Enter Number : 2
fibo(2) = 1

Enter Number : 3
fibo(3) = 2

Enter Number : 4
fibo(4) = 3

Enter Number : 5
fibo(5) = 5

Enter Number : 6
fibo(6) = 8
'''