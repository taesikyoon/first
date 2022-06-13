from numpy.random import seed
from numpy.random import randint

N = int(input())
N = N if 1<= N <= 100 else False
M = int(input())
M = M if 1<= M <= 100 else False

seed(1)
values = randint(0, 100, N)
N_list= list(int(i) for i in values)
N_list.sort(reverse=True)
print(N_list)

values = randint(0, 100, M)
M_list=list(int(i) for i in values)
M_list.sort(reverse=True)
print(M_list)

result=N_list+M_list
result.sort(reverse=True)
print(result)
print(type(result[0]))


일곱난쟁이 문제
# test=[20, 7, 23, 19, 10, 15, 25, 8, 13] #20 7 23 19 10 15 25 8 13 >>짝수를 먼저
test=[20, 30, 10, 7, 6, 14, 12, 8, 13] #>>> 100
resul=[20 30 10 6 14 12 8]
# 100 이 난쟁이가 진짜 아닌지 1차조건
# 1

def solution(list):
    result=[]
    count = 0
    dwarf = 0
    for i in range(len(list)):
        if i == count:
            if test[i] % 2== 0:
                result.append(test[i])
                if sum(result) < 100:
                    count += 1
                    dwarf += 1
                elif sum(result) > 100:
                    del test[i]
                    count += 1
                else :
                    dwarf += 1
                    if dwarf == 7 :
                        print("일곱난쟁이를 구별해냈어요!",result)
                        break
                    else:
                        del test[i]
                        count +=1
                        print("가짜 난쟁이가 있어서 너무 빨리 완성 되었어요")
            else:
                for k in range(i+1,len(list)):
                    if test[i]+test[k] % 2 == 0:
                        result.append(test[i])
                        if sum(result) < 100:
                            count += 1
                            dwarf += 1
                        elif sum(result) > 100:
                            del test[i]
                            count += 1
                        else:
                            dwarf += 1
                            if dwarf == 7:
                                print("일곱난쟁이를 구별해냈어요!", result)
                                break
                            else:
                                del test[i]
                                count += 1
                                print("가짜 난쟁이가 있어서 너무 빨리 완성 되었어요")
                    else:

    return result

print(solution(test))


