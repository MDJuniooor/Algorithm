def calc(a, index, cur, plus, minus, mul, div):
    if index == len(a):
        return (cur, cur)
    res = []
    if plus > 0:
        res.append(calc(a, index+1, cur+a[index], plus-1, minus, mul, div))
    if minus > 0:
        res.append(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
    if mul > 0:
        res.append(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
    if div > 0:
        if cur >= 0:
            res.append(
                calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
        else:
            res.append(
                calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div-1))
    ans = (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )

    return ans


n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = calc(a, 1, a[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])

# n = int(input())
# a = list(map(int, input().split()))
# w, x, y, z = map(int, input().split())
# mx = -2e9
# mn = 2e9


# def f(i, t, w, x, y, z):
#     global mx, mn
#     if i == n:
#         if t > mx:
#             mx = t
#         if t < mn:
#             mn = t
#         return
#     if w:
#         f(i + 1, t + a[i], w - 1, x, y, z)
#     if x:
#         f(i + 1, t - a[i], w, x - 1, y, z)
#     if y:
#         f(i + 1, t * a[i], w, x, y - 1, z)
#     if z and a[i]:
#         f(i + 1, t // a[i] if t > 0 else -(-t // a[i]), w, x, y, z - 1)


# f(1, a[0], w, x, y, z)
# print(mx)
# print(mn)
