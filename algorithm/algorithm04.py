# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 소수를 출력하
# 는 프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출
# 력한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
#
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 100,000를 넘지 않는다.
#
# ▣ 출력설명
# 첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
# 0610 https://www.programiz.com/python-programming/examples/prime-number 구글링 자료!

# 첫번째 (소수 판별)
#[32, 55, 62, 20, 250, 370, 200, 30, 100]

nums=list(map(int,(input().split())))

def solution(list):
    temp_list=[str(i) for i in list]
    result=[]

    for x in temp_list:
        result.append(int(((x[::-1]))))

    return check_prime(result)

# 소수확인 함수
def check_prime(list):
    result_list = []
    for num in list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0: break
            else:
                result_list.append(num)
    return result_list

print(solution(nums))
#[32, 55, 62, 20, 250, 370, 200, 30, 100]