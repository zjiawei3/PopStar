from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from collections import OrderedDict

xaxis1 = OrderedDict()
xaxis2_temp = OrderedDict()
xaxis2 = OrderedDict()
yaxis = OrderedDict()

# key = domain, value[0] = social rank, value[1] = search rank position
with open('social_rank_search.txt','r') as sr:
	for dn in sr:
		xaxis1[dn.split(' ')[0]] = [dn.split(' ')[1],dn.split(' ')[2]]


with open('Blacklist_Check_Score.txt','r') as bl:
	for dn in bl:
		yaxis[dn.split(' ')[0]] = dn.split(' ')[1]


xf1 = OrderedDict()
xf2 = OrderedDict()
yf = OrderedDict()
# change string to floats
for k,v in xaxis1.items():
	v[1] = v[1].strip()
	xf1[k] = [float(v[0]), (float(v[1])/10)] # v[1]/10 to get search position scale down in 100, cause we have searched 1000 websites

for each in yaxis.items():
	yf[each[0]] = float(each[1])

yf1 = OrderedDict()
yf2 = OrderedDict()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



# map y to x
for i in xf1.items():
	for j in yf.items():
		if i[0] == j[0]:
			yf1[i[0]] = j[1]
		else:
			continue
for i in xf2.items():
	for j in yf.items():
		if i[0] == j[0]:
			yf2[i[0]] = j[1]
		else:
			continue

x1 = range(len(xf1))
x2 = range(len(xf2))
x3 = []
for i in xrange(len(xf1)):
	x3.append(0)
y3 = []
for i in xrange(len(xf1)):
	y3.append(0)


_x = OrderedDict()
_y = OrderedDict()
for i in xf1.items():
	_x[i[0]] = i[1][0]
	_y[i[0]] = i[1][1]

# 3d bar plot
xpos = []
ypos = []
for i in _x.values():
	xpos.append(i)
for j in _y.values():
	ypos.append(j)

zpos = np.zeros(len(yf1))

dx = np.ones(len(xf1))
dy = np.ones(len(xf1))
dz = yf1.values()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
ax.set_xlabel('Social Score')
ax.set_ylabel('Bing Serach Rank')
ax.set_zlabel('Danger Score')
plt.show()
