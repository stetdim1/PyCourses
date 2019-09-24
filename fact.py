# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))


# for i in range(0,10):
#     print(bool(i%2))
#
# for i in filter(lambda x: x%2,range(1,10)):
#     print(i)


b = [a for a in range(10, 1, -1)]
bf = [k for k in b if k%2]
bfw = [2**k for k in bf]
print(b)
print(bf)
print(bfw)