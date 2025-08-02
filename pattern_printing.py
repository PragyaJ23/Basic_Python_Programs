rows=int(input("enter no of rows"))
for i in range(rows):
    n = int(input("Enter number of rows: "))

    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

