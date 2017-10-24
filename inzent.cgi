#!/usr/bin/python
# coding: utf-8

# In[1]:

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import sqlalchemy as sql
import mpld3 as d3
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
conn = sql.create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')


# In[42]:

import cgi
import cgitb
#cgitb.enable()
#form = cgi.FieldStorage()
#sy = form.getvalue('sy')
#sm = form.getvalue('sm')
#sd = form.getvalue('sd')
#ey = form.getvalue('ey')
#em = form.getvalue('em')
#ed = form.getvalue('ed')
#fn = form.getvalue('file')


# In[115]:

sy = 2016
sm = 7
sd = 1
ey = 2016
em = 8
ed = 31
fn = ''


# In[116]:

groupby = ''
kind = 'line'
sel_vol = ''
if sy == ey and sm == em and sd == ed: kind = 'bar'#bar graph
    
if sm == 0: 
    groupby = 'Year(date)'
    ey += 1
elif sd == 0: 
    groupby = 'Year(date), Month(date)'
    em += 1
else : 
    groupby = 'date'

if kind == 'bar': sel_vol = ', VOLUMEID'

start = "'" + str(sy) + '-' + str(sm) + '-' + str(sd) + "'"
end = "'" + str(ey) + '-' + str(em) + '-' + str(ed) + "'"

alias = ['Total', 'storage1', 'storage2']
vol = [' ', " and VOLUMEID='1HS_V001' ", " and VOLUMEID='2HS_V001' "]



# In[117]:

df = []
for i in range(3):
    query = "select sum(FILESIZE) as " + alias[i] + sel_vol + ", date from data where Date(date) >= " + start + " and Date(date) <= " + end + vol[i] + " group by " + groupby + sel_vol
    df.append(pd.read_sql(query, conn))


# In[118]:

if kind == 'bar':
    df[0] = df[0].append({'Total': df[0].loc[0,'Total'] + df[0].loc[1, 'Total'], 'VOLUMEID' : 'Total', 'date' : ''}, ignore_index=True)
    ax = df[0].plot(x='VOLUMEID',y='Total', kind='bar')
else:
    ax = df[0].plot(x='date', kind=kind)
    df[1].plot(x='date', ax=ax, kind=kind)
    df[2].plot(x='date', ax=ax, kind=kind)
#plt.show()


# In[114]:

fig = ax.get_figure()
print 'Content-type:text/html;\r\n\r\n'
print d3.fig_to_html(fig)
#print 'hello'
if fn != "": df[0].to_excel(fn)


# In[ ]:



