#Write a python script to calculate sum of digits of a given number
num = int(input("Enter any number : "))
count = 0
for i in str(num):
    remainder = num % 10
    count=count+remainder
    num=num//10
print(count)