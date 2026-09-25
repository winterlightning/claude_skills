"""Downward Trend Arrow.
Plan: Three descending trend segments with arrowhead sharing the endpoint.
References: supplied source; Lucide original and atomic-debug trending-down.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '082bbc6d-66f5-4ed1-9c07-82e626a9bcbb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/downtrend arrow_082bbc6d-66f5-4ed1-9c07-82e626a9bcbb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'downward-trend-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'downward', 'trend', 'arrow')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        poly('trend',(4,8),(17,22),(26,13),(44,40))
        poly('arrowhead',(32,40),(44,40),(44,28))
        contacts(self)
