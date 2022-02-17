# while 문의 실습
# while 문은 조건을 정해놓고 반복을 하는 구조

i = 0
while i < 3:
    print("안녕하세요.")
    i += 1      # 만약 좌측 코드가 없다면 while 문은 무한 루프를 돌 것임
print("반복 종료.")

# 숫자 0~4까지 줄바꿈을 하지 않고 출력(while 문 사용)
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print("")
print("-------------------")
# 1~5까지의 누계합을 구하는 예제
i = 1
hap = 0

while i <= 5: # i < 11보다 가독성이 좋음
    hap += i
    i += 1
print("1~5까지의 누계합 : ", hap)

# while 문을 사용하여 팩토리얼을 구하는 예제
# f(1) = 1
i = 1
fa = 1

while i <= 5:
    fa *= i
    i += 1
print("5!의 값은 %d 입니다." % fa)

print("------------------------")
# while 문을 사용하여 5단을 출력하는 예제
i = 1
while i <= 9:
    # % 뒤에 오는 숫자들은 출력할 때 자릿수 차지하게끔 만들어줌
    # %.1f나 %0.1f나 동일한 자릿값을 출력함(소수점 첫째자리만 나타내도록 함)
    print("5 * %d = %2d" % (i, 5*i))
    i += 1
print("------------------------")
# 1~50까지의 5의 배수만 누적값을 구하는 예제
i = 1
hap = 0
while i <= 50:
    # 5의 배수인지 확인하는 조건
    if (i % 5) == 0:
        hap += i
    i += 1

print("1부터 50사이의 모든 5의 배수의 합은 %d입니다." % hap)
print("------------------------")

# 정수 안의 각 자리수의 합을 계산하는 예제
# 예를 들면 1234라면 (1+2+3+4)를 계산함
num = 4567
hap = 0
while num > 0:
    digit = num % 10    # 해당하는 자릿수의 값을 구하는 코드
    hap += digit
    num = num // 10     # 10으로 나누어줌으로써 몫만 num 에 저장되는 코드

print("4567정수의 자리수의 합: %d" % hap)

# shift + f9 -> 디버깅 모드
