# 语法：f"内容{变量}"
name = 'zs'
age = 18

print(f"我叫{name},今年{age}")

# example
company_name = '字节跳动'
stock_price = 19.99
stock_code = '003032'
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司{company_name}，股票代码{stock_code}，当前股价{stock_price}")
print("每日增长系数是：%1.1f,经过%d天的增长后，股价达到了：%1.2f" % (stock_price_daily_growth_factor,growth_days,stock_price*(stock_price_daily_growth_factor**growth_days)))
