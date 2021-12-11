from functools import reduce

print(list(map(lambda x: x*2, [1,2,3])))

print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3,4], [4,5,6])))
print(list(zip([1,2,3], [4,5,6,7])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))

print(reduce(lambda x,y: x+y, [1,2,3]))
print(reduce(lambda x,y: str(x)+str(y), [1,2,3]))

print(list(filter(lambda x: x%2 == 0, [1,2,3,4])))