def is_palindrome(n):
    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit   #palindrome number
        n = n // 10

    return original == reversed_num

num = int(input("Enter a number: "))
if is_palindrome(num):
    print("It's a palindrome number.")
else:
    print("It's not a palindrome number.")
