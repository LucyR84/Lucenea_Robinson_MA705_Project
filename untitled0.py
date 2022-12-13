# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:04:24 2022

@author: Lucy
"""
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash import dash_table


games_data = pd.read_csv('rawg_games_Final.zip')
game_platforms = pd.read_csv('game_platforms_updated.csv')
game_stores = pd.read_csv('game_stores.csv')
game_genres = pd.read_csv('game_genres.csv')
game_tags = pd.read_csv('game_tags.csv')
years_summary = pd.read_csv('years_summary.csv')


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[stylesheet])
server = app.server

games_data['Release Date']= pd.to_datetime(games_data['Release Date'])
years_set = set(games_data['Release Date'].dt.strftime('%Y').unique())


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Interactive Chart Dataframe
df = games_data[games_data['Platform Types'].str.contains('Console')]
df1 = df.groupby(df['Release Date'].dt.strftime('%Y'))['Game Name'].count().reset_index()
df1.rename(columns = {"Game Name": "Number of Games"}, inplace = True)
df1['Percentage of Games Released'] = [(x / y) 
                                       for x, y in 
                                       zip(df1['Number of Games'],
                                           years_summary['Number of Games Released'])]


# Interactive Table Dataframe
df2 = df.to_dict('records')

# Interactive chart
fig = px.bar(df1, x = 'Release Date' , y = 'Percentage of Games Released')




subcategory_list = game_platforms['Type'].unique().tolist()

# add percentage increase column 

table = generate_table(years_summary)


app.layout =html.Div([
            html.H1('Yearly Game Release Comparison',
                    style={"font-weight": "bold",
                           'font-size':50,
                           'color':'#3A84CA'}),
            html.Div([html.H5('MA 705 Dashboard Final Project | Lucenea Robinson'),
            html.H6("About", style={"font-weight": "bold"}),
            html.H6("""
                    This dashboard explores what trends are happening in the game industry by visualizing 
                    data of games released for years 2015 to 2022 by looking at the percentage of games 
                    that fall into various categories for a given year. This approach was mainly chosen 
                    to make the years comparative, because of the stark difference in the number of games 
                    released each year. As shown in the table to the right, the number of games has increased 
                    each year by at least 10%, except 2022.
                    However, the data for 2022 only goes up to December 2, 2022, which means 
                    there could still be a positive increase considering there is an average of about 14,000 
                    games released each month. With this upward trend, the dashboard explores what other 
                    possible trends might surround genres, platforms, platform types, stores, and game tags. 
                    Each of these categories is further divided into sub-categories. This is because games 
                    can be available in multiple sub-categories and a comparison between genres would be 
                    misleading if a game falls in both categories. With this in mind, the chart below was 
                    designed to show how represented games are for a given subcategory and how has the 
                    representation changed year over year. The table below the chart shows the name and 
                    other details of the games that fall within the chosen parameters.
                     
                    """,),
            html.H6(["""
                    The data used for this dashboard is taken from the """, 
                    html.A('RAWG.io',
                           href='https://rawg.io/',
                           target='_blank'),
                    """ database, through its free """,
                    html.A('API service',
                           href = 'https://rawg.io/apidocs',
                           target='_blank'),
                    """. 
                    After data collection and cleaning, a total of 745,143 games, 40 platforms, 
                    20 genres, 11 stores, 6 platform types, and over 80,000 unique tags are 
                    represented on the dashboard.
                    """]),
            html.Br(),
            html.H6("""*User Discretion Advised: There are many games rated for mature audiences, and so
                    game names may contain inappropriate language.*""", 
                     style={"font-weight":"bold", "font-size":12}),
            
            html.Br(),
            html.H6("How to Use", style={"font-weight": "bold"}),
            html.H6("""
                    First, select the category you are interested in from the first dropdown menu.
                    Then, from the second dropdown menu choose a sub-category. You can select or
                    type in the dropdown to search for a category/subcategory. Note: Chart will be 
                    blank until a sub-category is chosen.
                    """)]),
        
        # Summary table

           """ html.Div(table, id='table',
                     style={'width' : '100%',"text-align": "center"}),
            html.Br(),""",
                    
        # Select categories and sub-categories
            html.Br(),
            html.Br(),
            # CATEGORY
            html.H5('Select a Category',
                    style={'width' : '100%',
                           'text-align' : 'left',
                           'justify':'left'}),
            
            dcc.Dropdown(['Platform Types', 'Platforms', 
                          'Stores', 'Genres', 'Tags'], 
                                  'Platform Types', 
                                  searchable = True,
                                  id='category',
                                  style={'width' : '100%',
                                         'text-align' : 'left',}),
            html.Br(),
            #SUB-CATEGORY
            html.Div([html.H5('Select a Sub-category', 
                              style={'width' : '100%',
                                     'float' : 'left'})]),
            dcc.Dropdown(subcategory_list,
                         'Console',  
                         searchable = True,
                         id='sub_category',
                         style={'width' : '100%',
                                'float' : 'left'}),
            html.Br(),
            #Disclaimer
            html.H6("""Note 1: For Platform and Platform Types, the 'Other' and 'Web' sub-categories
                    are the same. This is because that is the only value under the Platform
                    category.""", 
                     style={"font-weight":"bold", "font-size":12}),
            html.H6("""Note 2: The sub-category dropdown and Chart may take a few seconds to update 
                    due to the large dataset.""", 
                     style={"font-weight":"bold", "font-size":12}),
      
        
                
        # Interactive Chart
            dcc.Graph(figure=fig,
                      id='plot',
                      style={'width' : '100%'}),
            html.Br(), 
            html.H3('Game Results',
                    style={"font-weight": "bold"}),
            html.Br(),
    
        # Interactive Table
            html.Div([dash_table.DataTable(df2, id = 'dtbl',
                                 columns = [{"name": 'Year', "id": 'Year', 'type':'numeric'},
                                            {"name": 'Release Date', "id": 'Release Date', 'type':'datetime'},
                                            {"name": 'Game', "id": 'Game Name', 'type':'text'},
                                            {"name": 'Platforms', "id": 'Platforms', 'type':'text'},
                                            {"name": 'Platform Types', "id": 'Platform Types', 'type':'text'},
                                            {"name": 'Stores', "id": 'Stores', 'type':'text'},
                                            {"name": 'Genres', "id": 'Genres', 'type':'text'},
                                            
                                            ],
                                 filter_action = 'native',
                                 page_action = 'native',
                                 page_current = 0,
                                 page_size = 10,
                                 style_table = {'overflow':'scroll'},
                                 style_data = {'height': 'auto',
                                               'whitespace':'normal'},
                                 style_cell={'textAlign': 'left', 
                                            'minWidth': '80px', 
                                            'width': '100px', 
                                            'maxWidth': '500px', 
                                            'whiteSpace':'normal', 
                                            'height':'auto'}),
                     ]),
            html.Br(),
            html.Br(), 
            html.Br(), 
            
            html.H3('References:',
                            style={"font-weight": "bold"}),
            html.H6('RAWG Database and Game API Information:'),
            html.A('https://rawg.io/',
                           href='https://rawg.io/',
                           target='_blank'),
                
            html.A('https://rawg.io/apidocs',
                   href = 'https://rawg.io/apidocs',
                   target='_blank'),
            html.Br(),

            html.H6('Plotly Dash Libraries and documentations:'),
            html.A('https://plotly.com/python/reference/layout/',
                   href='https://plotly.com/python/reference/layout/',
                   target='_blank')
            ])


@app.callback(
    Output('sub_category', 'options'),
    Input('category', 'value')
    )

def update_sub_category(category):
    if category == 'Platform Types':
        sub_category_list = game_platforms['Type'].unique().tolist()
        
    elif category == 'Platforms':
        sub_category_list = game_platforms['Platforms'].unique().tolist()

    elif category == 'Stores':
        sub_category_list = game_stores['Stores'].unique().tolist()

    elif category == 'Genres':
        sub_category_list = game_genres['Genres'].unique().tolist()

    elif category == 'Tags':
        sub_category_list = game_tags['Tags'].unique().tolist()

    return sub_category_list



@app.callback(
    Output('plot', 'figure'),
    [Input('category', 'value'), 
     Input('sub_category', 'value')]
    )


def update_dataframe(category, sub_category):
    df = games_data[games_data[category].str.contains(str(sub_category))]
    df1 = df.groupby(df['Release Date'].dt.strftime('%Y'))['Game Name'].count().reset_index()
    df1.rename(columns = {"Game Name": "Number of Games"}, inplace = True)
    df1['Percentage of Games Released'] = [(x / y)
                                           for x, y in 
                                           zip(df1['Number of Games'],
                                              years_summary['Number of Games Released'])]
    
    
    missing_years = years_set.difference(set(df1['Release Date'].unique()))
    
    if missing_years != set():
        for year in missing_years:
            new_row = {'Release Date':year,'Number of Games':0, 'Percentage of Games Released':0}
            df1 = pd.concat([df1,pd.DataFrame(new_row, index=[0])], ignore_index=True)
    
    df1 = df1.sort_values(by=['Release Date'])
    
    title = ''
    
    if category == 'Platform Types':
        title = ('The Percentage of Yearly Games Released that are Playable on Platform Type: '
        + str(sub_category))
    elif category == 'Platforms':
         title = ('The Percentage of Yearly Games Released that are Playable on Platform: '
         + str(sub_category))
    elif category == 'Genres':
         title = ('The Percentage of Yearly Games Released that are of Genre: '
         + str(sub_category))
    elif category == 'Stores':
         title = ('The Percentage of Yearly Games Released that are Available at Store: '
         + str(sub_category))
    elif category == 'Tags':
         title = ('The Percentage of Yearly Games Released that have Tag: '
         + str(sub_category))
    
    fig = px.bar(df1, x = 'Release Date' , y = 'Percentage of Games Released' 
                 )
    fig.update_layout(
        title={'text':title},
        yaxis={'tickformat': ',.2%'})

    return fig

@app.callback(
    Output('dtbl', 'data'),
    [Input('category', 'value'), 
     Input('sub_category', 'value')]
    )

def create_json_df(category, sub_category):
    df = games_data[games_data[category].str.contains(str(sub_category))]
    df2 = df.to_dict('records')

    return df2


if __name__ == '__main__':
    app.run_server(debug=True)