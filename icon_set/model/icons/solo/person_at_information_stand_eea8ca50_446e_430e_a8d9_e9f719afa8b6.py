"""Person Looking at Information Stand.
Plan: Standing reader beside a small sign on a tall post; bent arm points toward sign.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = 'eea8ca50-446e-430e-a8d9-e9f719afa8b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/watcher_eea8ca50-446e-430e-a8d9-e9f719afa8b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-at-information-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'person', 'at', 'information', 'stand')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        box('sign',6,6,18,16,2,xs=(12,))
        line('post',(12,16),(12,42))
        circle('head',36,10,4)
        line('torso',(36,22),(36,32))
        poly('arm',(36,22),(28,27),(24,22))
        poly('legs',(27,42),(36,32),(42,42))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        contacts(self)
