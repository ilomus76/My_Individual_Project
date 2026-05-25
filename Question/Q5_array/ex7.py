# 문제7. 
# 아래의 딕셔너리를 사용하여 전화번호부를 관리합니다. 
# phone_book = { 
# "홍길동": "010-1234-5678", 
# "김철수": "010-9876-5432", 
# "이영희": "010-5555-6666" 
# } 
# 다음의 요구사항을 수행해보세요. 
# 1. "박민수": "010-1111-2222"를 추가하시오. 
# 2. "김철수"의 번호를 "010-9999-0000"으로 수정하시오. 
# 3. "이영희"의 정보를 삭제하시오. 
# 4. 모든 이름(key)을 출력하시오. 
# 5. 모든 전화번호(value)를 출력하시오. 
# 6. 사용자로부터 이름을 입력받아, 전화번호부에서 해당 번호를 찾아 출력하시오. 

phone_book = { 
"홍길동": "010-1234-5678", 
"김철수": "010-9876-5432", 
"이영희": "010-5555-6666" 
} 
print(phone_book)
phone_book['박민수'] = "010-1111-2222"

#"김철수"의 번호를 "010-9999-0000"으로 수정하시오. 
phone_book['김철수']="010-9999-0000"
print(phone_book)

# 3. "이영희"의 정보를 삭제하시오. 
#del phone_book['이영희']
phone_book.pop('이영희')
print(phone_book)

# 4. 모든 이름(key)을 출력하시오. 
for e in phone_book:
    print("모든 key 값은:",e)

# 5. 모든 전화번호(value)를 출력하시오. 
items = phone_book.items()

for key,value in items:
    print("모든 전화번호는: ",value)
# 6. 사용자로부터 이름을 입력받아, 전화번호부에서 해당 번호를 찾아 출력하시오. 
temp_name = input("추가할 이름을 입력하세요: >>")
temp_phone_number = input("추가할 전화번호를 입력하세요")
phone_book[temp_name]=temp_phone_number

print(phone_book)