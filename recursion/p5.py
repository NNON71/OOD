def staircase(n,k):
    #code here
    if n-1 == 0:
        return '#'*k
    elif n+1 == 0:
        return '_'*(k-1)+'#'
    elif n > 0:
        print('_'*(n-1)+'#'*k)
        return staircase(n-1,k+1)
    elif n < 0:
        print('_'*(k-1)+'#'*(-n))
        return staircase(n+1,k+1)
    else:
        return 'Not Draw!'

print(staircase(int(input("Enter Input : ")),1))

'''
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

---------------------------------------------------------------

def staircase(n):
    #code here

print(staircase(int(input("Enter Input : "))))

---------------------------------------------------------------
Enter Input : 3
__#
_##
###

Enter Input : 7
______#
_____##
____###
___####
__#####
_######
#######

Enter Input : -8
########
_#######
__######
___#####
____####
_____###
______##
_______#

Enter Input : 2
_#
##

Enter Input : 0
Not Draw!

'''