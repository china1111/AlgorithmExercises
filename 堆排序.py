'''


'''

class Solution:
    def findKthLargest(self, nums, k):
        '''
        self._k = len(nums) - k
        return self.quicksort(nums, 0, len(nums) - 1)
        '''

        self._k = len(nums) - k
        return self.heapsort(nums)

        '''
        self._k = len(nums) - k
        return self.merge_sort(nums)[self._k]
        '''

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        r = []
        while left and right:
            if left[0] > right[0]:
                r.append(right.pop(0))
            else:
                r.append(left.pop(0))
        if left:
            r += left
        if right:
            r += right
        return r

    def heapsort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, self._k - 1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)
        return nums[self._k]

    def build_heap(self, nums):
        length = len(nums)
        for i in range(((length-1) // 2), -1, -1):
            self.max_heapify(nums, i, length)

    def max_heapify(self, nums, i, length):
        left = i * 2 + 1
        right = i * 2 + 2
        if left < length and nums[left] > nums[i]:
            largest = left
        else:
            largest = i
        if right < length and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.max_heapify(nums, largest, length)

    def quicksort(self, nums, left, right):
        if left == right:
            return nums[left]
        pivot = self.partition(nums, left, right)
        if pivot == self._k:
            return nums[pivot]
        elif pivot < self._k:
            return self.quicksort(nums, pivot + 1, right)
        else:
            return self.quicksort(nums, left, pivot-1)

    def partition(self, nums, left, right):
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[i] >= pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        return i


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

