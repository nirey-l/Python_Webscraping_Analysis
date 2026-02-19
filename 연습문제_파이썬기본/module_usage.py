import datetime
import random

# datetime 모듈 활용
now = datetime.datetime(2026, 2, 19, 14, 30, 25) # 출력 결과 예시에 맞춰 설정
print(f"현재 날짜와 시간: {now}")

# 날짜 포맷 지정 (%A는 요일을 의미합니다)
# 한글 요일 출력을 위해 리스트를 활용할 수도 있지만, 여기서는 포맷 문자열 위주로 작성합니다.
formatted_date = now.strftime("%Y년 %m월 %d일")
# 요일은 별도로 처리 (0: 월요일, 6: 일요일)
days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
weekday = days[now.weekday()]
print(f"포맷된 날짜: {formatted_date} {weekday}")

# random 모듈 활용
# 임의의 정수 (1~10 사이)
rand_int = random.randint(1, 10) 
print(f"임의의 숫자: {rand_int}")

# 임의의 실수 (3.0 ~ 4.0 사이 예시)
rand_float = random.uniform(3.0, 4.0)
print(f"임의의 실수: {rand_float:.2f}")

# 임의의 리스트 요소 선택
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"임의의 리스트 요소: {random.choice(fruits)}")

# 리스트 요소 섞기
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")