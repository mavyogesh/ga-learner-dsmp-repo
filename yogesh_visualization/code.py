# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# code starts here
data=pd.DataFrame()
data= pd.read_csv(path, sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
loan_status =data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
plt.show()


#Code starts here


# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=90)



# --------------
#Code starts here
education_and_loan =data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']
pd.Series(graduate['LoanAmount']).plot(kind='density' , label='Graduate')
pd.Series(not_graduate['LoanAmount']).plot(kind='density' , label='not_graduate')



#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) =plt.subplots(nrows = 3 , ncols = 1)
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)
plt.xlabel('Applicant Income')
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
plt.xlabel('Coapplicant Income')
data['TotalIncome'] =data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_2)
plt.xlabel('Total Income')

plt.show()





