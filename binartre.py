#!/usr/bin/python

class binarytree(object):
	class node(object):
		def __init__(self,data,left=None,right=None):
			self.left=left
			self.right=right
			self.data=data

	def __init__(self):
		self.root=None

	def traverse_inorder(self,root=None):
		node=root or self.root
		stack=[]
		while True:
			if node.left:
				stack.append(node)
				node=node.left
				continue
			yield node.data
			if not stack:
				break
			node=stack.pop()
			yield node.data
			if node.right:
				node=node.right
				continue

	def traverse_preorder(self,root=None):
		pass

	def traverse_postorder(self,root=None):
		pass
