"""Single Roasted Coffee Bean.
Plan: Oval coffee bean with a long S-shaped seam; mirrored hull and coherent seam.
References: supplied source; Lucide original and atomic-debug coffee.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '49c7ba4a-3465-4f47-bc5e-ebc126adebb0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/coffee bean_49c7ba4a-3465-4f47-bc5e-ebc126adebb0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-roasted-coffee-bean'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'single', 'roasted', 'coffee', 'bean')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        ellipse(self,'bean',24,24,16,20)
        path('seam',(24,4),('C',(35,16),(13,32),(24,44)))
        contacts(self)
