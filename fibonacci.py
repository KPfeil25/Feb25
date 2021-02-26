import pytest

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac

def test_answer():
    assert factorial(4) == 24

