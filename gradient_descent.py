import matplotlib.pyplot as plot
import random
import numpy as np
plot.title('Loss function with iterations')
plot.xlabel('iterations')
plot.ylabel('loss')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.ylim(0, 10)
n=50
x=[i for i in range(n)]
y=[79*i+91 for i in range(n)]
alphax=0.004
alphay=0.92
iterations=3000
sel=4
xaxis=np.linspace(0,iterations,iterations, endpoint=True)
a=40
b=40
yaxis=[]
for i in range(iterations):
	temp=int(random.random()*n)
	da=alphax*((a*x[temp]+b-y[temp])*x[temp])/n
	db=alphay*(a*x[temp]+b-y[temp])/n
	a-=da
	b-=db
	loss=0
	#print(a,b)
	for j in range(n):
		loss+=(a*x[j]+b-y[j])**2/(2*n)
	yaxis.append(loss)
print(a,b,loss)
plot.plot(xaxis,yaxis,label="loss")
plot.legend()
plot.show()
#wait.key()