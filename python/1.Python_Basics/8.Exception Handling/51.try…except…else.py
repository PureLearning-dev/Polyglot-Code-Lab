# try:
#     # code that may cause errors
# except:
#     # code that handle exceptions
# else:
#     # code that executes when no exception occurs

# 如果存在finally，则根据上述顺序执行完成后，再执行finally中的代码

fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')
