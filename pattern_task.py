import numpy as np 
##Given the list 𝑑𝑎𝑡𝑎 = [15,18,13,20,20,11,14,99,100,200,201, 0], use 
##NumPy to calculate the mean, median, variance, and standard deviation.

## mean 
list = [15,18,13,20,20,11,14,99,100,200,201,0]
print(np.mean(list,axis=0))

#%%
## median
print (np.median(list,axis=(0)))

#%%
## variance 
print(np.var(list,axis=0))

#%%
## Standard deviation
print(np.std(list,axis=0))

#%%
## Using NumPy and matplotlib, plot a figure of a Gaussian distribution of 
## 𝑚𝑒𝑎𝑛 = 6.0, 𝑠𝑡𝑎𝑛𝑑𝑎𝑟𝑑 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 = 1.0, with 𝑠𝑖𝑧𝑒 = 100000 
import matplotlib.pyplot as plt


# Creating a series of data of in range of 1-23.
x = np.linspace(1,23,100000)
def normal_density (x,mean,sd):
    prob_density = (np.pi*sd)*np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
pdf = normal_density(x, 6, 1)
plt.plot(x,pdf)
    
