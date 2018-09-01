import time


class Solution:
    def find_n_sum(self, sorted_nums, target, n, result_prefix, results):
        nums_len = len(sorted_nums)
        if n > nums_len:
            return -1

        ## as sorted_nums is a sorted list, we can simplify some special conditions
        if (target < sorted_nums[0] * n) or (target > sorted_nums[-1] * n):
            return -2

        if n == 1:
            for num in sorted_nums:
                if num == target:
                    results.append([num])
                    return 0
            return -2
        elif n == 2:
            ## find 2 elements in list whose sum is target
            idx_l, idx_r = 0, nums_len - 1
            while idx_l < idx_r:
                element_sum = sorted_nums[idx_l] + sorted_nums[idx_r]
                if element_sum < target:
                    idx_l += 1
                elif element_sum > target:
                    idx_r -= 1
                else:
                    ## a 2-element tuple is found
                    ## add this solution into results list
                    aux = result_prefix + [sorted_nums[idx_l], sorted_nums[idx_r]]
                    results.append(aux)

                    idx_l += 1
                    idx_r -= 1

                    ## to pass duplicate elements in list
                    while (idx_l < idx_r) & (sorted_nums[idx_l] == sorted_nums[idx_l - 1]):
                        idx_l += 1
                    while (idx_l < idx_r) & (sorted_nums[idx_r] == sorted_nums[idx_r + 1]):
                        idx_r -= 1
            return 0
        else:
            ## Try the SMALLEST element sorted_nums[i] in the n-tuple
            ##  and find the other (n-1)-tuple in remaining list sorted_nums[i+1:]
            for i in range(0, len(sorted_nums) - n + 1):
                if sorted_nums[i] * n > target:
                    break
                elif (i > 0) & (sorted_nums[i] == sorted_nums[i - 1]):
                    pass
                else:
                    self.find_n_sum(sorted_nums[i + 1:],
                                    target - sorted_nums[i],
                                    n - 1,
                                    result_prefix + [sorted_nums[i]],
                                    results)

    def fourSum(self, nums, target):
        sorted_nums = sorted(nums)
        results = []
        self.find_n_sum(sorted_nums, target=target, n=4, result_prefix=[], results=results)

        return results

sln = Solution()

begin = time.clock()
nums = [1, 0, -1]
expect = []
target = 10
print("TestCase1: ", sln.fourSum(nums, target) == expect, " ——take %.3f ms" % ((time.clock() - begin) * 1000))

nums = [1, 0, -1, 0, -2, 2]
target = 0
expect = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
expect.sort()
begin = time.clock()
actual = sln.fourSum(nums, target)
end = time.clock()
actual.sort()
print("TestCase2: ", actual == expect, " ——take %.3f ms" % ((end - begin) * 1000))

nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
expect = [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3],
          [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
expect.sort()
begin = time.clock()
actual = sln.fourSum(nums, target)
end = time.clock()
actual.sort()
print("TestCase3: ", actual == expect, " ——take %.3f ms" % ((end - begin) * 1000))