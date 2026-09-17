"""Chess Pawn.

Plan: Round-headed pawn with continuous flared neck and one rounded base tier. Lucide pawn informs spherical head and broad foot. Bounds (8,4)-(40,44). Drop doubled tier.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31076e3c-9bbc-45dd-abb5-872398985d57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess pawn 1_31076e3c-9bbc-45dd-abb5-872398985d57.svg'
AUTHOR = 'gpt-6'


class ChessPawnReference(Solo48):
    icon_id = 'chess-pawn-reference'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('chess', 'pawn')

    def build(self):
        self.add_arc('base-right',(36,36),(40,40),radius_x=4)
        self.add_polyline('base-bottom',(40,40),(40,44),(8,44),(8,40))
        self.add_arc('base-left',(8,40),(12,36),radius_x=4)

        self.add_line('shoulder-left',(12,36),(16,36))
        self.add_polyline('stem-left',(16,36),(20,28),(18,22))
        self.add_arc('head',(18,22),(30,22),radius_x=10,large_arc=True)
        self.add_polyline('stem-right',(30,22),(28,28),(32,36),(36,36))
        self.add_contour('piece','base-right','base-bottom-1','base-bottom-2','base-bottom-3','base-left','shoulder-left','stem-left-1','stem-left-2','head','stem-right-1','stem-right-2','stem-right-3',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['base-bottom','stem-left','stem-right']]
        self.add_line('base-seam',(16,36),(32,36))
        self.relate('connect','piece','base-seam')
