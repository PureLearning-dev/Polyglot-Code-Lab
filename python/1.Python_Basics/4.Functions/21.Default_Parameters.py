# 函数中的参数可以有默认值，防止在使用函数时没有传递对应参数的值而导致错误
def sum(a = 10, b = 10):
    return a + b;

print(sum());
print(sum(1, 1));

def sub(a, b = 1):
    return a - b;

print(sub(2));

# 在设置默认值时，只能前面的参数不设置，若前面参数设置，后面参数不设置，会报错
# def div(a = 10, b = 1, c):
#     return a / b;