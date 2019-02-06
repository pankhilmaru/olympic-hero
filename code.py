# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'},inplace=True)
data.head(10)

#Code starts here



# --------------
#Code starts here
data['Better_Event']=np.where((data['Total_Summer'])>(data['Total_Winter']),'Summer','Winter')

index_both = data.query('Total_Summer == Total_Winter').index

data.loc[index_both,'Better_Event']='Both'

better_event = data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here
top_countries = data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(146,inplace=True)

def top_ten(df,col_name):
    country_list=[]
    temp =df.nlargest(10,col_name)
    country_list= temp['Country_Name']
    return country_list

top_10_summer=list(top_ten(df=top_countries,col_name='Total_Summer'))
top_10_winter=list(top_ten(df=top_countries,col_name='Total_Winter'))
top_10=list(top_ten(df=top_countries,col_name='Total_Medals'))

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer')
winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter')
top_df.plot(kind='bar',x='Country_Name',y='Total_Medals')



# --------------
#Code starts here
summer_df['Golden Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden Ratio'].max()
index_summer_country = summer_df['Golden Ratio'].idxmax()
summer_country_gold = summer_df.loc[index_summer_country,'Country_Name']


winter_df['Golden Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden Ratio'].max()
index_winter_country = winter_df['Golden Ratio'].idxmax()
winter_country_gold = winter_df.loc[index_winter_country,'Country_Name']

top_df['Golden Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden Ratio'].max()
index_top_country = top_df['Golden Ratio'].idxmax()
top_country_gold = top_df.loc[index_top_country,'Country_Name']


# --------------
#Code starts here
data_1 = data.drop(146)

data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']*1

most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best=data[data['Country_Name']=='United States']
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


