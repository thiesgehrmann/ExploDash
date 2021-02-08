from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from flask import current_app as app
from flask import session

from . import tabs


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(server=server,
                    routes_pathname_prefix='/explodash/',
                    external_stylesheets=['/static/css/main.css']
                    )


    # Create Dash Layout
    header = create_header_layout()
    body   = create_body_layout(dash_app)
    footer = create_footer_layout()

    dash_app.layout = html.Div(id='dash-container', children=[header, body, footer])

    return dash_app.server
#edef

def create_header_layout():
    return html.Div(children=[
        html.H1("ExploDash")])
#edef

def create_footer_layout():
    return html.Div(id='footer', children=[html.Hr(), html.A(href="/logout", children=["Logout"])])
#edef

def create_body_layout(dash_app):
    T = [ tab(dash_app, session) for tab in tabs.registered ]
    return html.Div([
            dcc.Tabs(id='tab_frame', value='tab-1', children=[
                dcc.Tab(id='tab-%d' % i, label=tab.name, children=tab._layout()) for i,tab in enumerate(T)
            ]) 
        ])


def init_callbacks(dash_app):
    pass
#edef
