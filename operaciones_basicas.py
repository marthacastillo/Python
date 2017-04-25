class Number:
	
	def _sum(self,n1,n2):
		return	n1+n2
	def _mult(self, n1,n2):
		return n1*n2
	def _div(self,n1,n2):
		return n1/n2
	def _res(self,n1,n2):
		return n1-n2
	def _opc(self,opc):
		op = Number()
		if opc == '+':
			print(op._sum(1,1))
		elif opc == '-':
			print(op._mult(2,3))
		elif opc == '*':
			print(op._div(3,1))
		elif opc == '/':
			print(op._res(4,1))
		else:
			print("No es posible hacer esa operacion")

 
opt = Number()
opt._opc('+')





#op = Number(1,2)
#print(op._sum(1,1))
#print(op._mult(2,3))
#print(op._div(3,1))
#print(op._res(4,1))
		

		
		