"""Active Sporting Figure.
Plan: A leaning active stick figure; circular head and crossed extended arms. Head follows the vertical tangent of the curved upper torso.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path as _path, ellipse, box as _box, contacts
SOURCE_ICON_ID = '62189f84-b3c6-4b58-ba8a-fae03adee313'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-12/video game wii_62189f84-b3c6-4b58-ba8a-fae03adee313.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'active-sporting-figure'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('sub icon', 'active', 'sporting', 'figure')
    def build(self):
        path = lambda n,p,*cmd,**kw: _path(self,n,p,*cmd,**kw)
        circle = lambda n,x,y,r: ellipse(self,n,x,y,r)
        box = lambda n,l,t,r,b,q=4,**kw: _box(self,n,l,t,r,b,q,**kw)
        line, poly = self.add_line, self.add_polyline
        circle('head',34,11,5)
        self.add_bezier('torso',(34,24),((34,28),(28,32),(24,32)))
        poly('arms',(6,24),(34,24),(42,24))
        poly('legs',(6,42),(24,32),(30,42))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        contacts(self)
