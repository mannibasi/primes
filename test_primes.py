from primes import *

def test_prime_low_number():
    assert is_prime(1) == False

def test_prime_prime_number():
    assert is_prime(29)

def test_prime_composite_numbeer():
    assert is_prime(15) == False