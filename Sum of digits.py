num = int(input("Enter Number: "))
sum_digit = 0

while num>0:
    sum_digit = sum_digit + num%10
    num//= 10
print("sum of digits is :", sum_digit)