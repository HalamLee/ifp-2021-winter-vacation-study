'''''''''''''''''''''
31. 10진수를 입력받아 8진수(octal)로 출력해보자.
'''''''''''''''''''''

x = int(input())
print(oct(x)[2:])

'''''''''''''''''''''
32. 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
'''''''''''''''''''''

x = int(input())
print(hex(x)[2:])

'''''''''''''''''''''
33. 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
16진수(대문자)로 출력한다.
'''''''''''''''''''''

x = hex(int(input()))[2:]
print(x.upper)

'''''''''''''''''''''
34. 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
'''''''''''''''''''''

x = '0o' + input()
print(int(x, 8))

'''''''''''''''''''''
35. 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
'''''''''''''''''''''

x = int('0x' + input(), 16)
print(oct(x)[2:])

'''''''''''''''''''''
36. 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
아스키 코드란? 문자를 이진수의 7비트로 표현한 것
ex) A => 1100001
'''''''''''''''''''''

x = ord(input())
# ord() 함수는 아스키 코드를 반환한다.
print(x)

'''''''''''''''''''''
37. 10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
'''''''''''''''''''''

x = chr(int(input()))
print(x)
