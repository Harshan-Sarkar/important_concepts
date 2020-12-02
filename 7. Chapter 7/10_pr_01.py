num = int(input("Enter the number"))
list = []
for i in range(1, 11):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    # print(f"{num}X{i}={num*i}")
    list.append(num*i)
list.reverse()
print(list)
# 