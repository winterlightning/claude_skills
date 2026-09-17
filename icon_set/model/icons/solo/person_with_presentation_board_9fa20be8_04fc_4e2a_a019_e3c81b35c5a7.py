"""Person with Presentation Board.
Plan: Presenter bust beside a blank board; person and board retained from the saved standalone scene brief.
References: supplied source; Lucide original and atomic-debug user.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '9fa20be8-04fc-4e2a-a019-e3c81b35c5a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/man square_9fa20be8-04fc-4e2a-a019-e3c81b35c5a7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-presentation-board'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/container-components'
    aliases = ()
    keywords = ('sub icon', 'person', 'with', 'presentation', 'board')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        box('board',4,8,20,22,2)
        circle('head',36,16,5)
        path('shoulders',(28,40),('L',(28,33)),('A',8,8,True,(44,33)),('L',(44,40)))
        self.human_construction = 'bust'
        self.relate('connect','head','shoulders')
        contacts(self)
