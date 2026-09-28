"""Left Aligned Paragraph Text.
Plan: Three evenly spaced horizontal lines share left alignment and alternate length.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'b84c42e8-662b-41fd-bb1e-bb264e55ee35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three lines_b84c42e8-662b-41fd-bb1e-bb264e55ee35.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-left-aligned-text-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'three', 'left', 'aligned', 'text', 'lines')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        for n,y,end in [('top',8,44),('middle',24,33),('bottom',40,44)]:line(n,(4,y),(end,y))
        contacts(self)
