import math
def prime_list(limit):
    if limit < 3:
        return [2] if limit == 2 else []
    size = (limit - 3) // 2
    is_prime = [True] * (size + 1)
    for i in range(math.isqrt(limit - 3) // 2 + 1):
        if is_prime[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            is_prime[s::p] = [False] * ((size - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(is_prime) if v]