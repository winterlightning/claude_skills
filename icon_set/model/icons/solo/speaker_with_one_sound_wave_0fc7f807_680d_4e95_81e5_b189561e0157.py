"""Low Volume Speaker.
Plan: Speaker horn and one detached circular sound arc; no extra outer wave.
References: supplied source; Lucide original and atomic-debug volume-1.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '0fc7f807-680d-4e95-81e5-b189561e0157'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/volume 1_0fc7f807-680d-4e95-81e5-b189561e0157.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'speaker-with-one-sound-wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'speaker', 'with', 'one', 'sound', 'wave')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        poly('speaker',(4,18),(12,18),(26,8),(26,40),(12,30),(4,30),closed=True)
        path('wave',(36,12),('A',8,12,True,(36,36)))
        contacts(self)
