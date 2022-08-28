from decimal import Decimal
print("Введіть кількість гривень:")
grn = Decimal(input())

def exchange():
  rate = Decimal('37.2')
  return f"Станом на 25 серпня 2022 року це становить { round(Decimal(grn / rate), 2)} доларiв США :("
print(exchange())
