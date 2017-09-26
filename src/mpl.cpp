#include<iostream>
#include<string>
#include"util.h"
using namespace std;
int main()
{
	string command = R"(python -c "
import sqlalchemy as sql
import pandas as pd
import mpld3 as d3
import matplotlib as plt
import warnings
warnings.filterwarnings('ignore')
conn  = sql.create_engine('mysql://zezeon:cockcodk0@localhost/csv?charset=utf8')
df = pd.read_sql('select * from mountains;', conn)
ax = df.plot()
fig = ax.get_figure()
print d3.fig_to_html(fig)
")";

	string s = psstm(command);
	
	cout << "Content-type:text/html\r\n\r\n";
	cout << s;
	
}
