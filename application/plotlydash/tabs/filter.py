from .tabcontent import TabContent
import dash_core_components as dcc
import dash_html_components as html


class Filter(TabContent):
    def __init__(self, dashobj, session):
        super().__init__(dashobj, session, "Filter")

    #edef

    def _layout(self):
        return ["TEST"]
    #edef
#edef