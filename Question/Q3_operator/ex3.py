# 문제3. 
# 현재의 원화 환율을 찾아 변수에 저장하고, 달러를 키보드로 입력받으면 원화로 출력하는 
# 프로그램을 작성하시오. 

dollar_korea_exchange_rate = 1498 
dollor_value = int( input("계산하고자 하는 달러 금액을 입력하시오: "))
exchanged_value = dollar_korea_exchange_rate * dollor_value

s = "입력하신 {}달러($)의 원화가격은 {}입니다.".format(dollor_value,exchanged_value)
print(s)
