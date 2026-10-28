# def greet(name):
#     print("Hello,",name)
# greet("Sam")
# greet("Sujita")

transactions = [{"category":"food","amount":12.50},
                {"category":"transport","amount":8.00},
                {"category":"food","amount":34.20},
                {"category":"entertainment","amount":15.00},
                {"category":"transport","amount":5.50},]
# print(transactions[1])
# print(transactions[1]["category"])
# print(transactions[1]["amount"])
def total_by_category(transactions):
    totals = {}
    for t in transactions:
        category =t["category"]
        amount =t["amount"]
total_by_category(transactions)
