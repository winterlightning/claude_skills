"""Arrow pointing to a dot.
Plan: One southwest-pointing straight arrow and a detached destination dot; deliberate diagonal.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '2e9c1712-6d57-4597-8235-ae8113db02d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark point_2e9c1712-6d57-4597-8235-ae8113db02d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-arrow-pointing-to-dot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'diagonal', 'arrow', 'pointing', 'to', 'dot')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        line('shaft',(42,6),(15,33))
        poly('head',(15,21),(15,33),(27,33))
        self.add_dot('destination',(6,42))
        contacts(self)
