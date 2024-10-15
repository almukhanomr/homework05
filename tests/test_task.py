from src.hw05.task import is_prime, primes, checksum, pipeline


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(11) == True

    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False
    print("test_is_prime: PASSED")


def test_primes():
    prime_numbers = primes(1000)

    assert len(prime_numbers) == 1000

    for prime in prime_numbers:
        assert is_prime(prime) == True
    print("test_primes: PASSED")


def test_checksum():
    test_list = [1, 2, 6, 24]

    assert checksum(test_list) == 6_012_369
    print("test_checksum: PASSED")


def test_pipeline():
    assert pipeline() == 7_785_816
    print("test_pipeline: PASSED")


if __name__ == '__main__':
    test_is_prime()
    test_primes()
    test_checksum()
    test_pipeline()
