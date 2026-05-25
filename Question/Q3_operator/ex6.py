# 문제6. 
# 상점에 가면 우리는 상품에 대한 돈을 내고 영수증을 받는다. 영수증에서는 10% 
# 부가세와 
# 잔돈 등이 인쇄되어 있다. 구입한 상품의 가격과 손님한테 받은 금액을 입력하면 
# 부가세와 
# 잔돈을 출력하는 프로그램을 작성하여 보자. 
# 받은 돈: 10000 
# 상품 가격: 7500 
# 부가세: 750 
# 잔돈: 1750 

product_price = int ( input("상품가격 : > "))
receved_value = int ( input("받은 가격 : > "))

addition_value = product_price * 0.1
cash = receved_value - product_price - addition_value

a = " 받은 돈은  :{:d}".format(receved_value)
b = " 상품의 가격:{:d}".format(product_price)
c = " 부가세는   :{:g}".format(addition_value)
d = " 잔돈       :{:g}".format(cash)

print(a)
print(b)
print(c)
print(d)




