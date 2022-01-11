'''산 모양으로 별 출력하기
표준 입력으로 삼각형의 높이가 입력됩니다.
입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요.
(input에서 안내 문자열은 출력하지 않아야 합니다.)
이때 출력 결과는 예제와 정확히 일치해야 합니다.
모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.
'''
count=int(input())                   # count가 3이라고 가정했을 때
for i in range(count):               # i = 1 2 3
    for j in reversed(range(count)): # j = 3 2 1
        if j > i:  
            print(' ', end='')       # j가 크면 공백
        else:
            print('*', end='')       # j가 작으면 '*'
    for j in range(count):           # j = 1 2 3
        if j < i:
            print('*', end='')       # j가 작으면 '*'
    print()                          # 개행
'''
j=3 |  *
j=2 | **|*
j=1 |***|**
1번 if문|2번 if문
'''