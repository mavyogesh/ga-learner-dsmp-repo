# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode
# code starts here
bank=pd.DataFrame()
bank= pd.read_csv(path, sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
categorical_var =bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)






# code ends here


# --------------
# code starts here
bank.drop('Loan_ID',axis=1,inplace=True)
banks=bank.copy()
print(banks.isnull().sum())
bank_mode = bank.mode()
banks.fillna(np.nan,inplace=True)
banks =banks.replace(np.nan,bank_mode)

#code ends here


# --------------
# Code starts here
avg_loan_amount=banks.pivot_table(index=['Gender', 'Married','Self_Employed'],values='LoanAmount')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
a =banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y') ]
loan_approved_se =a.shape[0]
b =banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y') ]
loan_approved_nse =b.shape[0]
percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term  = loan_term[loan_term>=25].count()


# code ends here


# --------------
# code starts here

loan_groupby =banks.groupby(['Loan_Status'])
loan_groupby =loan_groupby[['ApplicantIncome','Credit_History']]
mean_values =loan_groupby.mean()




# code ends here


