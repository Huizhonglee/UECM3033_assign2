import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp


img=mpimg.imread('photo1.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]


U_red,s_red,Vh_red = sp.svd(r,False,True,False,True)
s_red = np.diag(s_red)

U_green,s_green,Vh_green = sp.svd(g,False,True,False,True)
s_green = np.diag(s_green)

U_blue,s_blue,Vh_blue = sp.svd(b,False,True,False,True)
s_blue = np.diag(s_blue)

print("The no. of non zero elements in sigma of red, green, blue are", len(s_red),"," ,len(s_green),"and" ,len(s_blue), "respectively.")


s_red_new = np.zeros_like(s_red)
s_red_new[0:30] = s_red[0:30]
r_new = U_red@s_red_new@Vh_red

s_green_new = np.zeros_like(s_green)
s_green_new[0:30] = s_green[0:30]
g_new = U_green.dot(s_green_new).dot(Vh_green)

s_blue_new = np.zeros_like(s_blue)
s_blue_new[0:30] = s_blue[0:30]
b_new = U_blue.dot(s_blue_new).dot(Vh_blue)

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

s_red_new = np.zeros_like(s_red)
s_red_new[0:200] = s_red[0:200]
rnew = U_red@s_red_new@Vh_red

s_green_new = np.zeros_like(s_green)
s_green_new[0:200] = s_green[0:200]
g_new = U_green.dot(s_green_new).dot(Vh_green)

s_blue_new = np.zeros_like(s_blue)
s_blue_new[0:200] = s_blue[0:200]
b_new = U_blue.dot(s_blue_new).dot(Vh_blue)


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

