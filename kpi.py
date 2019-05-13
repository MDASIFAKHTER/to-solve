
# coding: utf-8

# In[ ]:


import pandas as pd
import pandasql as ps


# In[ ]:


# =============================================================================
# KPI's
# 1. %ACtive Users
High during June,July,August : might be due to summer Holidays. Demand is more in these months


# 2. Percentage of Completed Trips	Rejected Trips	Cancelled Trips
# Give an insight :
  Trip rejection Ratio is highest in Churned January,February,December


# 3. Churned Captain Rate: Churned Captain/(Active Captains + New Captains)
Churned Captain Rate is highest dunring Feb,July,Aug.



# 4. % of new Captians added.
# This will show expansion of employee numbers 
# =============================================================================



# In[ ]:



path= r"C:\Personal\Careem EM_BIA_case_study(1).xlsx"

#['User id', 'Join Date', 'Gender']
Table1  = pd.read_excel(path,sheet_name="Sheet1")

#['Trip id', 'Trip Date ', 'Captain ID ', 'User ID']
Table2  = pd.read_excel(path,sheet_name="Sheet2")

# =============================================================================
# How many women took a trip? How many trips?
# Please have a check on this
# =============================================================================
q1 = """ SELECT count(*) as [Women],count([Trip id]) as [No of Trips] FROM Table1 join Table2 on Table1.[User id]=Table2.[User id] where Gender="F" """
print(ps.sqldf(q1, locals()))
# =============================================================================
# How many men took a trip on the same day they joined?
# =============================================================================
q2 = """SELECT count(*) FROM Table1 join Table2 on Table1.[User id]=Table2.[User id] where Gender="M" and Table1.[Join Date]= Table2.[Trip Date]"""
print(ps.sqldf(q2, locals()))

