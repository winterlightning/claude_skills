"""Chess Rook.

Plan: Second source rook keeps all three battlements in a broader layout. Each crenellation band is 8 units; Lucide rook informs broad tower and foot. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6827ce25-bda1-54bb-bc4b-11e435eb0b3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess rook_6827ce25-bda1-54bb-bc4b-11e435eb0b3f.svg'
AUTHOR = 'gpt-6'


class ChessRookWideBattlements(Solo48):
    icon_id = 'chess-rook-wide-battlements'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('chess', 'rook')

    def build(self):
        self.add_polyline('tower',(4,8),(12,8),(12,16),(20,16),(20,8),(28,8),(28,16),(36,16),(36,8),(44,8),(44,24),(36,24),(36,32),(40,32))
        self.add_arc('base-r',(40,32),(44,36),radius_x=4)
        self.add_polyline('base',(44,36),(44,40),(4,40),(4,36))
        self.add_arc('base-l',(4,36),(8,32),radius_x=4)
        self.add_polyline('left',(8,32),(12,32),(12,24),(4,24),(4,8))
        self.add_contour('piece',*[f'tower-{i}' for i in range(1,14)],'base-r','base-1','base-2','base-3','base-l','left-1','left-2','left-3','left-4',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['tower','base','left']]
        self.add_line('crown-seam',(12,24),(36,24))
        self.add_line('base-seam',(12,32),(36,32))
        self.relate('connect','piece','crown-seam')
        self.relate('connect','piece','base-seam')
