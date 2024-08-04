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

#def factors(n):
#    def smaller_factors():
#        k = 1
#        while k * k <= n:
#            if n % k == 0:
#                yield k
#                if k != n // k:
#                    yield n // k
#            k += 1
#    
#    def larger_factors(small_factors_gen):
#        # Track factors in increasing order from the first generator
#        for factor in small_factors_gen:
#            yield factor
#        k = int(n ** 0.5) + 1
#        while k <= n:
#            if n % k == 0:
#                if k != n // k:  # Avoid yielding the square root twice if it's a perfect square
#                    yield n // k
#            k += 1
#
#    # Generate smaller factors and then generate the corresponding larger factors
#    small_factors_gen = smaller_factors()
#    yield from larger_factors(small_factors_gen)

