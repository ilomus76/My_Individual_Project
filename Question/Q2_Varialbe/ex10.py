
# 변수와 자료형 및 키보드 입력기능 : input() 과제 
# 문제10. 
# 마일을 킬로미터로 변환하는 프로그램을 작성하자. 1마일은 1.609킬로미터와 같다. 
# 실행되는 입출력의 모양은 아래와 같이 만들어보자. [예시의 입력값 10은 사용자의 입력값 
# 임] 
# 마일을 입력하시오: 10 
# 10마일은 16.09킬로미터입니다.


# # -----    나의 코드 -------------
# print("This program converts the unit from mile to kilometer.")
# print("1 mile = 1.609 km")
# print()

# #mile_num1 = input(" input the mile that you want to convert into kilometer: ")
# mile_num1 = input(" 마일을 입력하시오 : ")
# float_cast_mile_num1 = float( mile_num1 )
# kilometer_result = float_cast_mile_num1 * 1.609
# #print("{} mile is coresponding to {} km.".format(float_cast_mile_num1,kilometer_result))
# print("{} 마일은 {} km(킬로미터)입니다.".format(float_cast_mile_num1,kilometer_result))

# # ----- end of 나의 코드 ---------------------------

# # --start of 구글 코드 -----------------------------
# def main():
#     # 1. 사용자로부터 마일 입력 받기 (문자열로 입력되므로 float로 변환)
#     mile_str = input("마일을 입력하시오: ")

# # 예외 처리: 숫자가 아닌 값이 입력되었을 경우를 대비
#     try:
#         miles = float(mile_str)

#         # 2. 변환율 상수 정의
#         KM_PER_MILE = 1.609

#         # 3. 계산
#         km = miles * KM_PER_MILE

#         # 4. 결과 출력 (f-string 사용)
#         print(f"{miles}마일은 {km}킬로미터입니다.")

#     except ValueError:
#         print("올바른 숫자를 입력해주세요.")

# if __name__ == "__main__":
#     main()

# # -------------end of 구글 코드 ---------------------------------------------------


# ---- Start of chatgpt 코드 

# 마일을 킬로미터로 변환하는 프로그램

mile = float(input("마일을 입력하시오: "))
km = mile * 1.609

print(f"{mile}마일은 {km:.2f}킬로미터입니다.")
# 설명
# input()으로 사용자 입력을 받고, 소수점 입력도 가능하도록 float로 변환했습니다.
# 변환 공식: 킬로미터 = 마일 × 1.609
# 출력은 f-string을 사용했고, {km:.2f}로 소수점 둘째 자리까지 표시했습니다.
# 실행 예시
# 마일을 입력하시오: 10
# 10.0마일은 16.09킬로미터입니다.

# 만약 출력에서 10.0 대신 10처럼 정수 형태로 깔끔하게 보이게 하고 싶다면 그 부분도 개선해줄 수 있어요.
# ---- end of chatgpt 코드  