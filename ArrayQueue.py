class ArrayQueue:
	"""FIFO queue implementation using a Python list as underlying storage."""
	def __init__(self):
		"""Create an empty queue."""
		self.m_data = [None]*ArrayQueue.DEFAULT_CAPACITY
		self.m_size = 0
		self.m_front = 0

	def __len__(self):
		"""Return the number of elements in the queue"""
		return self.m_size

	def isEmpty(self):
		"""Return True if the queue is empty."""
		return self.m_size == 0

	def first(self):
		"""Return (but do not remove) the element at the front of the queue.

		Raise Empty exception if the queue is empty
		"""
		if self.isEmpty():
			raise Empty('Queue is empty.')
		return self.m_data[self.m_front]

	def dequeue(self):
		"""Remove and return the first element of the queue (i.e., FIFO).

		Raise Empty exception if the queue is empty.

		"""
		if self.isEmpty():
			raise Empty('Queue is empty')
			answer = self.m_data[self.m_front]
			self.m_data[self.m_front] = None
			self.m_front = (self.m_front + 1) % len(self.m_data)
			self.m_size -= 1
			return answer

	def enqueue(self, elem):
		"""Add an element to the back of the queue."""
		if self.m_size == len(self.m_data):
			self.resize(2*len(self.m_data)) #double the array size
		avail = (self.m_front + self.m_size) % len(self.m_data)
		self.m_data[avail] = elem
		self.m_size += 1

	def m_resize(self, cap):
		"""Resize to a new list of capacity >= len(self)."""
		old = self.m_data
		self.m_data = [None]*cap
		walk = self.m_front
		for k in range(self.m_size):
			self.m_data[k] = old[walk]
			walk = (1 + walk) % len(old)
			self.m_front = 0

def main():
	pass

if __name__ == '__main__':
	main()

		