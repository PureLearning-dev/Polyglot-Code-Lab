numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3, 4, 5}

# 判断函数中的集合是否为外部集合的子集，相当于<=
print(scores.issubset(numbers))

print(numbers <= scores)

print(numbers < scores)