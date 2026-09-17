"""Person Digging with Shovel.
Plan: Forward-leaning worker grips diagonal shovel; circular head and spread legs preserve digging pose.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '15a300e5-b82d-4912-8a2a-869d03bdf837'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person with a shovel_15a300e5-b82d-4912-8a2a-869d03bdf837.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-digging-with-shovel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/container-components'
    aliases = ()
    keywords = ('sub icon', 'person', 'digging', 'with', 'shovel')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('head',29,11,5)
        self.add_bezier('torso',(29,24),((29,30),(22,34),(16,34)))
        poly('arms',(29,24),(34,30))
        poly('legs',(6,42),(16,34),(22,42))
        poly('shaft',(6,24),(29,24),(34,34))
        poly('spade',(34,34),(40,30),(42,42),(30,40),closed=True)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        contacts(self)
