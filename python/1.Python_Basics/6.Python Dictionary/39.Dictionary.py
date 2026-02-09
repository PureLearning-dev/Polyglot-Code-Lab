# python中的字典就是“键值对”
# 键不能被改变，值可以是任意的
empty_dict = {};

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# 访问字典，两种方式
# 第一种方式只能访问存在的键，若访问不存在的键，则会报错
# 第二种方式在访问不存在的键时，不会报错，会返回一个None
print(person['first_name']);
print(person.get('age'));

# get()还可以设置一个返回的默认值，在访问没有这个key时进行默认返回
print(person.get('city', 'SiChuan'));

# 在字典中添加新的key-value
person['city'] = 'CiChuan';

print(person);

# 还可以对字典中的键值对进行修改，删除
person['age'] = 22
print(person)

del person['age']
print(person)

for key in person.keys():
    print(key)

print('---------------')

for key in person:
    print(key)

print('----------------')

for (key, val) in person.items():
    print(f'{key} : {val}');

print('----------------')

for val in person.values():
    print(val)