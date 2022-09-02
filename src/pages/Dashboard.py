import dash
from dash import html, dcc, callback
import plotly.express as px
import pandas as pd


dash.register_page(__name__)

col_discr_map = {'JAN':'orange', 'FEB':'darkgreen','MAR':'blue', 'APR': 'violet','MAY' : 'red','JUNE' : 'darkred',
                'JUL':'pink','AUG':'grey','SEPT':'black','OCT':'yellow','NOV':'aqua','DEC':'greenyellow'}

df1=pd.read_csv('E:\Shubham\Shubham\Mxpertz app\src\data\Sales.csv') #change no. format and remove , from no., otherwise code will not take it as integer

# Revenue pie chart
fig5=px.pie(data_frame = df1,
              values = 'Revenues', names = 'Months',
              color = 'Months',
              color_discrete_map= col_discr_map, title="<b>Total Revenue in the year</b>")

# fig5.update_layout(title_x=0.5)
fig5.update_traces(sort=False,textinfo='label+percent')

# Profit pie chart
fig6=px.pie(data_frame = df1,
              values = 'Profit', names = 'Months',
              color = 'Months',
              color_discrete_map= col_discr_map, title="<b>Month in which profit earned in the year</b>")

# fig6.update_layout(title_x=0.5)
fig6.update_traces(sort=False,textinfo='label+percent')

# No. of items sold pie chart
fig7=px.pie(data_frame = df1,
              values = 'Item_Sold', names = 'Months',
              color = 'Months',
              color_discrete_map= col_discr_map, title="<b>Month on Month Item Sale</b>")

# fig7.update_layout(title_x=0.5)
fig7.update_traces(sort=False,textinfo='label+percent')




layout = html.Div([
    html.H2(html.Marquee(children='''Let's compare the monthly sales''',loop=True,dir='ltr',className='head_marquee')),    

    html.Div([dcc.Graph(figure=fig5,className='pi'),

    dcc.Graph(figure=fig6,className='pi'),
    
    dcc.Graph(figure=fig7,className='pi')

    ],className='pie_div')

])




    

