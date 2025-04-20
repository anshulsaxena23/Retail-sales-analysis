import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#files_name = os.listdir('SalesData')
#print(files_name)
#edf=pd.DataFrame()
#for files in files_name:
    #print(files)
    #df=pd.read_csv(f'SalesData/{files}')
    #print(df)
    #edf=pd.concat([edf,df])
#print(edf)
#edf.to_csv('Sales.csv',index=False)
# df=pd.read_csv('Sales.csv')
# df=df.dropna(how='all')
# df=df.loc[df['Quantity Ordered']!='Quantity Ordered']
#print(df.info())
# df['Price Each']=df['Price Each'].astype(float)
# df['Quantity Ordered']=df['Quantity Ordered'].astype(int)
# df['Order Date']=pd.to_datetime(df['Order Date'])
#print(df.info())
#print(df)
#print(df.isnull().sum())
#df.to_csv('SALE.CSV',index=True)
# df=pd.read_csv('SALE.CSV')
# df['Amount']=df['Quantity Ordered']*df['Price Each']
# df['City']=df['Purchase Address'].str.split(',',expand=True)[1]
# df['Order Date']=pd.to_datetime(df['Order Date'])
# df['month']=df['Order Date'].dt.month
# df['month name']=df['Order Date'].dt.month_name()
# df['day name']=df['Order Date'].dt.day_name()
# df.to_csv('Sal.csv')
# Monthly sale revenue
# df=pd.read_csv('Sal.csv')
#ndf=df.groupby(['month','month name']).agg(
    #total= ('Amount','sum'),
    #avg= ('Amount','mean')
#)
#ndf=ndf.reset_index()
#ndf.to_csv('Analysis/MonthlySales.csv',index=False)
#df=pd.read_csv('Analysis/MonthlySales.csv')
#plt.figure(figsize=(15,10))
#plt.plot(df['month name'],df['total'],marker='o',label='sale')
#plt.title('Monthly sales')
#plt.xlabel('month')
#plt.ylabel('sale')
#for x,y in zip(df['month name'],df['total']):
    #plt.text(x,y,y)
#plt.grid()
#plt.legend()
#plt.savefig('Analysis/MonthlySales.png')
#s=df['day name'].value_counts()
#plt.figure(figsize=(15,10))
#plt.bar(s.index,s.values,color='Green')
#plt.title('Number of Orders')
#plt.grid(axis="x", linestyle="--", alpha=0.7)
#plt.xlabel('Days')
#plt.ylabel('Orders')
#for x,y in zip(s.index,s.values):
    #plt.text(x,y,y,color = 'Red')
#s.to_csv('Analysis/Ordersbyday.csv')
#plt.savefig('Analysis/Ordersbyday.png')
#----------------------- holiday
#df['IsHoliday']='False'
#df.loc[df['day name'].isin(['Saturday','Sunday']),'IsHoliday']=True
#ndf=df.groupby('IsHoliday').agg(
    #Avgsales=('Amount','mean')
#)
#print(ndf)
#Which City as most number of orders:
#ndf=df.groupby('City').agg(
    #orders=('City','count'),
    #Quantity=('City','count'),
    #revenue= ('Amount','sum')
#)
#ndf=ndf.reset_index()
#ndf.to_csv('Analysis/City.csv',index=False)
#df=pd.read_csv('Analysis/City.csv')
#x_pos= np.arange(0,9)
#plt.figure(figsize=(15,10))
#plt.bar(x_pos,df['orders'],label='order',color='green')
#plt.bar(x_pos+0.2,df['Quantity'],label='Quantity',color='blue',width=0.4)
#plt.title('City Analysis')
#plt.xlabel('City')
#plt.ylabel('Orders')
#plt.grid()
#plt.legend()
#plt.xticks(x_pos,df['City'])
#plt.savefig('Analysis/City.png')
#ndf=df.loc[df['Order ID'].duplicated(keep=False)].copy()
#ndf['Product']= ' , ' + ndf['Product']
#ndf=ndf.groupby('Order ID').agg(group =('Product','sum'))
#ndf['group']=ndf['group'].str.strip(',')
#ndf=ndf.reset_index()
#ndf.to_csv('Analysis/duplicate.csv',index=False)
from itertools import combinations
from collections import Counter

df=pd.read_csv('duplicate.csv')
df['group']=df['group'].str.split(',')
l=list(df['group'])
count = Counter()
for sublist in  l :
    count.update(Counter(combinations(sublist,2)))
print(count)