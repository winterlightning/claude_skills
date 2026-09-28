"""Six Dots Drag Handle.
Plan: Six round dots, two evenly spaced rows of three; no enclosing border.
References: supplied source; Lucide original and atomic-debug grip.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'b1a71762-cfed-4c31-8dc5-4cfaea8d5909'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark circle_b1a71762-cfed-4c31-8dc5-4cfaea8d5909.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-dot-drag-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'six', 'dot', 'drag', 'handle')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        for row,y in enumerate((8,40)):
         for col,x in enumerate((4,24,44)):self.add_dot(f'dot-{row}-{col}',(x,y))
        contacts(self)
