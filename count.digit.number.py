#Write a python script to count digits in a given number
num = int(input("Enter any number : "))
count = 0
for i in str(num):
    num=num//10
    count+=1
print(count)