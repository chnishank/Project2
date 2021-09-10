import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set() 

olympic=pd.read_csv("athlete_events.csv")
# print(olympic.head())

#----------sex ratio-----------------
# sex_values=list(olympic["Sex"].value_counts())
# sex_keys=list(olympic["Sex"].value_counts().keys())
# print(sex_keys)
# print(sex_values)
# explode=[0,0.1]
# plt.figure(figsize=(12,7))
# plt.pie(sex_values,labels=sex_keys,startangle=87,autopct="%.1f%%",explode=explode,shadow=True)
# print(plt.show())

#----------medals ratio------------------
# medal_values=list(olympic["Medal"].value_counts())
# medal_keys=list(olympic["Medal"].value_counts().keys())
# print(medal_keys)
# print(medal_values)
# explode=[0,0.1,0.1]
# plt.figure(figsize=(12,7))
# plt.pie(medal_values,labels=medal_keys,startangle=87,autopct="%.1f%%",explode=explode,shadow=True)
# print(plt.show())
#------------------------------------
# sns.set_style("whitegrid")
# sns.set_palette("Set2")
# sns.countplot("Sex",data=olympic)
# print(plt.show())

#--------medals distribution-----------------
# print(olympic["Medal"].value_counts())
# medal_keys=list(olympic["Medal"].value_counts().keys())
# medal_values=list(olympic["Medal"].value_counts())
# #print(medal_keys,medal_values)
# explode=[0,0.1,0.1]
# plt.figure(figsize=(12,7))
# plt.pie(medal_values,labels=medal_keys,startangle=87,autopct="%.1f%%",explode=explode,shadow=True)
# print(plt.show())

#--------------medals with respect to male and female-----------------
# sns.set_style("whitegrid")
# sns.set_palette("Set2")
# sns.countplot(x="Sex",hue="Medal",data=olympic)
# print(plt.show())
#------------------top 7 sports-----------------------------
sns.set_style("whitegrid")
sns.set_palette("Set2")
sns.countplot("Sport",data=olympic,order=olympic["Sport"].value_counts().index[:7])
print(plt.show())
#----------------------sports wrt sex---------------------------
# sns.set_style("whitegrid")
# sns.set_palette("Set2")
# sns.countplot("Sport",hue="Sex",data=olympic,order=olympic["Sport"].value_counts().index[:7])
# print(plt.show())
#---------------------medal distribution among top games-------------------
# sns.set_style("whitegrid")
# sns.set_palette("Set2")
# sns.countplot("Sport",hue="Medal",data=olympic,order=olympic["Sport"].value_counts().index[:7])
# print(plt.show())

# plt.figure(figsize=(12,30))
# sns.set_style("whitegrid")
# sns.set_palette("Set2")
# sns.countplot("Name",data=olympic,order=olympic["Name"].value_counts().index[:7])
# print(plt.show())

