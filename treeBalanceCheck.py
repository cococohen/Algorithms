#check if a binary tree has hights of two subtrees of any node do not
#differ by more than one

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right= None


class BalanceCheck:

	def isBalancedInt(self, root):
		if root is Null:
			return 0
		left = self.isBalancedInt(root.left) 
		right = self.isBalanced(node.right)
		if left < 0 or right < 0 or abs(left-right)>1:
			return -1
		return max(left,right)+1
	
	def isBalanced(self, root):
		return isBalancedInt(root)>=0
			
