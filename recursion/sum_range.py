def sum_range(n, m):
    if n == m:
        return m
    return n + sum_range(n+1, m)

print(sum_range(4, 6)) # 4+5+6 = 15
print(sum_range(1, 10)) # 55