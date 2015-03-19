class BinarySearch:
	def _init_(self):
		pass

	def binarySearch(self,s, tergat):
		index = -1
		low = 0
		high = len(s)
		while low < high:
			mid = (int)((low + high) / 2)
			if s[mid] > tergat:
				high = mid
			elif s[mid] < tergat:
				low = mid
			else:
				index = mid
				break
		return index

b = BinarySearch()
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b.binarySearch(s, 3))

