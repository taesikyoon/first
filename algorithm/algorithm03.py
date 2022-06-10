# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
# 하는 프로그램을 작성하세요. 자릿수의 합이 같은 경우 원래 숫자가 큰 숫자를 답으로 합니다.
# 만약 235 와 1234가 동시에 답이 될 수 있다면 1234를 답으로 출력해야 합니다.
#
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 10,000,000를 넘지 않는다.

def solution(n):
    nums=list(map(int,(input().split())))
    first = nums[0]
    if len(nums) != n : return False
    else :
        for x in range(len(nums)):
            if first != nums[x]:
                if solution02(first) < solution02(nums[x]) :
                    first = nums[x]
                elif solution02(first) == solution02(nums[x]):
                    first = (first if first>nums[x] else nums[x])
    return first

def solution02(n):
    N=[int(i) for i in str(n)]
    return sum(N)

print(solution(7))
#128 460 603 40 521 137 123
# 6월 10일 수정내용
# N개의 자연수가 제대로 입력되지않으면 false 반환하도록 만듬 >>> 이유 : 제대로 된 값이 입력되지않아도 반환되는 값이 따로 존재했었음