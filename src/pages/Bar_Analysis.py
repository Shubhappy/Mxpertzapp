import dash
from dash import html, dcc, callback
import plotly.express as px
import pandas as pd


dash.register_page(__name__)

df1=pd.read_csv('E:\Shubham\Shubham\Mxpertz app\src\data\Sales.csv') #change no. format and remove , from no., otherwise code will not take it as integer

# wide_df = px.df1_wide()


fig8=px.bar(df1,x="Months", y=["Production_cost","Other_Cost","Profit"])
fig8.update_layout(barmode='relative',title="<b>Revenue achieved</b>",title_x=0.5)
fig8.update_traces(width=0.5)

fig9=px.bar(df1,x="Months", y=["Revenues","Target"])
fig9.update_layout(barmode='relative',title="<b>Revenue vs Target</b>",title_x=0.5)
fig9.update_traces(width=0.5)


layout = html.Div([
    html.Div([html.H2(html.Marquee(children='''Let's see monthly Ups & Down''',loop=True,dir='ltr',className='bar_marquee'))]),   

    # html.Hr(), 

    html.Div([
        html.Div([dcc.Graph(figure=fig8,className='revenue_stack')],className='bar'),

        html.Div([dcc.Graph(figure=fig9,className='revenue_stack')],style={'text-align': 'center'},className='bar')],
        className='bar_div')
])