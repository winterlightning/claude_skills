"""Selection List With Checkmark.
Plan: Two rows of list dots with a large selection tick at the upper right; no enclosing checklist box.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '61d959f7-97b7-46a5-94a0-ea37d640fb9c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark check_61d959f7-97b7-46a5-94a0-ea37d640fb9c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'selection-list-with-checkmark'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'selection', 'list', 'with', 'checkmark')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        for row,y in enumerate((8,40)):
         for col,x in enumerate((4,16,28)):
          if row==0 and col==2:continue
          self.add_dot(f'mark-{row}-{col}',(x,y))
        poly('check',(30,17),(35,22),(44,8))
        self.add_dot('last',(44,40))
        contacts(self)
