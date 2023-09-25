#2.Write a python script to enter any number and print the sum of its digit.

def sumofdigit(n):
    a=n
    ram=0
    sum=0
    while(n!=0):
        ram=n%10
        sum=sum+ram
        n//=10
    print(f"The sum of digit of number {a} is {sum}!")  

num=int(input("Enter a number:"))
sumofdigit(num)
