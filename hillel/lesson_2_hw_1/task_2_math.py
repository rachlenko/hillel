from math import *
a, b, c = 1, 5, 4
def expression_1():
  return (-b + (sqrt(pow(b, 2) - (4 * a * c)))) / (a * 2)  
#print(expression_1())

def expression_2():
  return (-b - (sqrt(pow(b, 2) - (4 * a * c)))) / (a * 2)
#print(expression_2())


def main():
    a, b, c = 1, 5, 4
    print(expression_1())
    print(expression_2())

if __name__ == '__main__':
    main()
