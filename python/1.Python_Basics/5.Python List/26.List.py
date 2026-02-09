# List(列表)，相当于其他编程语言中的数组，通过索引进行访问值
empty_list = [];

todo_list = ['Learn Python List','How to manage List elements'];

test = ["hello", 1, {'age': 10}];
print(test[2])

numbers = [1, 3, 2, 7, 9, 4]
print(numbers)

coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)

# 可以通过负数索引进行访问，从后往前
print(numbers[-1])
print(numbers[-2])

# 列表常用的方法

# append(val): 在列表的最后添加元素val
numbers.append(100)
print(numbers)

# insert(index, value): 指定插入的位置
numbers.insert(1, 10);
print(numbers)

# del(list[index]): 在列表list中删除index上的元素
del numbers[0]
print(numbers)

# pop(): 删除列表中的最后一个元素，并返回
last = numbers.pop()
print(numbers);
print("删除的最后一个元素为: " + str(last));

# remove(val): 删除列表中第一次遇到的val
numbers.remove(9)
print(numbers) 
