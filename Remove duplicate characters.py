text = input("Enter a text: ")
result= ""

for i in text:
    if i not in result:
        result += i

print("Text after removing duplicate characters: ", result)
        