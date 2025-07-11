text = input("Enter text: ")
for i in set(text):
    print(i, text.count(i))