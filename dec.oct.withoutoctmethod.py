""" Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)"""
n=int(input("Enter decimal number:"))
bs=''
while n!=0:
    bs=bs+str(n%8)
    n=n//8
print("Decimal no. equal to binary no. is")
for i in range(len(bs)-1,-1,-1):
    print(bs[i],end=' ')