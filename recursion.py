def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def fibo(n):
    if (n == 0): return 0
    elif (n == 1): return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def hanoi (disc, start, end, middle):
    if (disc <= 1):
        print (start, end)
        return
    else:
        hanoi(disc - 1, start, middle, end)
        print(start, end)
        hanoi(disc - 1, middle, end, start)

if __name__ == '__main__':
    print("Enter a number and get n!")
    a = int(input())
    print(factorial(a))

    print("Enter a number and get n-th fibonacci number:")
    a = int(input())
    print(fibo(a))

    print("Enter a number of disc:")
    a = int(input())
    print("Number of movement:", (2 ** a) - 1)
    hanoi(a, 1, 3, 2)