# lambda表达式是一种匿名函数，且此函数中只有一个表达式，可以有多个参数
def num(a, b, fn):
    return fn(a, b);

def add(a, b):
    return a + b;

# 下列两种表示方式一样的效果
print(num(1, 3, add));
print(num(2, 3, lambda a, b: a + b));

# 返回一个匿名函数
def times(n):
    return lambda x : x * n;

# double指向返回的匿名函数，可以通过double执行
double = times(2);
print(double(4));

# 在callables中存放匿名函数
callables = []
for i in (1, 2, 3):
    callables.append(lambda: i)
# lambda返回的是变量i，在执行了for循环之后，i变为了3，所以输出3个3
# 匿名函数需要等到执行时才去外部作用域找，为了解决此问题，可以在函数被创建时就将i值放入到函数属性中，可以通过使用默认值实现
for f in callables:
    print(f())

funcs = []
for i in range(1, 4):
    # 匿名函数在被创建时就将值赋予给函数内部属性
    funcs.append(lambda a = i : a);    

for f in funcs:
    # 没传入参数，返回默认参数
    print(f());
