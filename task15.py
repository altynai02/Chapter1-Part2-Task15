# 15. Write the code, which will print numbers from 0 till your age. And if your
# age is odd, will be printed all odd numbers till your age, if even all even
# numbers.
your_age = int(input("Enter your age: "))
for i in range(your_age):
    if your_age % 2 == 0:
        if i % 2 == 0:
            print(i)
    elif your_age % 2 != 0:
        if i % 2 != 0:
            print(i)