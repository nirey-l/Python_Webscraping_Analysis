import math_operations

# 원의 넓이 (반지름 5)
area_c = math_operations.circle_area(5)
print(f"원의 넓이: {area_c:.2f}")

# 직사각형 넓이 (가로 10, 세로 5)
area_r = math_operations.rectangle_area(10, 5)
print(f"직사각형 넓이: {area_r}")

# 팩토리얼 (5!)
fact_5 = math_operations.factorial(5)
print(f"팩토리얼 5! = {fact_5}")

# 최대공약수 (48, 18)
gcd_val = math_operations.gcd(48, 18)
print(f"최대공약수(48, 18) = {gcd_val}")