from functools import lru_cache


class Solution:
    def decodeWays(self, s):
        return self.recursiveWithMemo(0, s)
        lru_cache(maxsize=None)

    def recursiveWithMemo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer


T = int(input("Enter no. of test cases: "))
for _ in range(T):
    s = str(input("Enter the string: "))
    Obj = Solution()
    ans = Obj.decodeWays(s)
    print(ans)
