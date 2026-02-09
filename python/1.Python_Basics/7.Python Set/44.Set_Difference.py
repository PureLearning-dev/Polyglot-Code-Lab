s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s3 = ['Java']

# 返回左侧相对于右侧的不同值，此时s4只会返回s1中的Python，而不会返回s2中的C#
s4 = s1.difference(s2)
print(s4)

s5 = s1 - s2

print(s5)

s6 = s1.difference(s3)

print(s6)

s7 = s1 - s3

print(s7)