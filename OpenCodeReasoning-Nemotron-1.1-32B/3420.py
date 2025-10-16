class Solution:
	def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
		indices = [i for i, num in enumerate(nums) if num == x]
		res = []
		for q in queries:
			if q > len(indices):
				res.append(-1)
			else:
				res.append(indices[q-1])
		return res