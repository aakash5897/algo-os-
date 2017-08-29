class TSP:
	def __init__(self,dat=None):
		self.data={}
		self.v=[]
		self._e=[]
		try:
			self.get_data(dat)
		except:raise TypeError("Did not provide proper detailes")
	@property
	def infi(self):
		return 999
	def get_data(self,val=None):
		print("provide the data regarding the graph like the following:\n[(vertex_1,vertex_2,weight of the edge)] example:\n('a','b',4) which represents an edge connecting two vertices a,b(as strings) with weight 4")	
		l=eval(input())
		for i in l:
			for j in range(2):
				if not i[j] in self.v:self.v.append(i[j])
		self.res={(i[0],i[1]):i[2] for i in l}
		print(self.res)
	def func(self):
		self.am=[[] for i in range(len(self.v))]
		temp=list(self.v)
		for i in self.am:
			for j in range(len(temp)):
				if (temp[self.am.index(i)],temp[j]) in self.res:
					i.append(self.res[(temp[self.am.index(i)],temp[j])])
				elif (temp[j],temp[self.am.index(i)]) in self.res:
					i.append(self.res[(temp[j],temp[self.am.index(i)])])					
				else:i.append(0)
		return self.am
	def algo(self):
			
			
				
			
