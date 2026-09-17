"""Chess Knight and Pawn.

Plan: Left-facing knight beside smaller round pawn. Lucide knight and pawn inform profiles; reduce eye and pawn body to essential strokes. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8184764-3245-40c1-a10d-883944a9fe13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess_e8184764-3245-40c1-a10d-883944a9fe13.svg'
AUTHOR = 'gpt-6'


class ChessKnightAndPawn(Solo48):
    icon_id = 'chess-knight-and-pawn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('chess', 'knight', 'and', 'pawn')

    def build(self):
        self.add_polyline('knight-front',(4,40),(4,32),(8,32),(16,24),(4,24),(12,14),(12,8))
        self.add_arc('knight-mane',(12,8),(24,20),radius_x=12)
        self.add_polyline('knight-back',(24,20),(24,32),(24,40),(4,40))
        self.add_contour('knight',*[f'knight-front-{i}' for i in range(1,7)],'knight-mane','knight-back-1','knight-back-2','knight-back-3',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['knight-front','knight-back']]
        self.add_line('knight-base',(8,32),(24,32))
        self.relate('connect','knight','knight-base')
        self.add_arc('pawn-head-r',(38,28),(38,16),radius_x=6,sweep=False)
        self.add_arc('pawn-head-l',(38,16),(38,28),radius_x=6,sweep=False)
        self.add_contour('pawn-head','pawn-head-r','pawn-head-l',closed=True)
        self.add_line('pawn-stem',(38,28),(38,40))
        self.add_polyline('pawn-base',(32,40),(38,40),(44,40))
        self.relate('connect','pawn-head','pawn-stem')
        self.relate('connect','pawn-stem','pawn-base')
