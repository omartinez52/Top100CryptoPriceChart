"""
    CoinGeckoApi():
        - Uses coin gecko api to gather data from the top 100 crypto currencies based on rank.
        - Data gathered is used to create a table, similar to that on the coin gecko website: https://www.coingecko.com/en
        - Columns are neatly labeled based on information provided from coin gecko api.
        - Project focuses on HTML and CSS practices and basic Python.
"""
import pandas as pd
from pycoingecko import CoinGeckoAPI
import dash
import json
import requests
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
cg = CoinGeckoAPI()
cg = cg.get_coins_markets(vs_currency='usd')
df = pd.DataFrame(cg,
                  columns=['id',#crypto token name
                           'symbol',#crypto token symbol
                           'current_price',#crypto token current price in $usd
                           'price_change_percentage_24h',#crypto 24hr price change
                           'market_cap',#crypto token market cap in $usd
                           'image',#crypto token image src
                           'price_change_24h',#crypto 24hr price change %
                           'ath',#crypto 24hr all time high in $usd
                           'total_volume',#crypto 24hr volume in $usd
                           'high_24h', #crypto 24 hr highest price
                           'low_24h',#crypto 24hr lowest price
                           ]
                  )
df['id'] = df['id'].str.upper() #making all crypto names all capital letters
df['symbol'] = df['symbol'].str.upper() #making all crypto symbols all capital letters


