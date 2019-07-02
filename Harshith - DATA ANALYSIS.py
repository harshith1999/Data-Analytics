
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# In[31]:


mtcars1= pd.read_csv("F:\\Study\\mtcars.csv")
print(mtcars1)


# In[3]:


# To calculate mean
n = mtcars1.mean()
print("mean is\n",n)


# In[6]:


#To calculate Geometric mean
gmean=stats.gmean(mtcars1.mpg)
print("geometric mean is",gmean)


# In[7]:


#To calculate Harmonic mean
hmean=stats.hmean(mtcars1.mpg)
print("harmonic mean is",hmean)


# In[9]:


#To calculate median
v=mtcars1.median()
print("median is\n", v)


# In[10]:


#To calculate mode
mod = mtcars1.mode()
print("mode is", mod)


# In[30]:


# To make Pi chart - mpg
mpg_data = mtcars1["mpg"]
model_data = mtcars1["model"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#1f77b4", "#ff7f0e", "#2ca02c"]
explode = (0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)  
plt.pie(mpg_data, labels=model_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=180)
plt.title("Models of the cars " + " mpg of cars")
plt.tight_layout()
plt.show()


# In[12]:


# To Display Data in Histogram
plt.hist(mtcars1.mpg)
plt.show()


# In[13]:


#To Display Box Plot
mtcars1.boxplot(column="mpg", return_type = "axes", figsize = (8,8))
plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="min")
plt.text(x=0.9, y=35, s="max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

