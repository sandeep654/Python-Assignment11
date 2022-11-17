#Write a python script to calculate sum of first N odd natural numbers
N=int(input("Enter N Natural number:"))
i=0
for e in range(1,N*2,2):
    i=e+i
print("Sum of Square first n natural number",i)