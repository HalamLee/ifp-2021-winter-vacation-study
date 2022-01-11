'''5와 7의 배수, 공배수 처리하기
표준 입력으로 정수 두 개가 입력됩니다.
(첫 번째 입력 값의 범위는 1~1000, 두 번째 입력 값의 범위는 10~1000이며
첫 번째 입력 값은 두번째 입력값보다 항상 작습니다.)
첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서 5의 배수일 때는 'Fizz',
7의 배수일 때는 'Buzz', 5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램을 만드세요.
(input에서 안내 문자열은 출력하지 않아야 합니다.)
'''
start, stop = map(int, input().split())
for i in range(start, stop+1): # start부터 stop까지
    if i % 35 == 0:            # 5와 7의 최소공배수 35
        print('FizzBuzz')
    elif i % 5 == 0:           # 5의 배수
        print('Fizz')
    elif i % 7 == 0:           # 7의 배수
        print('Buzz')
    else:                      # 나머지
        print(i)
