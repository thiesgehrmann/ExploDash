import dash_core_components as dcc
import dash_html_components as html


class TabContent(object):
    def __init__(self, dashobj, session, name):
        self._name    = name
        self._session = session

        self.init_callbacks(dashobj)

    #edef

    @property
    def name(self):
        return self._name
    #edef
    

    @property
    def layout(self):
        return self._layout()
    #edef

    def init_callbacks(self, dashobj):
        pass
        #@dashobj.callback
    #edef

    def _layout(self):
        return html.Div(children=html.H1(self.name))
    #edef
#edef
