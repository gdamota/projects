def fizzbuzz(n):

    if n%3==0 and n%5==0:
        return 'Fizzbuzz'
    elif n%3==0 and n%5!==0:
        return 'Fizz'
    elif n%5==0 and n%3!==0:
        return 'Buzz'
    else:
        str(n)

print "\n".join(fizzbuzz(n) for n in xrange(1, 100))