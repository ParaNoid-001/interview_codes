# This code checks if a number is prime or not

# num = int(input("Enter a number: " ))
# count = 0

# if num>1:
#     for i in range(1, num+1):
#         if (num%i) == 0:
#             count += 1

#     if count == 2:
#         print ("it's a prime")
#     else:
#         print("not prime") 

num = int(input("Enter number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

