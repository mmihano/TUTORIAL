
# coding: utf-8

# # Advanced Data Visualizaton Tutorial Using Bokeh

# # Table of Contents:
# 
# 1. Defintion of Data Visualization
# 2. Advanced Data Visualization Bokoeh Examples
# 3. Digging Deeper into Bokeh 
# 4. Summary of the Data Visualization
# 5. Helpful/Useful Data Visualization Websites

# # What is Data Visualization?
# 
# Data visualization is the understaning of the data.  It is an valuable technique for data exploration and for reading the data. 
# Data visualization is also considered business intelligence (BI). BI is about visualizing past data  in creative ways using graphs and charts to help make decisions in the near future or in the future.
# 

# Welcome to the advanced data visualization tutorial. Today, we will take a look at several ways to use data visualization that will enhance your understanding. Today we will follow certain steps in the visualizaiton process to eventually work our way up to more advanced topics in visiualization. 

# # Part 1:

# First thing we are going to do is import the python packages. Note that you will not need this many packages but, in this case I want to be sure I dont have to upload several more throughout the project. We will also need to upload a random data set. In this case it will be a CSV package. Follow these steps:
# 
# 1. Run/import the data
# 2. Read the data ______.head()
# 3. Find out the data types
# 4. Drop Unmeaningful Data

# In[3]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'matplotlib inline')

#import decisiontreeclassifier
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
#import logisticregression classifier
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
#import knn classifier
from sklearn.neighbors import KNeighborsClassifier
import sklearn.linear_model as lm


from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage, ward


# STEP 1: Import The data

# In[81]:

df = pd.read_csv("data/bank.csv")


# Step 2: Read the data

# In[5]:

df.head(5)


# Step 3: Find out data types

# In[6]:

df.info()


# Now we are going to drop some unmeanigful data in the data set: in this case if it were me, I would drop the categories radio/tv, telphone and foreign. 

# In[7]:

#drop unmeaningful data

df = df.drop(['TELEPHONE', 'RADIO/TV','FOREIGN'], axis=1)


# In[8]:

#make sure data dropped unmeaningful data first 5 rows

df.head(5)


# In[30]:

df.max()


# In[31]:

df.min()


# Now that we have seen some basic data visualization models, it is time to move onto more advanced data visualization models. Advanced visualization models make the data more easily read and more easier to interpret the data. We are going to use different techniques and websites to help you visualize and read data easier. 
# 
# We are going to use Bokeh as our new technique for visualizing data. We will list several examples but first we have to know why we use Bokeh and what Bokehs definition is.

# # What is Bokeh and why do we use Bokeh?

# Definition and why we use Bokeh: Bokeh is a Python interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of novel graphics in the style of D3.js, and to extend this capability with high-performance interactivity over very large or streaming datasets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, and data applications.
# 

# # Basic Bokeh
# 
# Now let's import the data and take a look at some basic Bokeh examples and then move on to more advanced styles of Bokeh using our data set

# In[9]:

#import the data
from bokeh.io import output_notebook, show
output_notebook()


# In[10]:

#bokeh example 1: HISTOGRAM using AGE AND RESPONSE
from bokeh.charts import Histogram, output_file, show

hist = Histogram(df, values="AGE", color="RESPONSE", legend="top_right", bins=12)
show(hist)


# you can also do a histogram comparing two or more data set points:

# In[82]:

#bokeh example 1: HISTOGRAM using AGE AND RESPONSE AND JOB
from bokeh.charts import Histogram, output_file, show

hist = Histogram(df, values="AGE", color="JOB", legend="top_right", bins=12)
show(hist)


# Histograms are a great way to visualize data sets another great bokeh tool is using heatmaps. This is another basic data visualization technique using Bokeh. We will eventually see some more advanced ways of using Bokeh. Here are two examples of Bokeh heat maps:

# In[11]:

#bokeh example 2: HEATMAP
#3 

from bokeh.charts import HeatMap, show, output_file

hm = HeatMap(df, x="AMOUNT", y="AGE", values='RESPONSE', title='AGE vs AMOUNT vs RESPONSE', stat=None)
show(hm)


# In[12]:

#bokeh example 3: HEATMAP 2


from bokeh.charts import HeatMap, bins, show, output_file

hm1 = HeatMap(df, x='AMOUNT', y='AGE')
show(hm1)


# #  Advanced Bokeh Techniques

