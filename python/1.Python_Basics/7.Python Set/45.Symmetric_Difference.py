s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# 这个方法是会返回两个集合中都不在交集的元素
s4 = s1.symmetric_difference(s2)
print(s4)