def fatorial(n):
    if n == 0 or n == 1:
        return 1
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

limite = 30
e = 0
for n in range(limite):
    e += 1/fatorial(n)

# while n < limite:
#     e += 1/fatorial(n)
#     n += 1

print(f"e = {e} con {limite} iteraciones")