from primes import *

def test_prime_low_number():
    assert is_prime(1) == False

def test_prime_prime_number():
    assert is_prime(29)

def test_prime_composite_number():
    assert is_prime(15) == False

def test_sum_of_primes_empty_list():
    assert sum_of_primes([]) == 0