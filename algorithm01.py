# 세 수중 최솟값 구하기

# 1번째 내장함수 쓰기
num_list=list(map(int, input().split()))
print(min(num_list))


# 2번째 직접 비교해보기
smal = num_list[0]
for i in num_list:
    if i < smal:
        smal = i
print(smal)