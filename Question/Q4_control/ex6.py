# 문제6. 로그인 검사 
# 미리 저장된 ID와 패스워드를 기준으로, 
# 사용자가 입력한 값이 둘 다 일치하면 "로그인 성공", 
# 하나라도 틀리면 "로그인 실패" 를 출력하는 프로그램을 작성하세요. 
# saved_id = "python" 

saved_id = "python"
saved_pw = "1234" 

user_input_id= input("User ID ::::: ")
user_input_password = input("Password :::: ")

if user_input_id == saved_id and user_input_password == saved_pw:
    print(f"로그인 성공")
else:
    print(f"로그인 실패")
    print(f"ID와 password를 확인하세요!")

