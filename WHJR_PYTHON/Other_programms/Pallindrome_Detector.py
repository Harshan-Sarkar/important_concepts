a = input("Enter to check if a word is a pallindrome or not: ")
a = a.replace(" ", "")
b = a.upper()
c = b[::-1]
if b == c :
    print(f"Yes, '{a}' is a pallindrome.")
else :
    print(f"No, '{a}' is not a pallindrome.")