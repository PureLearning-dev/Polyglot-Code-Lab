# 与所有编程语言一样，python也存在函数，其将一系列操作合并为一个整体并为这个整体命名，称为函数名
def add(a, b):
    return a + b;

def main():
    # input函数返回的是一个string类型，需要使用int函数将其转换为int型
    a = input("输入一个整数");
    b = input("输入另一个整数");
    print(add(int(a), int(b)));

# main();

# python中的函数和js中的函数一样，函数是一等公民，可以传递到函数中
def sum(a, b, callback):
    return callback(a, b);

result = sum(3, 5, add);
print(result);