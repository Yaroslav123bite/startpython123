# print(f'Пример 1')
# for x in 0, 1:
#     for y in 0,1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F = (x or y) and not (y == z) and not(w)
#                 if F == 1:
#                     print(x, y, z, F)
#
# print(f'Пример 2')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#               F = (x or y) and not(y == z) and not(w)
#
#               print(x, y, z, w, F)


print("Пример 1")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (not (a or b)) and c
            if f == 1:
                print(a, b, c, f)

print("Пример 2")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x or not y) <= z
            print(x, y, z, f)

print("Пример 3")
for s1 in 0, 1:
    for s2 in 0, 1:
        for s3 in 0, 1:
            f = (s1 and not s2) or s3
            print(s1, s2, s3, f)


print("Пример 4")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x) == (y or z)
            print(x, y, z, f)

print("Пример 5")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = a <= (b or (not c))
            print(a, b, c, f)

print("Пример 6")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (not (a and b)) or c
            print(a, b, c, f)

print("Пример 7")
for x1 in 0, 1:
    for x2 in 0, 1:
        for x3 in 0, 1:
            f = (not x1 and not x2) or (x1 and x3)
            print(x1, x2, x3, f)

print("Пример 8")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a and (not c)) == (a and b)
            print(a, b, c, f)




