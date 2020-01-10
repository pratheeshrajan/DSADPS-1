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
		
	def findFrequentVisitor(self, node):
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

	def inorder(self, startEmpId, endEmpId, outfile):
		outfile.write("Employee attendance: " + "\n");
		def inorderUtil(node):
			if node is not None:
				inorderUtil(node.getLeft());
				if int(node.data) in range(startEmpId, endEmpId):
					if(node.attCtr % 2 == 0 ):
						outfile.write(str(node.data) + "," + str(node.attCtr) + ", out" + "\n");
					else :
						outfile.write(str(node.data) + "," + str(node.attCtr) + ", in" + "\n");
				inorderUtil(node.getRight())

		inorderUtil(self.root)
		
	def maxCountNode(self):
		def maxCountNodeUtil(node):
			if node is not None:
				cc=node.getCount()
				ln=maxCountNodeUtil(node.getLeft())
				rn=maxCountNodeUtil(node.getRight())
				lc=-1
				rc=-1
				if ln is not None:
					lc=ln.getCount()
				if rn is not None:
					rc=rn.getCount()
				if(cc>=lc and cc>=rc):
					return node
				elif lc>=rc:
					return maxCountNodeUtil(node.getLeft())
				else:
					return maxCountNodeUtil(node.getRight())
			return None
		return maxCountNodeUtil(self.root)
	
	
def _readEmployeesRec():
	BT =  BinaryTree()
		
	with open('inputPS1.txt', 'r') as file:
		for line in file:
			BT.addNode(line.strip())
			
	return BT;
	
def _getHeadcountRec(BT):
	return(BT.count_nodes(BT.getRoot()));
	
def _searchIDRec(BT, eId):
	return BT.findNode(BT.getRoot(), eId);
	
def _howOften_Rec(BT, eId):
	node = BT.findNode(BT.getRoot(), empId);
	if node is not None:
		return node.getCount();
	else:
		return 0;


if __name__ == '__main__':

	outfile = open("outputPS1.txt", "w");
	BT = _readEmployeesRec()
	no_of_unique_items = _getHeadcountRec(BT);
	
	outfile.write("Total number of employees came today : " +str(no_of_unique_items) + "\n");
	
	with open('promptsPS1.txt', 'r') as file:
		for line in file:
			whichMethod = line.partition(':')[0].strip();
			empId = line.partition(':')[2].strip();
			if whichMethod == 'searchID':
				node = _searchIDRec(BT, empId);
				if node is None:
					outfile.write("Employee id " + str(empId) + " is absent today " + "\n");
				else:
					outfile.write("Employee id " + str(empId) + " is present today" + "\n");
			
			if whichMethod == 'howOften':
				attCount = _howOften_Rec(BT, empId);
				if(attCount % 2 == 0 ):
					outfile.write("Employee id " + str(empId) + " swiped " + str(attCount) + " times today and is currently outside office " + "\n");
				else :
					outfile.write("Employee id " + str(empId) + " swiped " + str(attCount) + " times today and is currently in office " + "\n");
						
			if whichMethod == 'range':
				splitData = line.partition(':')[2];
				startEmpId = int(splitData.partition(':')[0].strip());
				endEmpId = int(splitData.partition(':')[2].strip()) + 1;
				BT.inorder(startEmpId, endEmpId, outfile);

	swipedMost = BT.maxCountNode();
	outfile.write("Employee id " + str(swipedMost.getData()) + " swiped the most number of times today with a count of " + str(swipedMost.getCount()));
	
	print("Done!, check the output  file : " + outfile.name + "\n");
	
	outfile.close()
	
