"""Chess Bishop.

Plan: Pointed bulbous bishop head flows through a narrow neck into a flared pedestal. Lucide bishop informs pointed head; omit tiny finial. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4020213e-b2a5-5ea0-a2b2-78847651ebd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess bishop_4020213e-b2a5-5ea0-a2b2-78847651ebd5.svg'
AUTHOR = 'gpt-6'


class ChessBishop(Solo48):
    icon_id = 'chess-bishop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('chess', 'bishop')

    def build(self):
        self.add_arc('base-right',(36,36),(40,40),radius_x=4)
        self.add_polyline('base-bottom',(40,40),(40,44),(8,44),(8,40))
        self.add_arc('base-left',(8,40),(12,36),radius_x=4)

        self.add_polyline('stem-left',(12,36),(16,36),(20,28),(20,26))
        self.add_arc('head-left-lower',(20,26),(14,18),radius_x=6,radius_y=8)
        self.add_arc('head-left-upper',(14,18),(24,4),radius_x=10,radius_y=14)
        self.add_arc('head-right-upper',(24,4),(34,18),radius_x=10,radius_y=14)
        self.add_arc('head-right-lower',(34,18),(28,26),radius_x=6,radius_y=8)
        self.add_polyline('stem-right',(28,26),(28,28),(32,36),(36,36))
        self.add_contour('piece','base-right','base-bottom-1','base-bottom-2','base-bottom-3','base-left','stem-left-1','stem-left-2','stem-left-3','head-left-lower','head-left-upper','head-right-upper','head-right-lower','stem-right-1','stem-right-2','stem-right-3',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['base-bottom','stem-left','stem-right']]
        self.add_line('base-seam',(16,36),(32,36))
        self.relate('connect','piece','base-seam')
