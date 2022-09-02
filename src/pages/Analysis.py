import dash
from dash import html, dcc, Dash, callback
# from dash import dash_table as dt
from dash.dependencies import Input, Output
from pandas import *
import plotly.graph_objs as go
# import plotly.express as px
# from dash.exceptions import PreventUpdate
import pandas as pd
# import numpy as np
# from app import app


dash.register_page(__name__,name="Analysis", path="/") 

df=pd.read_csv('E:\Shubham\Shubham\Mxpertz app\src\data\Sales.csv') #change no. format and remove , from no., otherwise code will not take it as integer

layout = html.Div([
     html.Img(src='/assets/mxpertz.jpg',className='logo_image'),
     html.H6('Analysis Software',className='title_text'),
#     html.H1(children='This is our Home page'),
#     html.Div(html.Marquee(children='''This is our Home page content''',loop=True,dir='ltr')),
#    # html.Img(src='/assets/mxpertz.jpg',sizes='1000px',style={'padding':'50px'}),
#      html.Audio(src='/assets/Airtel.mp3', controls=True),    

    # #Second row div starts here
    # html.Div([
    #     html.H6("Please Select the Service",className='service_div_heading'),
        
    #     dcc.RadioItems(options=[{'label':'Web Development','value':'Web Development'},
    #                             {'label':'Mobile App Development','value':'Mobile App Development'},
    #                             {'label':'Custom Software Development','value':'Custom Software Development'}],
    #                           inline=True, className='services')
    #         ],
    #         className='radio_div'),

    
  

    html.Div((
            html.P('Month',className='month'),
            dcc.Dropdown(id='select_month',placeholder='Select the month',options=[{'label':i,'value':i} for i in df['Months']], value='JAN',clearable=True,className='month_dropdown'),

          dcc.Graph(id='chart1', className='guage',animate=True, animation_options={  'frame': { 'redraw': False, },'transition': { 'duration': 1000, 'ease': 'cubic-in-out'}},config={'displaylogo': False,'displayModeBar':'hover'}),

          dcc.Graph(id='chart2', className='guage',animate=True, animation_options={'transition': { 'duration': 1000, 'ease': 'cubic-in-out'}},config={'displaylogo': False}),

          dcc.Graph(id='Inquire', className='guage1',animate=True, animation_options={},config={'displaylogo': False}),
          
          dcc.Graph(id='order', className='guage2',animate=True, animation_options={},config={'displaylogo': False}),

          dcc.Graph(id='item_sold', className='guage3',animate=True, animation_options={},config={'displaylogo': False})
          
          ),className='indicator')

            
],className='analysis_div')



@callback(Output('chart1', 'figure'),
                # Output('chart2', component_property='fig1'),
              [Input('select_month', 'value')])
def build_graph(month):
    #print(month)
    
    dff=df[df.Months==month]
    dff.Months.to_dict()
    #print(dff.Months)
    key=[k for k, v in dff.Months.items() if v==month] 
    indx=''
    for element in key:
        indx=element       

        revenue=df.Revenues.iloc[indx]
        target= df.Target.iloc[indx]        

    fig=go.Figure(go.Indicator(
            customdata=[1,2,3,4,5],
            mode = "number+gauge+delta", value = revenue,number={'valueformat':"0d"},visible=None,align='left',name="Revenue Generated",legendgrouptitle={'text' :'Revenue Generated'},
            domain = {'x': [0, 0.5], 'y': [0, 1]},
            title = {'text' :"<b>Sale (in ₹)</b>"},
            delta = {'reference': target,'valueformat':"0d"},
            gauge = {
                    'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
                    'axis': {'range': [None, 6000],'tickwidth': 1.5,'nticks':10,'ticksuffix':' ₹','ticks':"inside",'ticklen':5},
                    'threshold': {
                        'line': {'color': "red", 'width': 2},
                        'thickness': 0.75,
                        'value': target},
                    }
            ))
        
    return fig
    


    
@callback(Output('chart2', 'figure'),
              [Input('select_month', 'value')]) 
    
