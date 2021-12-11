print([x for x in [1,2,3]])
print([x*x for x in [1,2,3]])
print([x for x in [1,2,3] if x%2 == 1])
print([x*x for x in [1,2,3] if x%2 == 1])

print(list(map(lambda x: x*x, filter(lambda x: x%2 == 1, [1,2,3]))))

print([x%3 for x in [7,16,14] if x%7 == 0])
print(list(map(lambda x: x%3, filter(lambda x: x%7 == 0, [7,16,14]))))
