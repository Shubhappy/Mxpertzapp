import dash
from dash import html, dcc, Dash
from dash import dash_table as dt
from dash.dependencies import Input, Output
from pandas import *
import plotly.graph_objs as go
import plotly.express as px
#from dash.exceptions import PreventUpdate
import pandas as pd
# import numpy as np
# import pathlib
# from app import app


# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("data").resolve()

# df=pd.read_csv(DATA_PATH.joinpath('E:\Shubham\Shubham\Mxpertz app\src\data\Sales.Csv'))


# df=pd.read_csv('E:\Shubham\Shubham\Mxpertz app\Data file\Sales.Csv') #change no. format and remove , from no., otherwise code will not take it as integer

# city=dataframe.State/City.unique().tolist()

# Layout design
'''app.layout=html.Div ([
    #html.H1("This app is for analysis purpose", style={'color':'red','textAlign':'center','fontSize':50, 'text-decoration':'underline','text-shadow': '3px 2px gray','font-style': 'oblique','font-family': 'Verdana'}),
   #html.H4(html.Img(src='/assets/mxpertz.jpg',height='100px',style={'padding':'5px','margin':'5px'}),style={'textAlign':'left'}),
    html.Img(src='/assets/mxpertz.jpg',height='200px',width='200px',style={'padding':'0px','margin':'0px 100px 0px 500px','justify-contens':'center'}),

    html.Hr(), # Used for break
   
    html.Div([
        dcc.Link(children=page['name'],href=page["path"],style={'position':'fixed','color':'black','backgroundColor':'white','border':'1px grey','margin-left': '0px','padding-top': '5px','text-align': 'center','font-weight': '900','width':'16rem'})   
        
        for page in dash.page_registry.values()
            ]),
        #content of each page
        dash.page_container,
        html.Img(src='/assets/mxpertz.jpg',height='500px',width='500px',style={'padding':'10px','margin':'0px','textAlign':'center'},alt="Mxpertz Logo",title='Mxpertz Logo')
])'''







# Web page initialization
app=dash.Dash(__name__,title='Mxpertz',use_pages=True)
server=app.server
# dash.register_page("home", layout="We're home!", path="/")


app.layout=html.Div([
    # Logo and title of page div
#     html.Div([
#         html.Img(
#             src='/assets/mxpertz.jpg',className='logo_image'
#         ),
#         html.H6(
#             'Analysis Software',className='title_text'
#         ),
    
#     # Month title    
#         html.P('Month',className='month'),

#     # Month dropdown    
#         dcc.Dropdown(id='select_month',placeholder='Select the month',options=[{'label':i,'value':i} for i in df['Months']], value='JAN',clearable=True,className='month_dropdown'),

        
            html.Div([
            
                # html.Img(src='/assets/mxpertz.jpg',className='logo_image'),
                # html.H6('Analysis Software',className='title_text'),
                

                dcc.Link(children=page['name']+"    "  ,href=page["path"],style={'position':'relative','color':'black','backgroundColor':'white','border':'1px grey','margin-left': '0px','padding-top': '5px','text-align': 'left','font-weight': '900','width':'20rem'},className='link')   
                for page in dash.page_registry.values()
                  
            
       ],
       className="TopHeader")
       
            
        
       

       ,


        #content of each page
        html.Div([dash.page_container])
        ])


# #     # #Second row div starts here
# #     # html.Div([
# #     #     html.H6("Please Select the Service",className='service_div_heading'),
        
# #     #     dcc.RadioItems(options=[{'label':'Web Development','value':'Web Development'},
# #     #                             {'label':'Mobile App Development','value':'Mobile App Development'},
# #     #                             {'label':'Custom Software Development','value':'Custom Software Development'}],
# #     #                           inline=True, className='services')
# #     #         ],
# #     #         className='radio_div'),



#      html.Div((
#            dcc.Graph(id='chart1', className='guage',animate=True, animation_options={  'frame': { 'redraw': False, },'transition': { 'duration': 1000, 'ease': 'cubic-in-out'}},config={'displaylogo': False,'displayModeBar':'hover'}),

#            dcc.Graph(id='chart2', className='guage',animate=True, animation_options={'transition': { 'duration': 1000, 'ease': 'cubic-in-out'}},config={'displaylogo': False}),

#            dcc.Graph(id='Inquire', className='guage1',animate=True, animation_options={},config={'displaylogo': False}),
          
#            dcc.Graph(id='order', className='guage2',animate=True, animation_options={},config={'displaylogo': False}),

#            dcc.Graph(id='item_sold', className='guage3',animate=True, animation_options={},config={'displaylogo': False})
          
#            ),

#            className='indicator' )

        #     ])



# @app.callback(Output('chart1', 'figure'),
#                  # Output('chart2', component_property='fig1'),
#                [Input('select_month', 'value')])
# def build_graph(month):
#      #print(month)
    
#      dff=df[df.Months==month]
#      dff.Months.to_dict()
#      #print(dff.Months)
#      key=[k for k, v in dff.Months.items() if v==month] 
#      indx=''
#      for element in key:
#          indx=element       

#          revenue=df.Revenues.iloc[indx]
#          target= df.Target.iloc[indx]        

#      fig=go.Figure(go.Indicator(
#              customdata=[1,2,3,4,5],
#              mode = "number+gauge+delta", value = revenue,number={'valueformat':"0d"},visible=None,align='left',name="Revenue Generated",legendgrouptitle={'text' :'Revenue Generated'},
#              domain = {'x': [0, 0.5], 'y': [0, 1]},
#              title = {'text' :"<b>Sale (in ₹)</b>"},
#              delta = {'reference': target,'valueformat':"0d"},
#              gauge = {
#                      'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
#                      'axis': {'range': [None, 6000],'tickwidth': 1.5,'nticks':10,'ticksuffix':' ₹','ticks':"inside",'ticklen':5},
#                      'threshold': {
#                          'line': {'color': "red", 'width': 2},
#                          'thickness': 0.75,
#                          'value': target},
#                      }
#              ))
       
