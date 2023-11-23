num = int(input("Enter a number: "))

notifier = False

if num == 1:
    print(f"{num} is not a prime number.")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            notifier = True
            break
    if notifier:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")
