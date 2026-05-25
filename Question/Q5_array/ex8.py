# [심화 문제] 
# 문제 8. 
# 입력값들의 분포를 시각적으로 볼 수 있는 히스토그램을 만드는 프로그램을 작성하시오. 
# 이 프로그램은 1부터 100이하의 정수 10개를 읽어야 하고, 1-10,11-20 등의 범위에 
# 드는 
# 값들의 횟수를 아래와 같이 출력하여야 한다. 
# 1 - 10 : **** 
# 11 - 20 : ** 
# 21 - 30 : * 
# 31 - 40 : ** 
# .......... 
# .......... 
# .......... 
# 91 -100 : * 

s = '히스토그램을 위한 1부터 100까지의 정수 10개를 임의로 입력하시오. >>>> '
print(s)


temp_array=[]
for n in range(10):
    s='{:d}번째 정수:'.format(n+1)
    temp_value = int ( input(s))
    temp_array.append(temp_value)
print('입력된 수:',temp_array)

temp_array.sort()
print('정렬된 수: ',temp_array)

temp_sort_list=[0 for n in range(10)]
print('히스토그램 초기화 값: ',temp_sort_list)

for i in range(10):
    temp_sort_list[temp_array[i]//10] +=1


print('입력된 숫자 {}개의 히스토그램 분포{}:'.format(sum(temp_sort_list),temp_sort_list))

s=''
for i in range(10):
    s= '{} - {} : '.format(10*i+1,10*(i+1)) + '*'*temp_sort_list[i]
    print(s)
