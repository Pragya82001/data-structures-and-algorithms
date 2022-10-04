class Solution:
    def houseRobber(self, nums):
        n = len(nums)
        even = [nums[x] for x in range(n) if x % 2 == 0]
        odd = [nums[x] for x in range(n) if x % 2 != 0]

        if(sum(even) > sum(odd)):
            return sum(even)
        return sum(odd)




T = int(input("Enter Test Cases: "))
for _ in range(T):
    nums = list(map(int, input().strip().split()))
    obj = Solution()
    ans = obj.houseRobber(nums)
    print(ans)