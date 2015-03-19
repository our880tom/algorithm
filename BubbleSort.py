class BubbleSort:
	def _init_(self):
		pass
	def bubbleSort(self, s):
		size = len(s)
		for i in range(size - 1):
			for j in range(size - i - 1):
				if s[j] > s[j + 1]:
					temp = s[j]
					s[j] = s[j + 1]
					s[j + 1] = temp
		print(s)
		return s
b = BubbleSort()
s = [8, 6, 3, 7, 2, 8]
b.bubbleSort(s) 