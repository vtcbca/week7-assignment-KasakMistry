#3.Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

def palindrome(n):
    a=str(n)
    if(a==a[::-1]):
        print(f"The number {n} is a palindrome number!!")
    else:
        print(f"The number {n} is not a palindrome number!!")

num=input("Enter a number!!:")
if(num.isdigit()):
    palindrome(num)
else:
    print(f"The given input {num} is not valid number!!")
