# Question 1: Code Tracing
# 1300, 1500, 2700, 1500
# Output: 4
# Output: 7000

# Question 2: Code Tracing
# Output: 0x9F1aB3c...

# Question 3: Code Writing
def portfolio_value(holdings, prices):
    sum = 0
    for key, value in holdings.items():
        multiplied = value * prices[key]
        sum += multiplied
    return f"{sum:.2f}"
            
holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142}
print(portfolio_value(holdings, prices))