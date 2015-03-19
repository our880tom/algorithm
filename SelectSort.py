class SelectSort:
	def _init_(self):
		pass
	def selectSort(self, s):
		for i in range(len(s)):
			self.findSmallest(s,i);
		return s

	def findSmallest(self, s, index):
		small = index
		for i in range(index + 1,len(s)):
			if s[i] < s[small]:
				small = i
		tmp = s[index]
		s[index] = s[small]
		s[small] = tmp


s = SelectSort()
l = [3, 8, 5, 6, 2, 7]
print(s.selectSort(l))
		