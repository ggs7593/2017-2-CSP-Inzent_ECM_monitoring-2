#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import sqlalchemy as sql
import pandas as pd
import mpld3 as d3
import matplotlib.pyplot as plt
import warnings, json
import cgi
import cgitb
cgitb.enable()

warnings.filterwarnings('ignore')
conn  = sql.create_engine('mysql://zezeon:cockcodk0@localhost/csv?charset=utf8')
df = pd.read_sql('select * from mountains;', conn)
ax = df.plot();
#df.to_excel('df.xlsx')
fig = ax.get_figure();
print 'Content-type:text/html\r\n\r\n'
print d3.fig_to_html(fig);
#print json.dumps(d3.fig_to_dict(fig))
