
# 현수네 반 선생님은 반 학생들의 수학점수를 향상시키기 위해 멘토링 시스템을 만들려고 합니
# 다. 멘토링은 멘토(도와주는 학생)와 멘티(도움을 받는 학생)가 한 짝이 되어 멘토가 멘티의
# 수학공부를 도와주는 것입니다.
# 선생님은 M번의 수학테스트 등수를 가지고 멘토와 멘티를 정합니다.
# 만약 A학생이 멘토이고, B학생이 멘티가 되는 짝이 되었다면, A학생은 M번의 수학테스트에서
# 모두 B학생보다 등수가 앞서야 합니다.
# M번의 수학성적이 주어지면 멘토와 멘티가 되는 짝을 만들 수 있는 경우가 총 몇 가지 인지
# 출력하는 프로그램을 작성하세요.
#
# ▣ 입력설명
# 첫 번째 줄에 반 학생 수 N(1<=N<=20)과 M(1<=M<=10)이 주어진다.
# 두 번째 줄부터 M개의 줄에 걸쳐 수학테스트 결과가 학생번호로 주어진다. 학생번호가 제일
# 앞에서부터 1등, 2등, ...N등 순으로 표현된다.
# 만약 한 줄에 N=4이고, 테스트 결과가 3 4 1 2로 입력되었다면 3번 학생이 1등, 4번 학생이
# 2등, 1번 학생이 3등, 2번 학생이 4등을 의미합니다.
#
# ▣ 출력설명
# 첫 번째 줄에 짝을 만들 수 있는 총 경우를 출력합니다.

#   https://www.w3schools.com/python/ref_random_shuffle.asp 셔플 함수

# 조건은 어떻게 맞추는지 이제 슬슬 궁금하다

# M=int(input())
# M = M if (1 <= M <= 10) else False
# N=int(input())
# N = N if (1 <= N <= 20) else False

# def list_test(N,M):
#     temp=[]
#     result=[]
#     for i in range(M):
#         for x in range(N):
#             temp.append(int(input()))
#         result.extend([temp])
#         temp=[]
#         print("현재 리스트 보기",result)
#
# list_test(4,3)

sample=[[3, 4, 1, 2], [4, 3, 2, 1], [3, 1, 4, 2]]
temp=[]
for i in range(3):
    criterion=sample[i][0]
    # print("criterion=[",i,"]","[0]")
    for x in range(4):
        if criterion > sample[i][x]:
            temp.append([criterion,sample[i][x]])
print(temp)
new_temp=[]
for a in range(len(temp)):
    if temp[a][0] > temp[a][1] :
        new_temp.append([sample[a][0]], sample[a][1]])
print(new_temp)


# 눈이 너무 아파졌어서 해결 못하겠다... 집중도 안되고 내일 또 하는걸로!
