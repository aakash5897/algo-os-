"""implementing FIRST COME FIRST SERVE scheduling algorithm """
class FCFS:
	def read(self):	
		n=int(input("enter number of processes:"))
		self.n=n
		self.d={"ar":[],"bt":[]}
		for i in range(self.n):
			r=input("enter arrival time and burst time of the process %d:"%(i+1))
			try:
				a,b=map(int,r.split())
				self.d["ar"].append((i,a))
				self.d["bt"].append((i,b))
			except:print("spaces between the two inputs!!!!!".upper())
			break
		self.rq=sorted(self.d["ar"],key=lambda x:x[1])
	def calc(self):
		self.d["ft"]=[]
		s=0
		for i in self.rq:
				p=i[0]
				s+=[r for g,r in self.d["bt"] if g==p][0]
				self.d["ft"].append((i[0],s))
		self.tat=[]
		self.wt=[]
		for i in range(self.n):
			self.tat.append([m-n for z,m in self.d["ft"] if z==i for x,n in self.d["ar"] if x==i][0])
		for i in range(self.n):
			self.wt.append([self.tat[i]-m for x,m in self.d["bt"] if x==i][0])
	@property
	def avg_wt_tat(self):
		print("Average waiting time:%f \n Average turnaroundtime:%f"%((sum(self.wt))/len(self.wt),(sum(self.tat))/len(self.tat)))	
				
			
			

					

			
		