#      return fig
    


    
# @app.callback(Output('chart2', 'figure'),
#                [Input('select_month', 'value')]) 
    
# def build_graph1(month):
#      #print(month)
       
#      dff=df[df.Months==month]
#      dff.Months.to_dict()
#      #print(dff.Months)
#      key=[k for k, v in dff.Months.items() if v==month] 
#      indx=''
#      for element in key:
#          indx=element       
#          profit=df.Profit.iloc[indx]
#          # cost= df.Production_cost.iloc[indx]+df.Other_Cost.iloc[indx] 
   
    
#      fig1=go.Figure(go.Indicator(
#              customdata=[1,2,3,4,5],
#              mode = "number+gauge+delta", value = profit,number={'valueformat':"0d"},visible=True,align='left',name="Profit Generated",legendgrouptitle={'text' :'Profit Generated'},
#              domain = {'x': [0, 0.5], 'y': [0, 1]},
#              title = {'text' :"<b>Profit/Loss (in ₹)</b>"},
#              # delta = {'reference': cost,'valueformat':"0d"},
#              gauge = {
#                      'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
#                      'axis': {'range': [-1500, 5500],'tickwidth': 1.5,'nticks':10,'ticksuffix':' ₹','ticks':"inside",'ticklen':5},
#                      # 'threshold': {
#                      #     'line': {'color': "red", 'width': 2},
#                      #     'thickness': 0.75,
#                      #     'value': cost},
#                      }
#              ))
       
#      return fig1



# @app.callback(Output('Inquire', 'figure'),
#                [Input('select_month', 'value')])

# def build_graph2(month):
#      #print(month)
       
#      dff=df[df.Months==month]
#      dff.Months.to_dict()
#      #print(dff.Months)
#      key=[k for k, v in dff.Months.items() if v==month] 
#      indx=''
#      for element in key:
#          indx=element       
#          inquiries=df.Inquiries.iloc[indx]
     
#      fig2=go.Figure(go.Indicator(
#              customdata=[1,2,3,4,5],
#              mode = "number+gauge+delta", value = inquiries,number={'valueformat':"0d"},visible=True,align='left',name="Inquiries received",legendgrouptitle={'text' :'Inquiries Received'},
#              domain = {'x': [0, 0.5], 'y': [0, 1]},
#              title = {'text' :"<b>Inquiries received</b>"},
#              # delta = {'reference': inquiries,'valueformat':"0d"},
#              gauge = {
#                      'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
#                      'axis': {'range': [250, 500],'tickwidth': 1.5,'nticks':10,'ticks':"inside",'ticklen':5},
#                      # 'threshold': {
#                      #     'line': {'color': "red", 'width': 2},
#                      #     'thickness': 0.75,
#                      #     'value': inquiries},
#                      },
            
#              ))
#      return fig2



# @app.callback(Output('order', 'figure'),
#                [Input('select_month', 'value')])

# def build_graph3(month):
#      #print(month)
       
#      dff=df[df.Months==month]
#      dff.Months.to_dict()
#      #print(dff.Months)
#      key=[k for k, v in dff.Months.items() if v==month] 
#      indx=''
#      for element in key:
#          indx=element       
#          order=df.Orders_Placed.iloc[indx]
      
#      fig3=go.Figure(go.Indicator(
#              customdata=[1,2,3,4,5],
#              mode = "number+gauge+delta", value = order,number={'valueformat':"0d"},visible=True,align='left',name="Order Placed",legendgrouptitle={'text' :'Profit Generated'},
#              domain = {'x': [0, 0.5], 'y': [0, 1]},
#              title = {'text' :"<b>Order placed</b>"},
#              # delta = {'reference': inquiries,'valueformat':"0d"},
#              gauge = {
#                      'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
#                      'axis': {'range': [0, 100],'tickwidth': 1.5,'nticks':10,'ticks':"inside",'ticklen':5},
#                      # 'threshold': {
#                      #     'line': {'color': "red", 'width': 2},
#                      #     'thickness': 0.75,
#                      #     'value': inquiries},
#                      },
           
#              ))
#      return fig3


# @app.callback(Output('item_sold', 'figure'),
#                [Input('select_month', 'value')])

# def build_graph4(month):
#      #print(month)
       
#      dff=df[df.Months==month]
#      dff.Months.to_dict()
#      #print(dff.Months)
#      key=[k for k, v in dff.Months.items() if v==month] 
#      indx=''
#      for element in key:
#          indx=element       

#          sale=df.Item_Sold.iloc[indx]
      
#      fig4=go.Figure(go.Indicator(
#              customdata=[1,2,3,4,5],
#              mode = "number+gauge+delta", value = sale,number={'valueformat':"0d"},visible=True,align='left',name="Items Sold",legendgrouptitle={'text' :'Items Sold'},
#              domain = {'x': [0, 0.5], 'y': [0, 1]},
#              title = {'text' :"<b>Total Items Sold</b>"},
#              # delta = {'reference': inquiries,'valueformat':"0d"},
#              gauge = {
#                      'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
#                      'axis': {'range': [0, 100],'tickwidth': 1.5,'nticks':10,'ticks':"inside",'ticklen':5},
#                      # 'threshold': {
#                      #     'line': {'color': "red", 'width': 2},
#                      #     'thickness': 0.75,
#                      #     'value': inquiries},
#                      },
            
#              ))
#      return fig4



# calling the server to run the dashboard    
if __name__=='__main__':
    app.run_server(debug=True)