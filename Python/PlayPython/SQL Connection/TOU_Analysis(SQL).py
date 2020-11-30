#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import cx_Oracle
import datetime as dt
from pivottablejs import pivot_ui


# In[2]:


username = "PECUTILOTST"
password = "PECUTILOTST"
host = "dboratst.spsi.co.za"
service = "tst"


# In[3]:


# create connection 
connection = cx_Oracle.connect(username, password, host+"/"+service)


# In[4]:


#Create cursor
cur = connection.cursor()


# In[5]:


sql_select = """SELECT
MPR.NAME ,MR.ICE_METERREADINGDATE ,MR.ICE_METER_READING ,MR.QTY
FROM ICE_METERREADINGS MR
INNER JOIN ICE_METER MP ON MR.ICE_METER_ID = MP.ICE_METER_ID
INNER JOIN ICE_METER_REGISTER MPR ON MR.ICE_METER_REGISTER_ID = MPR.ICE_METER_REGISTER_ID
WHERE MP.ICE_METER_NUMBER='{}'
AND MR.ICE_METERREADINGDATE BETWEEN TO_DATE('{}','dd-MON-YY hh24:mi:ss') 
AND TO_DATE('{}','dd-MON-YY hh24:mi:ss') 
ORDER BY MR.ICE_METERREADINGDATE ASC""".format(input('Meter number: '),
                                               input('Date From (DD-MON-YY HH:MM:SS): '),
                                               input('Date To (DD-MON-YY HH:MM:SS): '))


# In[6]:


Readings = pd.read_sql_query(sql_select,con=connection)
Readings.head()


# In[7]:


cur.close()
connection.close()


# In[8]:


weekDays = ("Weekdays","Weekdays","Weekdays","Weekdays","Weekdays","Saturday","Sunday")


# In[9]:


Readings['MONTH'] = Readings['ICE_METERREADINGDATE'].apply(lambda x : x.month)
Readings['DAY'] = Readings['ICE_METERREADINGDATE'].apply(lambda x : x.day)
Readings['HOUR'] = Readings['ICE_METERREADINGDATE'].apply(lambda x : x.hour)
Readings['MIN'] = Readings['ICE_METERREADINGDATE'].apply(lambda x : x.minute)
Readings['DOW'] = Readings['ICE_METERREADINGDATE'].apply(lambda x :weekDays[x.weekday()])
Readings.head()


# In[10]:


Registers=list(dict.fromkeys(Readings['NAME']))
NA_REG = ['T2_KWH-kWh','T2_MAX_DEMAND_KVA-kVA','Total (kVA)-kVA']
Registers


# In[11]:


TOU = Readings[(Readings.NAME !=NA_REG[0]) & (Readings.NAME !=NA_REG[1]) & (Readings.NAME !=NA_REG[2])]
TOU.head(2)


# In[12]:


X=list(dict.fromkeys(TOU['DAY']))
Y=list(dict.fromkeys(TOU['MONTH']))


# In[13]:


f = open("TOU_Analysis_Output.TXT","w+")
f.write('TOU Analysis Results: ({}/{} - {}/{})'.format(X[0],Y[0],X[-1],Y[-1]))
f.write('\n'*2)
for i in X:
    f.write('Day '+str(i)+'\n')
    f.write('1)TOU consumption' + ' = ' + str(round(sum(TOU[(TOU.DAY ==i) & (TOU.QTY >0) & (TOU.NAME !='Active power (P) Import Total (kW)-kWh') ]['QTY']),2))+' kWh' + '\n')
    f.write('2)Total consumption' + ' = '+ str(round(sum(TOU[(TOU.DAY ==i) & (TOU.QTY >0) & (TOU.NAME =='Active power (P) Import Total (kW)-kWh') ]['QTY']),2))+ ' kWh'+'\n')
    f.write('3)Difference = ' + str(round((sum(TOU[(TOU.DAY ==i) & (TOU.QTY >0) & (TOU.NAME =='Active power (P) Import Total (kW)-kWh') ]['QTY']))-(sum(TOU[(TOU.DAY ==i) & (TOU.QTY >0) & (TOU.NAME !='Active power (P) Import Total (kW)-kWh') ]['QTY'])),2))+' kWh' + '\n')
    f.write('\n')
    #print(str(i)+' Difference = ' + str(round((sum(TOU[(TOU.DAY ==i) & (TOU.QTY >0) & (TOU.NAME =='Active power (P) Import Total (kW)-kWh') ]['QTY']))-(sum(TOU[(TOU.DAY ==i) & (TOU.QTY >0) & (TOU.NAME !='Active power (P) Import Total (kW)-kWh') ]['QTY'])),2))+' kWh' + '\n')
f.close()


# In[14]:


pivot_ui(TOU,outfile_path='TOU_Analysis.html',width=0,height=0)

