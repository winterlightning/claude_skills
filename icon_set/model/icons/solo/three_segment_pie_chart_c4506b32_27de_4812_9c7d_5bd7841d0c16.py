"""Three Segment Pie Chart.
Plan: Circle divided into three unequal sectors by up, right, and lower-left spokes.
References: supplied source; Lucide original and atomic-debug chart-pie.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'c4506b32-27de-4812-9c7d-5bd7841d0c16'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pie chart_c4506b32-27de-4812-9c7d-5bd7841d0c16.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-segment-pie-chart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'three', 'segment', 'pie', 'chart')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('pie',(24,4),('A',20,20,True,(44,24)),('A',20,20,True,(24,44)),('A',20,20,True,(12,40)),('A',20,20,True,(4,24)),('A',20,20,True,(24,4)),closed=True)
        poly('upper',(24,4),(24,24),(44,24))
        line('lower',(24,24),(12,40))
        contacts(self)
