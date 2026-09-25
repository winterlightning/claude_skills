"""Digital Facial Recognition Scan.
Plan: Symmetric face outline, scan cross through upper face, and curved smile. The cross is the scan detail.
References: supplied source; Lucide original and atomic-debug scan-face.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'e8d4be3d-150f-41a6-9d1a-bc26830066af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/deepfake_e8d4be3d-150f-41a6-9d1a-bc26830066af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'digital-facial-recognition'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'digital', 'facial', 'recognition')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        path('face',(8,20),('A',16,16,True,(40,20)),('L',(40,28)),('A',16,16,True,(8,28)),('L',(8,20)),closed=True)
        line('scan-horizontal',(8,20),(40,20))
        line('scan-vertical',(24,4),(24,24))
        path('smile',(19,32),('C',(22,35),(26,35),(29,32)))
        contacts(self)
