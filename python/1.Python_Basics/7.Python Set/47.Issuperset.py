# 判断是否为超集
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3, 4, 5}

result = numbers.issuperset(scores)

print(result)

print(numbers >= scores)

print(numbers > scores)