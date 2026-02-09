# 对字典的简洁操作，返回一个新的字典

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {}

# 原本的写法
for symbol, price in stocks.items():
    new_stocks[symbol] = price*1.02

print(new_stocks)

# 更加简洁的写法
# 这个字典推导式表达式返回一个新字典，其条目由表达式 key: value 指定
new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks)

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

selected_stocks = {}

# 过滤字典中的元素
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price

print(selected_stocks)

selected_stocks = {symbol: val for (symbol, val) in stocks.items() if val > 200}