a = int(input("Enter number: "))
length = 0
temp = a
while temp != 0:
    length +=1
    temp = temp// 10
reversed_number = 0
unit = 10**(length-1)
while a !=0 :
    reversed_number += (a%10)*unit
    unit = unit / 10
    a = a // 10
print(int(reversed_number))
