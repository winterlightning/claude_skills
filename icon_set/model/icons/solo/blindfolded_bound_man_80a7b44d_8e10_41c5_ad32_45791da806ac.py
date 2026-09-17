"""Blindfolded Bound Man.

Symbol plan: Mirror head about x24; circular radius10 head ends y26, shoulders start y34, exact detached ink gap4. Binding width36 and height8. Centerline extremes (6,6)-(42,42).
References: original SOURCE_PATH; Lucide pencil/gavel/hat-glasses for coherent
outlines and shared attachment nodes; human_ref/user.svg for circular heads
and rounded shoulders. Omit tiny decorative face, emblem and robe marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80a7b44d-8e10-41c5-ad32-45791da806ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/kidnapping man_80a7b44d-8e10-41c5-ad32-45791da806ac.svg'
AUTHOR = 'gpt-6'

class BlindfoldedBoundMan(Solo48):
    icon_id = 'blindfolded-bound-man'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('blindfolded', 'bound', 'man')

    def build(self):
        axis, cy, r = 24, 16, 10
        self.add_arc('head-top',(axis-r,cy),(axis+r,cy),radius_x=r)
        self.add_arc('head-bottom',(axis+r,cy),(axis-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('blindfold',(axis-r,cy),(axis+r,cy))
        self.relate('connect','head','blindfold')
        self.add_arc('shoulder-left',(6,42),(16,34),radius_x=10,radius_y=8)
        self.add_line('binding-top-left',(16,34),(26,34))
        self.add_line('binding-top-right',(26,34),(32,34))
        self.add_arc('shoulder-right',(32,34),(42,42),radius_x=10,radius_y=8)
        self.add_line('binding-bottom-right',(42,42),(18,42))
        self.add_line('binding-bottom-left',(18,42),(6,42))
        self.add_contour('binding','shoulder-left','binding-top-left','binding-top-right','shoulder-right','binding-bottom-right','binding-bottom-left',closed=True)
        self.add_line('binding-division',(18,42),(26,34))
        self.relate('connect','binding','binding-division')
