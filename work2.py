#문제 1: 리스트에서 중복된 숫자 제거하기
#주어진 리스트에서 중복된 숫자를 제거하고, 
#중복되지 않은 숫자들만 포함된 새로운 리스트를 반환하는 함수를 작성하세요.

def remove_duplicates(numbers):
    set_data = set(numbers)   # set으로 변환
    list_data = list(set_data)  # 리스트로 변환
    return  list_data

# 테스트
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  # [1, 2, 3, 4, 5]
