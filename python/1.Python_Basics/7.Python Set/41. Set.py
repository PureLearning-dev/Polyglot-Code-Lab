# Set是一个包含不重复元素的集合，元素在其中无序

skills = {'Python programming', 'Databases', 'Software design'}

# 这样定义的是一个空字典而不是一个空集合！
empty_set = {}

# 这样才能进行定义一个空集合
empty_set = set()

skills = set()

if not skills:
    print('Empty sets are falsy')

# set()函数可以接受一个可迭代对象，用于创建集合，它会自动处理重复的元素
skills = set(['Problem solving','Critical Thinking','Critical Thinking'])
print(skills)

# 获取集合的大小
print(len(skills))

# 检查元素是否存在在集合中使用in
if 'Critical Thinking' in skills:
    print('存在')

if 'H' not in skills:
    print('不存在')

# 向集合中添加元素
skills.add('C++')

print(skills)

# 向集合中移除元素
skills.remove('C++')

print(skills)