# How to run: Open the shell and enter the command: python Employee_Attendance.py inputPS1.txt
import sys

# Python3 program to construct binary 
# tree from given array in level 
# order fashion Tree Node 

# Helper function that allocates a 
#new node 
class EmpNode: 
	def __init__(self, data):
		self.data = data 
		self.left = self.right = None
		self.attCtr = 1
	def __str__(self):
		return self.data + " attCtr: " + str(self.attCtr)
		

# Function to insert nodes in level order 
def insertLevelOrder(arr, root, i, n):
	# Base case for recursion
	if i < n:
		temp = EmpNode(arr[i])
		root = temp
				
		# insert left child 
		root.left = insertLevelOrder(arr, root.left, 
									2 * i + 1, n)
		# insert right child 
		root.right = insertLevelOrder(arr, root.right, 
									2 * i + 2, n)
	
	return root

# Function to print tree nodes in 
# InOrder fashion 
def inOrder(root):
	if root != None:
		inOrder(root.left)
		print(str(root.data) + " counter : " + str(root.attCtr))
		inOrder(root.right)
		
		
def main():
	empList = []
	if not len(sys.argv):
		print('No input provided')
		exit
	else:
		with open(sys.argv[1], 'r') as file:
			for line in file:
				empList.append(line.strip())
	
	n = len(empList)
	root = None
	root = insertLevelOrder(empList, root, 0, n)
	inOrder(root)

main()