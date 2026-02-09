# 集合的并操作，可以使用函数，也可以使用操作符

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s3 = ['Js', 'R']

# 使用函数进行操作，此形式运算的数据类型更加灵活，可以不是Set，还可以是List。返回一个新的Set
s = s1.union(s2)
s4 = s.union(s3)

print(s)
print(s1)

s5 = s1 | s2

print(s5)

s6 = s1 | s3

print(s6)