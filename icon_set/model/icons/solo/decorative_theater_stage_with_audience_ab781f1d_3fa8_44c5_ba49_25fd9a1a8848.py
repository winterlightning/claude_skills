"""Decorative Theater Stage with Audience.

Plan: Decorative necked stage arch over two audience busts. Remove nested doorway and outer facade; reduce three spectators to two. Shared human references: radius 4 heads at y28, shoulders top y40 give exact 8 centerline gap. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab781f1d-3fa8-44c5-ba49-25fd9a1a8848'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/ramlila 1_ab781f1d-3fa8-44c5-ba49-25fd9a1a8848.svg'
AUTHOR = 'gpt-6'

class DecorativeTheaterStageWithAudience(Solo48):
    icon_id = 'decorative-theater-stage-with-audience'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('decorative', 'theater', 'stage', 'with', 'audience')

    def build(self):
        self.add_arc('stage-left',(8,16),(20,8),radius_x=12,radius_y=8)
        self.add_polyline('stage-neck',(20,8),(20,4),(28,4),(28,8))
        self.add_arc('stage-right',(28,8),(40,16),radius_x=12,radius_y=8)
        self.add_contour('stage','stage-left','stage-neck-1','stage-neck-2','stage-neck-3','stage-right')
        self.contours=[c for c in self.contours if c.contour_id!='stage-neck']
        for i,x in enumerate([14,34]):
         self.add_arc(f'head-{i}-r',(x,24),(x,32),radius_x=4)
         self.add_arc(f'head-{i}-l',(x,32),(x,24),radius_x=4)
         self.add_contour(f'head-{i}',f'head-{i}-r',f'head-{i}-l',closed=True)
         self.add_arc(f'shoulder-{i}-l',(x-6,44),(x,40),radius_x=6,radius_y=4)
         self.add_arc(f'shoulder-{i}-r',(x,40),(x+6,44),radius_x=6,radius_y=4)
         self.add_contour(f'shoulders-{i}',f'shoulder-{i}-l',f'shoulder-{i}-r')
