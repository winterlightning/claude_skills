"""Emergency Medical First Aid Kit.
Plan: Rounded medical case and raised handle; centered medical cross with generous interior spacing.
References: supplied source; Lucide original and atomic-debug briefcase-medical.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '41bb0b4b-dc69-42d5-bf22-17d0a68fea2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit 1_41bb0b4b-dc69-42d5-bf22-17d0a68fea2b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'emergency-medical-first-aid-kit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'emergency', 'medical', 'first', 'aid', 'kit')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        box('case',6,14,42,42,4,xs=(16,32))
        path('handle',(16,14),('L',(16,10)),('A',4,4,True,(20,6)),('L',(28,6)),('A',4,4,True,(32,10)),('L',(32,14)))
        poly('cross-h',(18,28),(24,28),(30,28))
        poly('cross-v',(24,23),(24,28),(24,33))
        contacts(self)
