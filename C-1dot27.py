def factors(n):
    k=1
    while k*k <= n:
        if n % k == 0:
            print(k)
#            yield k
            print(n // k)
#            yield n // k
        k += 1
#    if k*k == n:
#        print(k)
#        yield k

factors(100)
