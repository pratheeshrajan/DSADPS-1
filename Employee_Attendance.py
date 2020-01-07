import sys

class EmpNode(object):
	def __init__(self,data):
		self.data = data
		self.left = self.right = None
		self.attCtr = 1

	def __str__(self):
		return "("+str(self.data)+", "+str(self.attCtr)+")";

	def getData(self):
		return self.data

	def getCount(self):
		return self.attCtr

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setLeft(self, node):
		self.left = node

	def setRight(self, node):
		self.right = node

	def incCount(self):
		self.attCtr+=1

class BinaryTree(object):
	def __init__(self):
		self.root = None
		
	def count_nodes(self, node):
		if node is None:
			return 0
		return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

	def isEmpty(self):
		return False

	def getRoot(self):
		return self.root;
		
	def findNode(self, node,data):
		if node is not None:
			if(str(node.getData()) == str(data)):
				return node;
			else:
				return self.findNode(node.getLeft(),data) or self.findNode(node.getRight(),data)	
		return None
		
	def search(self, node,data):
		if node is not None:
			if(node.getData()==data):
				node.incCount()
				return True
			else:
				return self.search(node.getLeft(),data) or self.search(node.getRight(),data)	
		return False

	def addNode(self,data):
		def getHeight(node):
			if(node!=None):
				return 1 + max(getHeight(node.getLeft()),getHeight(node.getRight()))
			return 0

		def addUtil(node,data):
			if node is not None:
				lh=getHeight(node.getLeft())
				rh=getHeight(node.getRight())
				if(lh>rh):
					node.setRight(addUtil(node.getRight(),data))
				else:
					node.setLeft(addUtil(node.getLeft(),data))
				return node
			return EmpNode(data)

		if not self.search(self.root,data):
			self.root=addUtil(self.root,data)

	def preorder(self):
		def preorderUtil(node):
			if node is not None:
				print(node)
				preorderUtil(node.getLeft())
				preorderUtil(node.getRight())

		preorderUtil(self.root)

	def inorder(self):

		def inorderUtil(node):
			if node is not None:
				inorderUtil(node.getLeft())
				print(node)
				inorderUtil(node.getRight())

		inorderUtil(self.root)

	def postorder(self):

		def postorderUtil(node):
			if node is not None:
				postorderUtil(node.getLeft())
				postorderUtil(node.getRight())
				print(node)

		postorderUtil(self.root)

if __name__ == '__main__':
	
	Read_List=[]

	with open('inputPS1.txt', 'r') as f:
		Read_List=f.readlines()

	Read_List=[int(i) for i in Read_List]

	BT= BinaryTree()

	for data in Read_List:
		BT.addNode(data)
	
	print ("Total number of employees came today")
	print(BT.count_nodes(BT.getRoot()));
	
	with open('promptsPS1.txt', 'r') as file:
		for line in file:
			node = BT.findNode(BT.getRoot(), line.partition(':')[2].strip())
			if node is None:
				print ("Employee id " + str(line.partition(':')[2].strip()) + " is absent today.")
			else:
				print ("Employee id " + str(line.partition(':')[2].strip()) + " is present today.")



	print("\n")
