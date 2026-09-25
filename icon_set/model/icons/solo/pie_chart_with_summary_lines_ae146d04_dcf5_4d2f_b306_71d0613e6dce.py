"""Pie Chart with Text Summary.
Plan: Three-sector pie at left, two short summary rules at right; descriptive marks are not typeface glyphs.
References: supplied source; Lucide original and atomic-debug chart-pie.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'ae146d04-dcf5-4d2f-b306-71d0613e6dce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/text pie_ae146d04-dcf5-4d2f-b306-71d0613e6dce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pie-chart-with-summary-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'pie', 'chart', 'with', 'summary', 'lines')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('chart',(28,24),('A',12,16,True,(16,40)),('A',12,16,True,(4,24)),('A',12,16,True,(16,8)),('A',12,16,True,(28,24)),closed=True)
        poly('sectors',(16,8),(16,24),(28,24))
        line('third',(16,24),(7,35))
        line('summary-top',(37,17),(44,17));line('summary-bottom',(37,31),(44,31))
        contacts(self)
