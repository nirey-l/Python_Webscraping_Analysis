import os
import sys

# 현재 작업 디렉토리 및 시스템 정보
print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")

# 환경 변수 PATH의 일부 출력 (가독성을 위해 첫 번째 경로만 출력하거나 일부 슬라이싱)
path_env = os.environ.get('PATH', '')
print(f"환경 변수 PATH 일부: {path_env.split(os.pathsep)[0]}")

# 파일 경로 다루기
file_path = "/Users/username/documents/report.txt"

# 경로에서 디렉토리와 파일명 분리
directory = os.path.dirname(file_path)
filename = os.path.basename(file_path)
# 파일명과 확장자 분리
name, extension = os.path.splitext(filename)

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {extension}")

# 파일 존재 여부 확인
# 실제 해당 경로에 파일이 없으므로 False가 출력됩니다.
exists = os.path.exists(file_path)
print(f"파일 존재 여부: {exists}")