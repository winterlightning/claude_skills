"""Swimmer wearing swim cap.
Plan: Capped swimmer bust over water; one head, shoulder curve, and a single wave.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '7572066a-0cea-41fd-ac3e-127debc90712'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/swim compete_7572066a-0cea-41fd-ac3e-127debc90712.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'swimmer-with-cap-and-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('sub icon', 'swimmer', 'with', 'cap', 'and', 'water')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('head',24,15,9)
        line('cap',(15,15),(33,15))
        path('shoulders',(14,32),('A',10,4,True,(24,28)),('A',10,4,True,(34,32)))
        path('water',(6,42),('C',(12,42),(12,40),(18,40)),('C',(24,40),(24,42),(30,42)),('C',(36,42),(36,40),(42,40)))
        self.human_construction='bust'
        self.relate('connect','head','shoulders')
        contacts(self)
