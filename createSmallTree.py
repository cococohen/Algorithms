class TreeNode(self, x):
	self.val = x
	self.left = None
	self.right = None


class sortedArrayToBST:
		
	def createSmallTree(self, nums):
		return self.sortedArrayToBST(nums, 0, len(num)-1)
		
	def sortedArrayToBST(self, nums, begin, end):
		if begin > end:
			return None
		midpoint = (begin+end)//2
		root = TreeNode(nums[midpoint])
		root.left = self.sortedArrayToBST(nums, begin, midpoint-1)
		root.left = self.sortedArrayToBST(nums, midpoint+1, end)
		return root
		
		
