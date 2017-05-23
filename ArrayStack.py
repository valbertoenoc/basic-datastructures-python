class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlying storage."""
	def __init__(self):
		"""Create an empty stack. """
		self.m_data = []
		
	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self.m_data)

	def __str__(self):
		"""Prints all elements of the stack."""
		return ('\n'.join([str(i) for i in self.m_data]) + '\n')

	def isEmpty(self):
		"""Return True if stack is empty."""
		return len(self.m_data) == 0

	def push(self, elem):
		"""Add element elem on top of the stack."""
		self.m_data.append(elem)

	def pop(self):
		"""Remove and return the element from the top of the stack (i.e., LIFO)

		Raise Empty exception if the stack is empty
		"""
		if self.isEmpty():
			raise Empty('Stack is empty')
		return self.m_data.pop()

	def top(self):
		"""Return (but do not remove) the element at the top of the stack.
		Raise Empty exception if the stack is empty.
		"""
		if self.isEmpty():
			raise Empty('Stack is empty')
		return self.m_data[-1]

def main():
	"""Testing if ArrayStack works."""
	stack = ArrayStack()
	
	# Adding elements
	stack.push(50)
	stack.push(100)
	stack.push(150)

	# Printing stack
	print(stack)
	print(stack.top())

	# Popping Stack
	topElem = stack.pop()

	# Printing top element and stack
	print(topElem)
	print(stack)


if __name__ == '__main__':
	main()