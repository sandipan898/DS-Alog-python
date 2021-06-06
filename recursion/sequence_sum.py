def sequence_sum(n):
    assert n >= 0 and int(n) == n, "The number should be an Positive Integer number"
    if n == 0:
        return 0
    return n + sequence_sum(n-1)

print(sequence_sum(4)) # 1+2+3+4 = 10