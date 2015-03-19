class InsertSort:
	def _init_():
		pass
	def insertSort(self, s):
		l = len(s)
		for i in range(1, l):
			j = i
			x = s[i]
			while j > 0 and s[j - 1] > x:
				s[j] = s[j - 1]
				j -= 1
			s[j] = x
		print(s)
		return s

i = InsertSort()
s = [3, 8, 2, 0, 5, 7, 4]
i.insertSort(s)


				
		