#!/usr/bin/python
import sqlalchemy as sql
import pandas as pd
import mpld3 as d3
import matplotlib as plt
import warnings, json
warnings.filterwarnings('ignore')
conn  = sql.create_engine('mysql://zezeon:cockcodk0@localhost/csv?charset=utf8')
df = pd.read_sql('select * from mountains;', conn)
ax = df.plot()
fig = ax.get_figure()
print 'Content-type:text/html\r\n'
print json.dumps(d3.fig_to_dict(fig))
