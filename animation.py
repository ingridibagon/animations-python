# Import required packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import os 


plt.rcParams['text.usetex']=True
plt.rcParams['font.size'] = 20
plt.rcParams['font.family'] = 'serif'
plt.rcParams["legend.columnspacing"] = 0.5
plt.rcParams["legend.handlelength"] = 0.8
plt.rcParams["legend.handletextpad"] = 0.5
# plt.rcParams["legend.edgecolor"] = '0.0'
plt.rcParams["legend.frameon"] = False
R1=100
xsize=R1
ysize=R1


def plotframe(i):
    if i<=200:
        it=i*10
    else:
        it=i*100-18000
    print(it)
    ax=fig.gca()
    ax.clear()
   
    
    #plt.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
   


    #import data
    data = np.loadtxt('as-lambda1.68-tp'+str(it)+'.dat')
    #reshape columns 3 and 4 two a square lattice
    sp1=data[:,3].reshape((R1,R1))
    sp2=data[:,4].reshape((R1,R1))
    rede=np.zeros((R1,R1),dtype=int)
    #filters sites with one species only or with spices sp1 and sp2
    filtrosp11=sp1==1
    filtrosp10=sp1==0
    filtrosp21=sp2==1
    filtrosp20=sp2==0
    filtro1=np.logical_and(filtrosp11,filtrosp20)
    filtro2=np.logical_and(filtrosp10,filtrosp21)
    filtro3=np.logical_and(filtrosp11,filtrosp21)
    rede[filtro1]=1
    rede[filtro2]=2
    rede[filtro3]=3
    #defines the colors for each case
    palette = np.array([[  255,   255,   255],   # white -empty sites
                    [255,   140,   0],   # oranage -species1 only
                    [  0,   139, 139],   # blue -species2 only
                    [50, 205, 50]])  # green - species1 and species2


# make a 3d numpy array that has a color channel dimension   
    data_3d = palette[rede]

    ax.imshow(data_3d)
    ax.text(0,100+5,'t='+str(it),color='k',fontsize=20)
    

VELOCITY=200
fig, ax = plt.subplots(1,1,figsize=(xsize/20.,ysize/20.))

ani = animation.FuncAnimation(fig=fig, func=plotframe, 
                              frames=304, interval=VELOCITY)
output='test-verde.mp4'
ani.save(filename=output, writer='ffmpeg' )
