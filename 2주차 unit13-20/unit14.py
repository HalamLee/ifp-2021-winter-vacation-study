'''합격 여부 판단하기
표준 입력으로 국어, 영어, 수학, 과학 점수가 이볅됩니다.
여기서 네 과목의 평균 점수가 80점 이상일 때 합격이라고 정했습니다.
평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램을 만드세요.
(input에서 안내 문자열은 출력하지 않아야 합니다.)
단 점수가 0점부터 100점까지만 입력받을 수 있으며 범위를 벗어났다면
'잘못된 점수'를 출력하고 합격, 불합격 여부는 출력하지 않아야 합니다.
'''
korean, english, math, science = map(int,input().split())
avg = (korean + english + math + science) / 4
if 0 <= korean <=100 and 0 <= english <=100 and 0 <= math <=100 and 0 <= science <=100:
    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:#모든 점수가 0~100사이의 값
    print('잘못된 점수')
