import math
import matplotlib.pyplot as plot
import random
import numpy as np
def sigmoid(z):
	return 1/(1+math.exp(-z))
def hypo(a,b,x):
	return sigmoid(a*x+b)
plot.title('Loss function with iterations')
plot.xlabel('iterations')
plot.ylabel('loss')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.ylim(0, 10)
n=700
x=[i for i in range(1,n+1)]
y=[1 for i in range(1,351)]
y+=[0 for i in range(351,n+1)]
print(sum(y))
alphax=0.01
alphay=0.099
iterations=3500
sel=4
xaxis=np.linspace(0,iterations,iterations, endpoint=True)
a=0.5
b=0.5
yaxis=[]
for i in range(iterations):
	temp=int(random.random()*n)
	da=alphax*((hypo(a,b,x[temp])-y[temp])*x[temp])/n
	db=alphay*(hypo(a,b,x[temp])-y[temp])/n
	a-=da
	b-=db
	loss=0
	for j in range(n):
		if hypo(a,b,x[j])==1 or hypo(a,b,x[j])==0:
			loss+=1/n
		else:
			loss-=(y[j]*math.log(hypo(a,b,x[j]))+(1-y[j])*math.log(1-hypo(a,b,x[j])))/(n)
	yaxis.append(loss)
for i in range(250,500):
	print(i,hypo(a,b,i))
plot.plot(xaxis,yaxis,label="loss")
plot.legend()
plot.show()