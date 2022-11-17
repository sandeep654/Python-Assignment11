#Write a python script to calculate sum of cubes of first N natural numbers
N=int(input("Enter N Natural number:"))
i=0
for e in range(1,N+1,1):
    i=(e**3)+i
print("Sum of cube first n natural number",i)