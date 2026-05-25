# 문제12. 
# 사용자로부터 하나의 문장을 입력받아 다음 기준에 따라 문장의 “유형”을 판단하세요. 
# 규칙: - 감탄사 "!" 로 끝나면 → "감탄 문장" - 물음표 "?" 로 끝나면 → "의문 문장" - 문장 길이가 30자 이상이면 → "긴 문장" - 문장에 숫자가 하나라도 포함되어 있으면 → "숫자 포함 문장" 
# 위 조건 중 해당되는 모든 유형을 출력하세요. 
# 예) 
# 입력: "Python is amazing! 123" 
# 출력: "감탄 문장, 긴 문장, 숫자 포함 문장" 
# [ hint: 문자열 끝 글자 확인, in, .replace() – 비효율적인 반복 작업이 
# 필요합니다. ]

a = input('입력: ')
if(a[-1]=='!'):
    print('감탄 문장')
elif(a[-1]=="?"):
    print("의문 문장")

if(len(a)>=30):
    print("긴문장")

check_id=0
for n in a:
    if n == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        check_id+=1
if(check_id > 0):
    print('숫자 포함 문장')


# if (a.isnumeric()):
#     print(a.alnum())
#     print('숫자 포함 문장')
# else:
#     print(a.isalnum())