# Now lets take a look at some new things, things that are more addvanced techniques we havent  learned too much on. Lets take a look at an examples of some more advanced Bokeh techniques.

# In[13]:

from bokeh.plotting import figure, output_file, show

plot = figure(plot_width=300, plot_height=300)
plot.circle(x=[1, 2, 3], y=[1, 2, 3], size=20)

show(plot)        


# In[14]:

#example 2: radius plotting

from bokeh.plotting import figure, output_file, show

plot = figure(plot_width=300, plot_height=300)
plot.annulus(x=[1, 2, 3], y=[1, 2, 3], color="#7FC97F",
             inner_radius=0.2, outer_radius=0.5)

show(plot)


# Radius plotting is good for the mean, median and mode of the data. It tells us the min, max and the mean of the data which could give us a better idea of the data and where the general vecinitiy of the data and where the data is located. Very helpful when finding statistics and could be a helpful tool. Now let's use some xvalues and yvalues in our 'df' data set. X will be DURATION and Y will be AGE. 
# 
# NOTE: This will be based off of the 5 samples of data we did when importing the data in the beggining. We will use 4 values for this.
# 
# X Values (DURATION) = 6, 48, 12, 24
# 
# Y Values (AGE) = 67, 22, 49, 45

# In[15]:

#example 1B : radius plotting

from bokeh.plotting import figure, output_file, show

plot = figure(plot_width=300, plot_height=300)
plot.annulus(x=[6, 48, 12, 24], y=[67, 22, 49,45], color="#7FC97F",
             inner_radius=0.5, outer_radius=0.75)

show(plot)


# When using radius and circle plotting, you compare SPECIFIC data from the model. You may find some kind of relationship but it does not compare all of the data. It is useful when comparing 2-8 data sets. It is not useful when comparing all of the data but if you are trying to find some relationship between the first couple of data sets it can be very useful. We can see, in this case  that the younger the age, the higher the response time. That is not comapring ALL of the data. 

# Bookeh Example 3: Linked panning
# 

# Linked panning is when multiple plots have ranges that stay in order, it is a  useful with Bokeh. You simply share the appropriate range objects between two (or more) plots. The example below shows how to accomplish this by linking the ranges of certain data together. Here is a random example of Linked Panning

# In[24]:

from bokeh.models import ColumnDataSource

from bokeh.layouts import gridplot

x = list(range(-20, 21))
y0, y1 = [abs(xx) for xx in x], [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "box_select,lasso_select,help"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300)
left.circle('x', 'y0', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, width=300, height=300)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

show(p)

















# Now let's look at a different panning example with a different range!

# In[25]:

x = list(range(-50, 100))
y0, y1 = [abs(xx) for xx in x], [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "box_select,lasso_select,help"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300)
left.circle('x', 'y0', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, width=300, height=300)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

show(p)


# This is a cool way to find different data points using ranges. It is perfect when you have certain ranges in your data and when you are trying to compare those ranges.

# # Digging Deeper in Bookeh

# Date times organize the data very well and youll be able to see results through a date times

# In[49]:

#example 1: DateTimes


import pandas as pd
from bokeh.plotting import figure, output_file, show



output_file("datetime.html")

p = figure(width=500, height=250, x_axis_type="datetime")

p.line(df['AGE'], df['RESPONSE'], color='navy', alpha=0.5)
p.line(df['AGE'], df['AMOUNT'], color='red', alpha=0.5)

show (p)
















# In this case data is all over the place let's try the same datetime just minus one variable. Let's try just AGE and RESPONSE variables.  
# 

# In[51]:

import pandas as pd
from bokeh.plotting import figure, output_file, show



output_file("datetime.html")

p = figure(width=500, height=250, x_axis_type="datetime")

p.line(df['AGE'], df['RESPONSE'], color='navy', alpha=0.5)

show (p)


# You can see the highest response rates are in the ages of 30 to 40 years of age there is alot of activity in there. Now let's see the other variable we used which was amount for the data set. 

# In[53]:

#creating DataTimes example 2



output_file("datetime.html")

p = figure(width=500, height=250, x_axis_type="datetime")

p.line(df['AGE'], df['AMOUNT'], color='navy', alpha=0.5)

show(p)


# In[56]:

#creating data Times Example 3

output_file("datetime.html")

p = figure(width=500, height=250, x_axis_type="datetime")

p.line(df['JOB'], df['RESPONSE'], color='navy', alpha=0.8)

show(p)


# Lets try one more example

# In[58]:

#creating data times Example 4





