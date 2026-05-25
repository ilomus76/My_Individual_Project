'''문제 9. 
아래의 모습으로 데이터가 출력되도록 하자. [이스케이프 문자 사용] 
—----------------------------- 
번호 이름 나이 전공 주소 
—----------------------------- 
1 
2 
3 
sam 20 web seoul 
robin 25 
ai 
busan 
park 30 data incheon '''



print('—----------------------------- ')
print('번호\t이름\t나이\t전공\t주소\n')  # \t는 8칸을 사용.
print('1\tsam\t20\tweb\tseoul\n')
print('2\trobin\t25\tai\tbusan\n')
print('3\tpark\t30\tdata\tincheon\n')
print('—----------------------------- ')
print()


print('—----------------------------- ')
print('{}\t{}\t{}\t{}\t{}\n'.format('번호','이름','나이','전공','주소'))  # \t는 8칸을 사용.
print('{}\t{}\t{}\t{}\t{}\n'.format(1,'sam',20,'web','seoul'))
print('{}\t{}\t{}\t{}\t{}\n'.format(2,'robin',25,'ai','busan'))
print('{}\t{}\t{}\t{}\t{}\n'.format(3,'park',30,'data','incheon'))
print('—----------------------------- ')




print('—----------------------------- ')
print(f'{'번호'}\t{'이름'}\t{'나이'}\t{'전공'}\t{'주소'}\n')  # \t는 8칸을 사용.
print(f'{1}\t{'sam'}\t{20}\t{'web'}\t{'seoul'}\n')
print(f'{2}\t{'robin'}\t{25}\t{'ai'}\t{'busan'}\n')
print(f'{3}\t{'park'}\t{30}\t{'data'}\t{'incheon'}\n')
print('—----------------------------- ')

