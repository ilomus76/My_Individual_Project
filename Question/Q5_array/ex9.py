# 문제 9. 
# 리스트를 이용하여 간단한 극장 예약 시스템을 작성하여 보자. 아주 작은 극장이라서 
# 좌석이 10개 밖에 안 된다. 사용자가 예약을 하려고 하면 먼저 좌석 배치표를 보여준다. 
# 즉, 예약이 끝난 좌석은 1로, 예약이 안된 좌석은 0으로 나타낸다. 
# 좌석을 예약하시겠습니까( 1(Y) 또는 0(N) )?  1 
# 현재의 예약 상태는 다음과 같습니다. ---------------------------------------- 
# 좌석 번호 :  1  2  3  4  5  6  7  8  9  10 ---------------------------------------- 
# 예약 상태 :  0  0  0  0  0  1  1  1  0   1 
# 몇번째 좌석을 예약하시겠습니까? 6 
# 죄송합니다. 이미 예약된 좌석입니다. 다른 좌석을 선택해 주세요. 
# 몇번째 좌석을 예약하시겠습니까? 1 
# 1번 좌석 예약되었습니다. 
# 좌석을 예약하시겠습니까( 1(Y) 또는 0(N) )?  0 
# 예약을 종료합니다. 

seat_number = list(range(1,11))
print('seat number(좌석번호)          : ', seat_number)

reserved_status = [0,0,0,0,0,1,1,1,0,1]
print('reserved status(현재 예약 상태):',reserved_status)
seat_reserving_number =int(input('몇번째 좌석을 예약하시겠습니까?'))
if reserved_status[seat_reserving_number-1] ==1:
    print('죄송합니다. 이미 예약된 좌석입니다. 다른 좌석을 선택해 주세요.')
    seat_reserving_number =int(input('몇번째 좌석을 예약하시겠습니까?'))

print(f'{seat_reserving_number} 좌석 예약되었습니다.')
question_s = '좌석을 예약하시겠습니까? ( 1(Y) 또는 0(N))? '
reserved_status[seat_reserving_number-1] = int(input(question_s))
print('현재의 좌석 예약 상태입니다: ', reserved_status)
print('예약을 종료합니다')

