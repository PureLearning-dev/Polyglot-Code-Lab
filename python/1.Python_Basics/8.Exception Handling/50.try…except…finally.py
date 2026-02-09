# 无论成功执行还是发生异常处理，都需要执行的代码可以放入到finally中
a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')

# except语句是可选的，换句话说就是异常可以不处理

try:
    c = a / b
    print(c)
finally:
    print('Finishing up.')
