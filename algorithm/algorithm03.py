def solution(n):
    nums=list(map(int,(input().split())))
    print(nums)
    first = nums[0]
    # if len(nums) == n :
    #     for x in range(len(nums)):
    #         if first != nums[x]:
    #             if solution02(first) < solution02(nums[x]) :
    #                 first = nums[x]
    #             elif solution02(first) == solution02(nums[x]):
    #                 first = (first if first>nums[x] else nums[x])
    # return first

def solution02(n):
    N=[int(i) for i in str(n)]
    return sum(N)

print(solution(7))
#128 460 603 40 521 137 123