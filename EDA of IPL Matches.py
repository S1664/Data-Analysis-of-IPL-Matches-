#!/usr/bin/env python
# coding: utf-8

# # <center> Exploratory Data Analysis of IPL Matches</center>

# #### Loading required libraries

# In[117]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# #### Loading IPL matches dataset

# In[118]:


ipl=pd.read_csv(r"C:\Users\Priya K\Desktop\IPL_PROJECT\matches.csv")


# #### Having a glance at first five records of the dataset

# In[119]:


ipl.head()


# #### Looking at the number of rows and columns in the dataset

# In[120]:


ipl.shape


# #### Getting the frequency of most man of the match awards

# In[121]:


ipl['player_of_match'].value_counts()


# #### Getting the top 10 players with most man of the match awards

# In[122]:


ipl['player_of_match'].value_counts()[0:10]


# #### Making a bar plot for the top 5 players with most man of the match awards.

# In[123]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# #### Getting the frequency of result column 

# In[124]:


ipl['result'].value_counts()


# #### Finding out the number of toss win with respect to each team

# In[125]:


ipl['toss_winner'].value_counts()


# #### Extracting the records where a team won batting first

# In[126]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[127]:


batting_first.head()


# #### Making a histogram

# In[128]:


plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'],color="blue")
plt.title("Distribution of runs")
plt.xlabel('Runs')
plt.show()


# #### Finding out the number of wins w.r.t each team after batting first

# In[129]:


batting_first['winner'].value_counts()


# #### Making a bar plot for top 3 teams with most wins after the batting first

# In[130]:



plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.xlabel("Teams")


# #### Making a pie chart

# In[131]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()))
plt.legend()
plt.show()


# #### Extracting those recored where a team has won after batting second

# In[132]:


batting_second=ipl[ipl['win_by_wickets']!=0]
batting_second


# #### Making a histogram for frequency of wins w.r.t number of wickets

# In[133]:


plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)

plt.show()


# #### Finding out the freq of no of wins w r t each time after batting second

# In[134]:


batting_second['winner'].value_counts()


# #### Making a bar plot for top 3 teams with most wins after batting second

# In[135]:


plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=['purple','maroon','yellow'])
plt.show()


# #### Making a pie chart for distribution of most wins after batting second

# In[153]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()))
plt.legend()
plt.show()


# #### Looking at the number of matches played in each season

# In[137]:


ipl['season'].value_counts()


# #### Looking at the no of matches played in each city

# In[138]:


ipl['city'].value_counts()


# #### Finding out how many times a team has won the match after winning the toss

# In[139]:


import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[140]:


393/756


# In[141]:


deliveries=pd.read_csv(r'C:\Users\Priya K\Desktop\IPL_PROJECT\deliveries.csv')


# In[142]:


deliveries.head()


# In[143]:


deliveries['match_id'].unique()


# In[144]:


match_1=deliveries[deliveries['match_id']==1]


# In[145]:


match_1.head()


# In[146]:


match_1.shape


# In[147]:


srh=match_1[match_1['inning']==1]


# In[148]:


srh['batsman_runs'].value_counts()


# In[149]:


srh['dismissal_kind'].value_counts()


# In[150]:


rcb=match_1[match_1['inning']==2]


# In[151]:


rcb['dismissal_kind'].value_counts()

