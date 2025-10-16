class Solution:
	def constructTransformedArray(self, nums: List[int]) -> List[int]:
		n = len(nums)
		res = [0] * n
		for i in range(n):
			if nums[i] == 0:
				res[i] = 0
			else:
				index = (i + nums[i]) % n
				res[i] = nums[index]
		return res