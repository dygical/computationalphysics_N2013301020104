from pylab import *
import pickle

x = []
t = []
v = 20
dt = 0.1
x.append(0.)
t.append(0)
end_time = 20

for i in range(int(end_time / dt)):
	tmp = x[i] + v * dt
	x.append(tmp)
	t.append(dt * (i + 1))
	print t[-1], x[-1]
	
#plot(t,v,'--')
plot(t,x,'-')
scatter(t,x)
show()
#savefig('output.jpg')