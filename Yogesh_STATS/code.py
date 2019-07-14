# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 

data=pd.read_csv(path)

data['Gender'].replace('-','Agender',inplace=True)
#print(data.head())

gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here
#print(data.head())
alignment=data['Alignment'].value_counts()
alignment.plot(kind='pie')
#plt.label()


# --------------
#Code starts here

sc_df=data[['Strength','Combat']]
#print(sc_df.head())

sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()

sc_pearson=sc_covariance/(sc_strength*sc_combat)
print('sc_pearson  :',sc_pearson)

#----------------------------------------------------------------------------
#------------------------------------------------------------------------------


ic_df=data[['Intelligence','Combat']]
#print(ic_df.head())

ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()

ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print('ic_pearson  :',ic_pearson)



# --------------
#Code starts here
total_high=data['Total'].quantile(0.99)
print(total_high)
super_best=data[data['Total']>total_high]
#print(super_best)
super_best_names=super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1,figsize=(10,4))
data['Intelligence'].plot(ax=ax_1, kind='bar')
ax_1.set_title('Intelligence')
ax_2.boxplot(data["Speed"])
ax_2.set_title('Speed')
ax_3.boxplot(data["Power"])
ax_3.set_title('Power')


