"""Front View Ceramic Bathroom Toilet.
Plan: Front-view cistern above a broad bowl and tapered pedestal; shared bowl rim.
References: supplied source; Lucide original and atomic-debug toilet.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '4b4b156b-56c7-45c1-80c4-fb442761ed90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/toilet_4b4b156b-56c7-45c1-80c4-fb442761ed90.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-view-bathroom-toilet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'front', 'view', 'bathroom', 'toilet')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        poly('tank',(14,24),(12,4),(36,4),(34,24))
        path('bowl',(8,24),('L',(40,24)),('C',(40,33),(34,34),(32,36)),('L',(35,44)),('L',(13,44)),('L',(16,36)),('C',(14,34),(8,33),(8,24)),closed=True)
        contacts(self)
