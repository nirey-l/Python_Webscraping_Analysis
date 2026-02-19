import math

def circle_area(radius):
    """원의 넓이를 계산합니다."""
    return math.pi * (radius ** 2)

def rectangle_area(width, height):
    """직사각형의 넓이를 계산합니다."""
    return width * height

def factorial(n):
    """재귀를 이용해 팩토리얼을 계산합니다."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    """두 수의 최대공약수를 계산합니다."""
    return math.gcd(a, b)