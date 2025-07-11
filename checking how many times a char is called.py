
#str = "AVHGF567832873kjfdj"
str_input = input ("Enter your string: ")
char_count = {}

for i in str_input:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for i in char_count:
    print(f"{i} = {char_count[i]}")
