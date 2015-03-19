class QuickSort:
	def _init_(self):
		pass
	def ajustArr(self, s, l, r):
		i = l
		j = r
		x = s[l]
		while i < j:			
			while i < j and s[j] > x:
				j -= 1
			if i < j:
				s[i] = s[j]
				i += 1
			while i < j and s[i] < x:
				i += 1
			if i < j:
				s[j] = s[i]
				j -= 1
		s[i] = x
		return i			

	def quicksort(self, s, l, r):
		if l < r:
			i = self.ajustArr(s, l, r)
			self.quicksort(s, l, i - 1)
			self.quicksort(s, i + 1, r)

q = QuickSort()
s = [8,5,3,7,6,2]
q.quicksort(s, 0, len(s) - 1)
print(s)

		
		