# N이 sqrt(N) 이하의 소인수로 나누어떨어지는지 검사
# primes = prime_list(10000000) 으로 소수 리스트 생성 후 실행
# 소수 리스트를 백만(10^7)까지 생성한다면 약 (10^14)까지 판별가능
def isprime(x):
    if x == 1:
        return False
    for i in primes:
        if i > x ** .5:
            break
        if x % i == 0:
            return False
    return True