# 在函数调用时，参数位置与参数含义可能不用，为了避免这种容易发生错误的情况，可以在传递参数到函数中时使用Keyword Arguments
def get_net_price(price, tax_rate = 0.07, discount = 0.05):
    discount_price = price - price * discount;
    net_price = discount_price * (1 + tax_rate);
    return net_price;

print(get_net_price(1000));

# 如果我想要将discount令为0.03，tax_rate令为0.04，就会导致错误
print(get_net_price(1000, 0.03, 0.04));

# 使用keywork-arguments必须将传入函数中的参数名与声明函数时的参数名完全一致，但放置的顺序可以不同
print(get_net_price(price = 1000, discount = 0.03, tax_rate = 0.04));