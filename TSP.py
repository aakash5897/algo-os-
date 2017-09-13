class TSP:
	def __init__(self,dat=None):
		self.data={}
		self.v=[]
		self.p=[]
		self._c=0
		try:
			self.get_data(dat)
		except:raise TypeError("Did not provide proper detailes")
	def get_data(self,val=None):
		print("provide the data regarding the graph like the following:\n[(vertex_1,vertex_2,weight of the edge)] example:\n('a','b',4) which represents an edge connecting two vertices a,b(as strings) with weight 4")	
		l=eval(input())
		for i in l:
			for j in range(2):
				if not i[j] in self.v:self.v.append(i[j])
		self.res={(i[0],i[1]):i[2] for i in l}
	def mak_sub(self,sub,l):
		R=list(sub)
		for i in range(len(R)):
			temp=R[i:i+l]
			if temp[0]==R[-1] and l!=1:temp=[R[i],R[0]]
			self.p.append(set(temp))
		r=lambda x:[i for i in x if len(i)==l]
		return r(self.p)
	def dist(self,li):
		try:return self.res[(li[0],li[1])]
		except KeyError:return self.res[(li[1],li[0])]
	def g(self,el,S):
		if S==set():return self.dist([el,"1"])
		else:
			for j in S:
				temp=S-{j}
				if len(temp)==0:return self.dist([el,j])+self.dist([j,"1"])
				else:return self.dist([el,j])+self.g(j,temp)
	def algo(self):
		assert self._c==0,("This function can be called only once")
		self._c+=1
		dist_dict={}
		check_list=[]
		rs=[]
		S=set(self.v)-{"1"}
		for _ in range(len(S)):
			subs=self.mak_sub(S,_+1)
			check_list.append(subs)
		check_list=[i for _ in check_list for i in _]
		for _ in check_list:
			rt=[]
			for i in _:
				rt.append(self.g(i,_-{i}))
			rs.append([rt])	
		return rs						
	
				
				
				
				
				
		
			
			
		
		
			
			
			
				
			
