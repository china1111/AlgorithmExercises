'''
    @author: NightGaunt
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = 0
        i = 0
        j = 0
        if len(nums) < 1 or nums == None:
            return 0
        while i <= len(nums):
            i += 1
            while sum(nums[j:i]) < s and i < len(nums):
                i += 1
            while sum(nums[j:i]) >= s and j <= i:
                j += 1
            if sum(nums[j-1: i] if j > 0 else nums[j:i]) >= s and (i - j + 1 < length or length == 0):
                length = i - j + 1
        return length

'''
    答案
'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 复杂度是O(n): Accepted
        # 这里计算复杂度的方法就是计算i和j两个指针最多的移动次数，每次都是n次
        i, j, r = 0, 0, len(nums) + 1
        sums = [] # 通过创建一个数组来将求和的复杂度从O(N)减到O(1)
        for num in nums:
            if not sums:
                sum.append(num)
            else:
                sums.append(sums[-1] + num)
        while i < len(nums) and j < len(nums):
            if sums[j] - sums[i] + nums[i] < s:
                j += 1
            else:
                if j + 1 - i < r:
                    r = j + 1 - i
                i += 1
        if r != len(nums) + 1:
            return r
        else:
            return 0
