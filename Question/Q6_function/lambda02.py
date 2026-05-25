#변수를 선언합니다.
list_input_a = [1,2,3,4,5]

# map()함수를 사용합니다.
output_a = map(lambda x:x*x,list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):",output_a)
print("map(power, list_input_a):",list(output_a))
print()



# # 함수를 선언합니다.

# power = lambda x:x*x
# # def power(item):
# #     return item*item

# under_3 = lambda x:x<3
# # def under_3(item):
# #     return item < 3 # 논리값 리턴 






#filter()함수를 사용합니다
output_b = filter(lambda x:x<3,list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):",output_b)
print("filter(under_3, list_input_a):",list(output_b))
print()