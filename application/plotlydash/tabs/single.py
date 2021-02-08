from .tabcontent import TabContent
import dash_core_components as dcc
import dash_html_components as html

class Single(TabContent):
    def __init__(self, dashobj, session):
        super().__init__(dashobj, session, "Single")
        print("Initializing with dropdown")
    #edef

    def _layout(self):
        return [ html.Div(id='single_select', children=
                 [html.Div(children=[
                            dcc.Dropdown(
                                id='single-selection',
                                options=[{"label":"Nothing yet", "value":None}],
                                value=None),
                            ]),
                html.Hr(),
                html.Div(id='single_output', children=["No column has been selected yet"])
                ])]
    #edef
#eclass