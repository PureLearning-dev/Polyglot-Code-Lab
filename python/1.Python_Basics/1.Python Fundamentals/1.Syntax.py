# 就和其他动态语言一样，python的语法是非常灵活的，也不需要分号结尾
# python和js这门动态语言也有这很大的区别，语法中python不使用大括号，而是使用缩紧进行控制代码块

def main(val):
    i = 0;
    while(i < val):
        print(i);
        i = i + 1;

main(10);

# 若需要在一行中进行换行，使用 \

def test(a, b, c):
    if (a == True) and (b == False) and \
   (c == True):
        print("Continuation of statements")

test(True, False, True);

# python中存在着关键字，常见的请查询：https://www.pythontutorial.net/python-basics/python-syntax/

# 三引号可以直接存放换行，适用于文档书写，并且使用特殊字符时，不需要转义。对于单引号和双引号，在使用特殊字符时，都需要进行转义

print(
'''   hello 
   world !
      ''');