# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.
# 선생님은 출석부를 보고 번호를 부르는데, 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.
# 그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러 이름과 얼굴을 빨리 익히려고 하는 것이다.
# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 10
# 1 3 2 2 5 6 7 4 5 9

# 출력
# 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
# 1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# Tip::
# 파이썬에서는 배열의 비어있는 공간을 미리 확보해 놓을 수 없다.따라서 필요한 갯수 만큼 '어떠한 값'으로 초기화 시켜주어야 한다.
# ex) LIST = list(range(23)) >> 0~22번지까지 0-22의 숫자들로 채워진다.
# ex) LIST = [0 for _ in range(23)] >> 0~22번지까지 0으로 채워진다.
# 호출되는 번호(주소값)의 값을 기존 값에서 +1하여 저장해주는 방식으로 해당 번호가 몇 번 호출되었는지 카운트할 수 있다.
# 아래 코드에서 '*(Asterisk)'를 사용한 이유
# 문제에서 원하는 출력값은 리스트 형태가 아닌, 내부의 원소를 그대로 출력하길 요구했기 때문이다.

# 내 풀이)
call = int(input())
randomCall = map(int, input().split())
count = list(range(23))
for n in count:
    count[n] -= n 
for i in randomCall:
    count[i-1] += 1
print(*(count))
# 강의 풀이)
n = int(input())
rand = map(int, input().split())
student = [0 for _ in range(23)]
for r in rand:
  student[r-1] += 1
print(*student)