def build_graph1(month):
    #print(month)
        
    dff=df[df.Months==month]
    dff.Months.to_dict()
    #print(dff.Months)
    key=[k for k, v in dff.Months.items() if v==month] 
    indx=''
    for element in key:
        indx=element       

        profit=df.Profit.iloc[indx]
        # cost= df.Production_cost.iloc[indx]+df.Other_Cost.iloc[indx] 
    
    
    fig1=go.Figure(go.Indicator(
            customdata=[1,2,3,4,5],
            mode = "number+gauge+delta", value = profit,number={'valueformat':"0d"},visible=True,align='left',name="Profit Generated",legendgrouptitle={'text' :'Profit Generated'},
            domain = {'x': [0, 0.5], 'y': [0, 1]},
            title = {'text' :"<b>Profit/Loss (in ₹)</b>"},
            # delta = {'reference': cost,'valueformat':"0d"},
            gauge = {
                    'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
                    'axis': {'range': [-1500, 5500],'tickwidth': 1.5,'nticks':10,'ticksuffix':' ₹','ticks':"inside",'ticklen':5},
                    # 'threshold': {
                    #     'line': {'color': "red", 'width': 2},
                    #     'thickness': 0.75,
                    #     'value': cost},
                    }
            ))
        
    return fig1



@callback(Output('Inquire', 'figure'),
              [Input('select_month', 'value')])

def build_graph2(month):
    #print(month)
        
    dff=df[df.Months==month]
    dff.Months.to_dict()
    #print(dff.Months)
    key=[k for k, v in dff.Months.items() if v==month] 
    indx=''
    for element in key:
        indx=element       

        inquiries=df.Inquiries.iloc[indx]
       
    fig2=go.Figure(go.Indicator(
            customdata=[1,2,3,4,5],
            mode = "number+gauge+delta", value = inquiries,number={'valueformat':"0d"},visible=True,align='left',name="Inquiries received",legendgrouptitle={'text' :'Inquiries Received'},
            domain = {'x': [0, 0.5], 'y': [0, 1]},
            title = {'text' :"<b>Inquiries received</b>"},
            # delta = {'reference': inquiries,'valueformat':"0d"},
            gauge = {
                    'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
                    'axis': {'range': [250, 500],'tickwidth': 1.5,'nticks':10,'ticks':"inside",'ticklen':5},
                    # 'threshold': {
                    #     'line': {'color': "red", 'width': 2},
                    #     'thickness': 0.75,
                    #     'value': inquiries},
                    },
            
            ))
    return fig2



@callback(Output('order', 'figure'),
              [Input('select_month', 'value')])

def build_graph3(month):
    #print(month)
        
    dff=df[df.Months==month]
    dff.Months.to_dict()
    #print(dff.Months)
    key=[k for k, v in dff.Months.items() if v==month] 
    indx=''
    for element in key:
        indx=element       

        order=df.Orders_Placed.iloc[indx]
       
    fig3=go.Figure(go.Indicator(
            customdata=[1,2,3,4,5],
            mode = "number+gauge+delta", value = order,number={'valueformat':"0d"},visible=True,align='left',name="Order Placed",legendgrouptitle={'text' :'Profit Generated'},
            domain = {'x': [0, 0.5], 'y': [0, 1]},
            title = {'text' :"<b>Order placed</b>"},
            # delta = {'reference': inquiries,'valueformat':"0d"},
            gauge = {
                    'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
                    'axis': {'range': [0, 100],'tickwidth': 1.5,'nticks':10,'ticks':"inside",'ticklen':5},
                    # 'threshold': {
                    #     'line': {'color': "red", 'width': 2},
                    #     'thickness': 0.75,
                    #     'value': inquiries},
                    },
            
            ))
    return fig3



@callback(Output('item_sold', 'figure'),
              [Input('select_month', 'value')])

def build_graph4(month):
    #print(month)
        
    dff=df[df.Months==month]
    dff.Months.to_dict()
    #print(dff.Months)
    key=[k for k, v in dff.Months.items() if v==month] 
    indx=''
    for element in key:
        indx=element       

        sale=df.Item_Sold.iloc[indx]
       
    fig4=go.Figure(go.Indicator(
            customdata=[1,2,3,4,5],
            mode = "number+gauge+delta", value = sale,number={'valueformat':"0d"},visible=True,align='left',name="Items Sold",legendgrouptitle={'text' :'Items Sold'},
            domain = {'x': [0, 0.5], 'y': [0, 1]},
            title = {'text' :"<b>Total Items Sold</b>"},
            # delta = {'reference': inquiries,'valueformat':"0d"},
            gauge = {
                    'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
                    'axis': {'range': [0, 100],'tickwidth': 1.5,'nticks':10,'ticks':"inside",'ticklen':5},
                    # 'threshold': {
                    #     'line': {'color': "red", 'width': 2},
                    #     'thickness': 0.75,
                    #     'value': inquiries},
                    },
            
            ))
    return fig4

