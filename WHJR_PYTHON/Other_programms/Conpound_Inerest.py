p = int(input("Enter your Principal:\t"))
r = int(input("Enter your Rate of Interest:\t"))
n = int(input("Enter your Time in years:\t"))
x = (1 + (r/100))
b = x ** n
c = p * b
print("The Amount is Rs", c)
ask = input("Do you want Compund Interest (y/n) ?\n :  ")
if ask == "y" :
    print(c - p)
elif ask == "n" :
    print ("Thank you")
else :
    print("I cannot understand what you have written, Try again by re-executing the program")