app.layout = html.Div(
    children=[
        html.Div(id='main-div',
            children=[
                # baby shark png
                html.Img(src='https://pngimg.com/uploads/baby_shark/baby_shark_PNG22.png',
                         style={'width':'8%',
                                'position':'absolute',
                                'top': '5%',
                                'left':'7%',
                                }
                         ),
                # CoinShark Text Image
                html.Img(src='https://fontmeme.com/permalink/210803/4d2b539d23d9bfb5b3e059de6d5067d7.png',
                         style={"width":'13%',
                                'position':'absolute',
                                'top': '10%',
                                'left':'15%',
                                }
                         ),
                # input bar
                dcc.Input(id='token-input',
                          placeholder='Search For Token',
                          type='text',
                          persistence=False,
                          debounce=False,
                          style={'position':'absolute',
                                 'width':'30vh',
                                 'top':'11%',
                                 'left':'77%',
                                 'border-radius':'5px',
                                 }
                      ),
                # column title divider
                html.Div(id='column-titles',
                    children=[
                        # coin
                        html.Img(src='https://fontmeme.com/permalink/210803/3f00bf8afa6e02350ff284246263766a.png',
                                 style={"width":'2%',
                                        'position':'absolute',
                                        'top': '30%',
                                        'left':'3%',
                                        }
                                 ),
                        # symbol
                        html.Img(src='https://fontmeme.com/permalink/210803/4a38dd6a72348e626639d4b7c69f6a4f.png',
                                 style={"width": '3%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '18%',
                                        }
                                 ),
                        # price
                        html.Img(src='https://fontmeme.com/permalink/210803/8c599cc025314c9f9d1f2455a30e59b4.png',
                                 style={"width": '2.3%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '26%',
                                        }
                                 ),
                        # 24h volume
                        html.Img(src='https://fontmeme.com/permalink/210803/29a963aa232102fb6939806ec87f7981.png',
                                 style={"width": '5%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '35.5%',
                                        }
                                 ),
                        # 24h price change
                        html.Img(src='https://fontmeme.com/permalink/210803/50ff1a3758c649d9feb8a89adee59bda.png',
                                 style={"width": '6.5%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '46%',
                                        }
                                 ),
                        # 24h % change
                        html.Img(src='https://fontmeme.com/permalink/210803/cb5a0833e2507c3c4b1226a2659ca7ff.png',
                                 style={"width": '2.7%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '57%',
                                        }
                                 ),
                        # 24h high
                        html.Img(src='https://fontmeme.com/permalink/210803/637a8e3e4c047dfacaf05d922d70a550.png',
                                 style={"width": '3.7%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '65.3%',
                                        }
                                 ),
                        # 24h low
                        html.Img(src='https://fontmeme.com/permalink/210803/4ce69918bf3e94a4ef6711bb333e3f8d.png',
                                 style={"width": '3.7%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '74.8%',
                                        }
                                 ),
                        # ath
                        html.Img(src='https://fontmeme.com/permalink/210803/634d2a18399002ba8880dab19e2f034f.png',
                                 style={"width": '1.7%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '83.4%',
                                        }
                                 ),
                        # market cap
                        html.Img(src='https://fontmeme.com/permalink/210803/b745e01e161d2e788d1270bbec5a5fe6.png',
                                 style={"width": '5%',
                                        'position': 'absolute',
                                        'top': '30%',
                                        'left': '91%',
                                        }
                                 ),
                    ],style={'position':'absolute',
                             'top':'17%',
                             'width':'169vh',
                             'height':'3.5vh',
                             'border': '5px solid black',
                             'text-align':'center',
                             'border-radius':'10px',
                             'background-color':'#f4bcbd',
                             'color':'black',
                             }
                ),
                # div containing crypto data
                # data from callbacks update data
                html.Div(id='crypto-div',
                         children=[

                         ],
                         style={'position':'absolute',
                                'width':'169vh',
                                "border": "5px solid black",
                                'border-radius':'10px',
                                "overflow": "hidden",
                                'text-align':'center',
                                'top':'21.5%',
                                'background-color':'#bcf4d6',
                                }
                 ),
                ],style=dict(display='flex',
                             justifyContent='center',
                             top='50%',
                             ),
        ),
    ],style={'background-color':'#c8ccff',
             'height':'715vh',
             'width':'100vw'
             }
)
"""
    createTable(value):
        - Takes user input from search bar as a parameter.
        - Makes a callback after each entered character.
        - From input, the table is re-ordered to show search results at the top of table.
        - @return list of tables that will be displayed in the crypto divider: 'crypto-div'.
"""
@app.callback(
    Output(component_id='crypto-div',component_property='children'),
    Input(component_id='token-input',component_property='value'),
)
def createTable(value):
    # index value for newly created data frames
    i = 0
    # data frame that will contains the data from searched input value
    dff = pd.DataFrame(columns=['id',
                                'symbol',
                                'current_price',
                                'high_24h',
                                'low_24h',
                                'price_change_percentage_24h',
                                'market_cap',
                                'image',
                                'price_change_24h',
                                'ath',
                                'total_volume',
                                ]
                       )
    mylist = list()
    if value is None:
        value = ""
    for index,row in df.iterrows():
        if value.upper() in row['id'] or value.upper() in row['symbol']:
            dff.loc[i] = df.loc[index]
            i += 1
    l = [dff,df]
    dff = pd.concat(l)
    dff = dff.drop_duplicates(subset=['symbol'], keep='first')
    for index,row in dff.iterrows():
        #assigning red color to 24hr price change if less than 0, else green
        color_24h = '(255,17,0)' if row['price_change_percentage_24h'] < 0 else '(3, 163, 30)'
        t = html.Tr(
            children=[
                # crypto image
                html.Th(
                    html.Img(src=row['image'],
                             style={'display': 'inline-block',
                                    'height': '3vh',
                                    'width': '3vh',
                                    'margin-left': '20px',
                                    'margin-bottom': '-7px',
                                    'margin-right':'40px',
                                    }
                             ),
                ),
                # crypto name
                html.Th(
                    html.H6(row['id'],
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   'margin-left': '-65px'
                                   }
                            ),
                ),
                # symbol of crypto
                html.Th(
                    html.H6(row['symbol'],
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   'margin-left':'-10px'
                                   }
                            ),
                ),
                # current price
                html.Th(
                    html.H6("${:,.2f}".format(row['current_price']),
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   }
                            ),
                ),
                # 24hr volume for crypto
                html.Th(
                    html.H6("${:,.2f}".format(row['total_volume']),
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   'margin-left': '50px',
                                   }
                            ),
                ),
                # 24hr change in price
                html.Th(
                    html.H6("${:,.4f}".format(row['price_change_24h']),
                            style={'display': 'inline-block',
                                   'color':'rgb'+color_24h,
                                   'font-size': '12px',
                                   'margin-left': '50px',
                                   }
                            ),
                ),
                # 24hr % change in price
                html.Th(
                    html.H6("%{:,.1f}".format(row['price_change_percentage_24h']),
                            style={'display': 'inline-block',
                                   'color': 'rgb'+color_24h,
                                   'font-size': '12px',
                                   'margin-left': '50px',
                                   }
                            ),
                ),
                # 24hr highest price
                html.Th(
                    html.H6("${:,.2f}".format(row['high_24h']),
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   'margin-left': '50px',
                                   }
                            ),
                ),
                # 24hr lowest price
                html.Th(
                    html.H6("${:,.2f}".format(row['low_24h']),
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   'margin-left': '50px',
                                   }
                            ),
                ),
                # all time high
                html.Th(
                    html.H6("${:,.2f}".format(row['ath']),
                            style={'display': 'inline-block',
                                   'font-size': '12px',
                                   'margin-left': '30px',
                                   }
                            ),
                ),
                # market cap
                html.Th(
                    html.H6("${:,}".format(row['market_cap']),
                            style={'display': 'inline-block',
                                   'margin-left': '20px',
                                   'margin-right': '50px',
                                   'font-size': '12px',
                                   }
                            ),
                ),
            ],
        )
        mylist.append(t)
    return mylist

if __name__ == '__main__':
    app.run_server(debug=True)