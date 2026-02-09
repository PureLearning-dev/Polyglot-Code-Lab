# 在for循环语句中有个可选的else语句

# 只有当要进行迭代的对象为空，或者里面没有触发break，才会执行else中的代码

# 不触发break，执行else代码
people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = 'Maria'

found = False
for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break

if not found:
    print(f'{name} not found!')

for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break
else:
    print("没找到")

people  = []

# 遍历空字典会执行else语句中的代码
for person in people:
    print(person)
else:
    print("The list is empty.")