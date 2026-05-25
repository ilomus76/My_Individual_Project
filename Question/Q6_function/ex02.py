# 문제2. 
# 섭씨(Celsius)온도를 입력하면 화씨(Fahrenheit)온도를 반환하는 cel_to_fah라는 
# 이름의 
# 함수와 그 반대로 화씨 온도를 입력하면 섭씨 온도를 반환하는 fah_to_cel라는 이름의 
# 함수를 정의하고 이 두 함수를 호출하는 예제를 완성해 보자. 참고로 섭씨와 화씨간의
# 온동변환의 공식은 다음과 같다. 
# Fah=1.8*Cel+32 

def cel_to_fah(cel_temp_value=25):
    fah_temp_value = 1.8 * cel_temp_value +32
    return fah_temp_value # 단일 변수 

def fah_to_cel(fah_temp_value=0):
    cel_temp_value =( fah_temp_value -32 ) / 1.8
    return cel_temp_value

cel_to_fah_conversion = cel_to_fah(25)
fah_to_cel_conversion = fah_to_cel(25)
print('입력한 섭씨(Celsius)온도를 화씨(Fahrenheit)온도로 바꾸면:{:f}'.format(cel_to_fah_conversion))
print('입력한 화씨(Fahrenheit)를 섭씨(Celsius)온도로 바꾸면:{}'.format(fah_to_cel_conversion))