output_file("datetime.html")

p = figure(width=500, height=250, x_axis_type="datetime")

p.line(df['AGE'], df['JOB'], color='navy', alpha=0.5)

show(p)


# # Analyzing the Data and Interpretion of Data Times

# You can see that the most of the  activity happens when amounts are in 30-40 years of the amounts between 0 to 5000.00. Since we have seen Data Times, an advanced way to do data visualization. Data Times can let you visualize specific categories in your data set aand where activity falls in.  Let's take a look at another data set comparing Apples and Fruits using a Bar Chart exmple. 

# In[54]:

#example 2: Creating a bar graph.

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure

output_file("bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (fruit, year) for fruit in fruits for year in years ]
counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250, title="Fruit Counts by Year",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)


# # Interpretation of Adv Bar Charts

# As you can see you can count objects by using a bar chart this is an advnced way to organize data and is easier to red CERTAIN data points. We can see a bar chart, will help you view certain data points rather than the whole thing. We saw that basic circle plots werre also used to compare certain data points but now bar charts especially this one is a deeper understanding of comparisons within specific data points. You can also customize titles and x and y valued comparisons how you want them to be. 

# As we finish up this tutorial, we have learned many different techniques to help improve dataa visualization and what different ways to improve your understanding of the data by visualizating it through Bokeh. Let's take look at one more technique and interpret what it means and what the technique is used for. We will be uploading a sample data set through Bokeh for this next example. The next example is something not related to the current data set but it is posted online on Bokeh. But we are using the fruit data set that is used throughout the Bokeh website.

# In[75]:

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure

output_file("stacked_split.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]

exports = {'fruits' : fruits,
           '2015'   : [2, 1, 4, 3, 2, 4],
           '2016'   : [5, 3, 4, 2, 4, 6],
           '2017'   : [3, 2, 4, 4, 5, 3]}
imports = {'fruits' : fruits,
           '2015'   : [-1, 0, -1, -3, -2, -1],
           '2016'   : [-2, -1, -3, -1, -2, -2],
           '2017'   : [-1, -2, -1, 0, -2, -2]}

p = figure(y_range=fruits, plot_height=250, x_range=(-16, 16), title="Fruit import/export, by year",
           toolbar_location=None)

p.hbar_stack(years, y='fruits', height=0.9, color=GnBu3, source=ColumnDataSource(exports),
             legend=["%s exports" % x for x in years])

p.hbar_stack(years, y='fruits', height=0.9, color=OrRd3, source=ColumnDataSource(imports),
             legend=["%s imports" % x for x in years])

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None

show(p)






 
 
 
 




 
 
 










# # Other Techniques- Mapping 

# In[79]:

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.tile_providers import STAMEN_TONER

bound = 20000000 # meters
fig = figure(tools='pan, wheel_zoom', x_range=(-bound, bound), y_range=(-bound, bound))
fig.axis.visible = False
fig.add_tile(STAMEN_TONER)
output_file("stamen_toner_plot.html")
show(fig)


# Mapping is used to plot mapping data. This is also a random data point but this is  great way to find GPS locations we can find different locations by using maps. Maps is a good way when you have longitutes and Latitudes. This is a useful tool when you have data longitudes and latitudes. 

# # 

# # Conclusion of the  Tutorial

# The conclusion of this tutorial is to find different ways to use Bokeh we learned different basic techniques, advanced techniques and digging deeper into the techniques. There are several more technqiues you can use within data visualization. I feel like Bokeh is one of the easiest techniques to do. In conclusion, we looked at several techniques and Bokeh techniques can really improve your interpretion of data and how to read it. Bokeh makes it easier to do comparisons of data as well as specifics of ALL the data. Bokeh is used to easily prepare and real data. Data is easily read and applied to in the Bokeh techniques shown. I hope you have learned many different styles of using bokeh in this tutorial.
# 
# You have to answer these questions when using Bokeh:
# 
# What do you want to visualize?
# 
# What kinds of data types do you have?
# 
# What are you trying to accomplish?
# 
# These data type questions will allow you to prepare what you are trying to do and what Bokeh Visualizations you can do. I showed you several different types now there are many different types listed below. 
# 
# 

# # Useful Bokeh Technique Websites:

# http://bokeh.pydata.org/en/0.10.0/docs/tutorials.html
# 
# https://github.com/
# 
# https://stackoverflow.com/questions/22345249/embedding-a-plot-in-a-website-with-python-bokeh
# 
