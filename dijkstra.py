"""Dijkstra's algorithm """
__author__="Aakash"
class Dj:
	def __init__(self,dat=None):
		self.data={}
		self.v=[]
		self._e=[]
		self.get_data(dat)
#	@property
#	def infi(self):
#		return 999
	def get_data(self,val=None):
		print("provide the data regarding the graph like the following:\n[(vertex_1,vertex_2,weight of the edge)] example:\n('a','b',4) which represents an edge connecting two vertices a,b(as strings) with weight 4")
		l=eval(input())
		for i in l:
			for j in range(2):
				if not i[j] in self.v:self.v.append(i[j])
		self.res={(i[0],i[1]):i[2] for i in l}
	def algo(self):
		s_v=input("source vertex:")
		d_v=input("destination vertex:")
		S=[s_v]
		label={}
		label[(s_v,s_v)]=[[],0]
		while(d_v not in S):
			lab={}
			final=[]
			for j in S:
				R=[m for m in self.res if j in m]
				cr=[set(p) for p in R]
				for _ in cr:_.remove(j)
				re=[(j,x) for y in cr for x in y if not x in S]
				for i in re:
					if not i:break
					else:final.append(i)
			for i in final:
				if (s_v,i[-1]) in lab:
					res=label[(s_v,i[0])][1]+self.res[(i[0],i[1])]
					if res<lab[(s_v,i[-1])][1]:
						lab[(s_v,i[-1])]=[label[(s_v,i[0])][0]+[i[-1]],label[(s_v,i[0])][1]+self.res[(i[0],i[1])]]
				else:lab[(s_v,i[-1])]=[label[(s_v,i[0])][0]+[i[-1]],label[(s_v,i[0])][1]+self.res[(i[0],i[1])]]
			d=min(lab,key=lambda x:lab[x][1])
			label[(s_v,d[1])]=lab[(s_v,d[1])]
			S.append(d[1])
		path=[s_v]+label[(s_v,d_v)][0]
		dist=label[(s_v,d_v)][1]
		return "Path:%s,Distance:%d"%(path,dist)

		
		
			
		
		  
		
		
		
		
