import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp


img=mpimg.imread('photo1.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]


U_r,s_r,V_r = sp.svd(r,False,True,False,True)
s_r = np.diag(s_r)

U_g,s_g,V_g = sp.svd(g,False,True,False,True)
s_g = np.diag(s_g)

U_b,s_b,V_b = sp.svd(b,False,True,False,True)
s_b = np.diag(s_b)

print("The no. of non zero elements in sigma of red, green, blue are", len(s_r),"," ,len(s_g),"and" ,len(s_r), "respectively.")


s_red_new = np.zeros_like(s_r)
s_red_new[0:30] = s_r[0:30]
r_new = U_r@s_red_new@V_r

s_green_new = np.zeros_like(s_g)
s_green_new[0:30] = s_g[0:30]
g_new = U_g.dot(s_green_new).dot(V_g)

s_blue_new = np.zeros_like(s_b)
s_blue_new[0:30] = s_b[0:30]
b_new = U_b.dot(s_blue_new).dot(V_b)

img[:,:,0] = r_new
img[:,:,1] = g_new
img[:,:,2] = b_new

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r_new, cmap = 'Reds')
ax3.imshow(g_new, cmap = 'Greens')
ax4.imshow(b_new, cmap = 'Blues')

plt.show()

s_red_new = np.zeros_like(s_r)
s_red_new[0:200] = s_r[0:200]
r_new = U_r@s_red_new@V_r

s_green_new = np.zeros_like(s_g)
s_green_new[0:200] = s_g[0:200]
g_new = U_g.dot(s_green_new).dot(V_g)

s_blue_new = np.zeros_like(s_b)
s_blue_new[0:200] = s_b[0:200]
b_new = U_b.dot(s_blue_new).dot(V_b)


img[:,:,0] = r_new
img[:,:,1] = g_new
img[:,:,2] = b_new

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

