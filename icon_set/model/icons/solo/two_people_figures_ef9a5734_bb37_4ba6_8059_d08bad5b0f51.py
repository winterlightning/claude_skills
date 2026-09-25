"""Two People Figures.
Plan: Two equal outlined heads and open shoulder arches, horizontally repeated without merging bodies.
References: supplied source; Lucide original and atomic-debug users.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'ef9a5734-bb37-4ba6-8059-d08bad5b0f51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-people-figures'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'two', 'people', 'figures')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        for n,cx in enumerate((12,36)):
         circle(f'head-{n}',cx,14,4)
         path(f'body-{n}',(cx-8,38),('L',(cx-8,30)),('A',8,8,True,(cx+8,30)),('L',(cx+8,38)))
         self.relate('connect',f'head-{n}',f'body-{n}')
        self.human_construction='bust'
        contacts(self)
