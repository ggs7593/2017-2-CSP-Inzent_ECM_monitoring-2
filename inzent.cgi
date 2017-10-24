#!/usr/bin/python
# coding: utf-8
import matplotlib, cgi, cgitb
matplotlib.use('Agg')
cgitb.enable()
from pandas import read_sql
from sqlalchemy import create_engine
from mpld3 import fig_to_html
conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')

form = cgi.FieldStorage()
sy = int(form.getvalue('sy'))
sm = int(form.getvalue('sm'))
sd = int(form.getvalue('sd'))
ey = int(form.getvalue('ey'))
em = int(form.getvalue('em'))
ed = int(form.getvalue('ed'))
fn = form.getvalue('file')

groupby = ''
kind = 'line'
sel_vol = ''
if sy == ey and sm == em and sd == ed: 
    kind = 'bar'#bar graph
    sel_vol = ', VOLUMEID'
    
if sm == 0: 
    groupby = 'Year(date)'
    ey += 1
elif sd == 0: 
    groupby = 'Year(date), Month(date)'
    em += 1
else : groupby = 'date'

start = "'" + str(sy) + '-' + str(sm) + '-' + str(sd) + "'"
end = "'" + str(ey) + '-' + str(em) + '-' + str(ed) + "'"
alias = ['Total', 'storage1', 'storage2']
vol = [' ', " and VOLUMEID='1HS_V001' ", " and VOLUMEID='2HS_V001' "]

df = []
for i in range(3):
    query = "select sum(FILESIZE) as " + alias[i] + sel_vol + ", date from data where Date(date) >= " + start + " and Date(date) <= " + end + vol[i] + " group by " + groupby + sel_vol
    df.append(read_sql(query, conn))

if kind == 'bar':
    df[0] = df[0].append({'Total': df[0].loc[0,'Total'] + df[0].loc[1, 'Total'], 'VOLUMEID' : 'Total', 'date' : ''}, ignore_index=True)
    ax = df[0].plot(x='VOLUMEID',y='Total', kind='bar')
else:
    ax = df[0].plot(x='date', kind=kind)
    df[1].plot(x='date', ax=ax, kind=kind)
    df[2].plot(x='date', ax=ax, kind=kind)

if fn: df[0].to_excel('file/'+fn)

fig = ax.get_figure()
print 'Content-type:text/html;\r\n\r\n'
print fig_to_html(fig)
