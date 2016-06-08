class bTree:
	__init__(self, val):	
		self.val = val
		self.left = None
		self.right = None
		
		
def depth(tree):
	if tree == None:
		return 0
	if tree.left == None and tree.right == None:
		return 1
	else:
		depthLeft = depth(tree.left) + 1
		depthRight = depth(tree.right) + 1
		return max(depthLeft, depthRight)

def depthLists(node, lists={}, d = none):
	if d == None:
		d = depth(node)
	if lists.get(d) == None:
		lists[d] = LinkedList(node.val)
	else:
		lists[d].add(node.val)
		if d == 1:
			return lists
	if node.left is not None:
		lists = depthLists(node.left, lists, d-1)
	if tree.right is not None:
		lists = depthLists(node.right, lists, d-1)
	return lists
