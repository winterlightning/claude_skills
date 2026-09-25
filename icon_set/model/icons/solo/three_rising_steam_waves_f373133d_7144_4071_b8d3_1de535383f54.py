"""Rising Hot Steam Waves.
Plan: Three identical vertical S-curves with a shared 14-unit repeat spacing.
References: supplied source; Lucide original and atomic-debug waves.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'f373133d-7144-4071-b8d3-1de535383f54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/heat waves_f373133d-7144-4071-b8d3-1de535383f54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-rising-steam-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'three', 'rising', 'steam', 'waves')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        for n,x in enumerate((10,24,38)):
         path(f'wave-{n}',(x+4,6),('C',(x-9,18),(x+9,30),(x-4,42)))
        contacts(self)
