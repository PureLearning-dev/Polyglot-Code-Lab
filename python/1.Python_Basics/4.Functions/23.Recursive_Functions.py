# 在函数A中调用函数A，直到满足终止条件
def acc(val):
    if(val == 1):
        return 1;
    return val + acc(val - 1);

print(acc(4));