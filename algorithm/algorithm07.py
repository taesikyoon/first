# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가
# 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
# 고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
# 하는 프로그램을 작성하세요.
# 만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
# 은 22입니다.
#
# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력
# 된다.
#
# ▣ 출력설명
# 첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
# 완전탐색

#오늘의 구글링!
#   https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
#   랜덤숫자를 생성해주는 라이브러리와 numpy 라이브러리 추가 설치




# 1부터 100까지의 자연수가 적힌 N장의 카드를 가지고 있다 (같은 숫자의 카드가 여러장 있을수 있다.)
# generate random integer values
from numpy.random import seed
from numpy.random import randint


def soultion(list,N,K):
    sum_nums=0
    result=[]
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                sum_nums =list[i]+list[j]+list[k]
                result.append(sum_nums)
    result.sort(reverse=True)
    # print(result)
    return result[K-1]
######
N = int(input("몇 장의 카드를 가져올까요? >>> "))
N = N if 3<=N<=100 else False
K = int(input("몇 번째 큰 값을 원하시나요? >>> "))
K = K if 1<=K<=50 else False

seed(1)
values = randint(0, 100, N)
card_list=list(int(i) for i in values)
card_list.sort(reverse=True)
# print(card_list)

print(soultion(card_list,N,K))

# 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다.
# 계속 머리속으로 패턴을 찾는데 생각이 안나서 경우의 수를 공부한다
# 추가로 나중에 정리해둘것 계승(factorial) 알고리즘 >>> 팩토리얼은 재귀함수를 사용한다 공부해두기!
# 본론으로 와서 순열과 조합의 공부가 필요해보이며 조합방식을 쓰는거같다
# https://blog.naver.com/minsik77777/222589708397





# 10부제 쉬운문제
# 날짜가 주어진다 ex) 2일 or 9일
# 차 리스트를 살펴보고 12 22 32 2 or 9 19 29

days=input("오늘 날짜: ")
# days= '2'

car_list= list(map(str,input().split()))
# car_list=["10",'11','12','13','21','41','20']
count =0
for car in car_list:
    print(car)
    if days in car[1]: count+=1
print("오늘 위반 한 차량의 수: ",count)


