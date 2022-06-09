# 소수를 구하는 함수 만들기
# 소수는 약수가 1과 자기 자신뿐인 자연수
# 첫번째 (소수 판별)
#[32, 55, 62, 20, 250, 370, 200, 30, 100]
num_list =[32, 55, 62, 20, 250, 370, 200, 30, 100]
# def solution(list):
#     hello = "약수가 아니올시다"
#     if num == 1: return hello
#     for x in range(2,(int(num/2))):
#         if num % x == 0: return hello
#         else :
#

# 23 1 23
#[32, 55, 62, 20, 250, 370, 200, 30, 100]
def solution(list):
    result =[]
    for num in list:
        for x in range(2,num):
            print(x)
            if num % x == 0: break
            else :
                result.append(num)
                break

    return result

def reverse(list):
    temp_list=[str(i) for i in list]
    result=[]

    for x in temp_list:
        result.append(int(((x[::-1]))))

    return solution(result)


print(reverse(num_list))
#실패 졸려서 내일 마무리하기





