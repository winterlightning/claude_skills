"""Close and Cancel Symbol.
Plan: Two diagonal strokes cross at the shared center.
References: supplied source; Lucide original and atomic-debug x.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'a24ed7fe-9b46-4add-a846-a94fecd03d7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/xmark_a24ed7fe-9b46-4add-a846-a94fecd03d7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'close-and-cancel-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/container-components'
    aliases = ()
    keywords = ('sub icon', 'close', 'and', 'cancel', 'symbol')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        poly('falling',(6,6),(24,24),(42,42))
        poly('rising',(6,42),(24,24),(42,6))
        contacts(self)
