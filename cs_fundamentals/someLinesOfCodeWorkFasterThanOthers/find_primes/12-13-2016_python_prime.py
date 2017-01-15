"""Python Exercises in Prime Numbers

The following functions are part of an exercise in response to a
CodeWars Kata. Very fun.

Important topics covered here are the functional programming tools:
    - operator
      - mod - modulo
      - floordiv - round down the quotient

Performance monitoring tools:
    - timeit

Completed: 12/13/2016
"""

import doctest # test a little
import operator # get functional
import math # get mathy
import timeit # optimize

def gap(g, m, n):
    """Return least primes in interval `m` and `n` with prime gap of `g`.

    g --- desired prime gap
    m --- lower bound
    n --- upper bound

    Examples:
    >>> gap(2, 2, 50)
    [3, 5]
    >>> gap(6, 100, 110)

    """
    a=0
    b=0

    interval = list(range(m, n+1))
    primer = list(range(2, math.floor(math.sqrt(n))))
 
    for i in primer:
        interval[:] = [x for x in interval if x==i or operator.mod(x, i)!=0]

    it = iter(interval)

    for p in it:
        if a:
            if p - a == g:
                b = p
                return [a, b]
            else:
                a = p
                continue
        else:
            pp = next(it)
            if pp - p == g:
                a = p
                b = pp
                return [a, b]
            else:
                a = pp
                continue

    return None

def fast_gap(g, m, n):
    """Return least primes in interval `m` and `n` with prime gap of `g`.

    g --- desired prime gap
    m --- lower bound
    n --- upper bound

    Examples:
    >>> gap(1,1,10)
    [2, 3]
    >>> gap(2, 2, 50)
    [3, 5]
    >>> gap(6, 100, 110)

    """
    a=2
    b=0

    interval = list(range(m, n+1))
    primer = list(range(2, math.floor(math.sqrt(n))+1))

    for e, x in enumerate(interval):
        # print("We are testing {} for primality. \
                # It has index: {}".format(x, e))
        is_Prime = True
        
        ''' Compare with Python's all() built-in
        '''
        for j in primer:
            if x != j and operator.mod(x, j) == 0:
                # print("{} is definitely not prime.".format(x))
                is_Prime = False
                                
                if x < math.floor(math.sqrt(n))+1:
                    i = primer.index(x)
                    # print("remove from primer, the number: {},\
                        # with index: {}".format(x, i))
                    del primer[i]
                    # print("---")
                    break
                else:
                    # print("---")
                    break
            else:
                continue
                # print("{} may be prime.".format(x))
        
        if is_Prime:
            # print("{} is definitely prime.".format(x))
            if a == 1:
                a = x
                # print("{} assigned to variable `a`".format(x))
                # print("---")
                continue
            else:
                pgap = x - a
                if pgap == g:
                    b = x
                    return [a, b]
                else:
                    a = x
                    # print("We have a new value for `a`: {}".format(x))
                    # print("---")
        else:
            continue
    
    return None

# Benchmarking
def haid():
    if True:
        # x = timeit.timeit('it = range(100,1000)')
        # it = range(100,1000)
        # y = timeit.timeit('iter(it)', globals=locals())
        # Wow. It takes a shit ton of time to make lists and sets compared to
        # iterators.
        # z = timeit.timeit('list(it)', globals=locals())
        # a = timeit.timeit('set(it)', globals=locals())

        gap = timeit.timeit('gap(6,2,400)', number=10000, globals=globals())
        fast_gap = timeit.timeit('fast_gap(6,2,400)', number=10000, globals=globals())

        return "gap: {} fast_gap: {}".format(gap, fast_gap)
    return "Okay?"

def succinct_gap(g, m, n):
    """Solution from Codewars
    """
    prev = 2
    for x in range(m|1, n + 1, 2):
        if all(x%d for d in range(3, int(x**0.5)+1, 2)):
            if x - prev == g: return [prev, x]
            prev = x 
 
def multiples(n, j, k):
    x = operator.floordiv(j, n) + 1
    return list(range(x, k, n))


