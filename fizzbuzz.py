def fizzbuzz(n):
    if n%15 == 0:
        return 'Fizzbuzz'
    elif n%3==0:
        return 'Fizz'
    elif n%5==0:
        return 'Buzz'
    else:
        str(n)

print("\n".join(fizzbuzz(n) for n in range(1, 100))

