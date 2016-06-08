def checkBST(node, min, max): #start out by sending the root node
	if node is None:
		return True
	
	if node.data < min or node.data >= max:
		return False
		
	if (not(checkBST(node.left, min, node.data))) or (not (checkBST(node.right, node.data, max))):
		return False
		
	return True

