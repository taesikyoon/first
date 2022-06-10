# 길이가 서로 다른 A, B, C 세 개의 막대 길이가 주어지면 이 세 막대로 삼각형을 만들 수 있으면 “YES"를 출력하고, 만들 수 없으면 ”NO"를 출력한다

#삼각형의 조건  a+b>c, b+c>a, c+a>b

triangle = list(map(int,(input().split())))
if triangle[0]+triangle[1] > triangle[2] and triangle[1]+triangle[2] > triangle[0] and triangle[2]+triangle[0] > triangle[1]:
        print('삼각형에 된다이')
else : print('삼각형이 못되네')

def solution(a,b,c):
        answer = 'Yes'
        if a+b > c and b+c > a and c+a > b : answer
        else: answer = 'No'
        return answer

print(solution(23,31,12))

#이름 정리하기! 삼각형의 조건
