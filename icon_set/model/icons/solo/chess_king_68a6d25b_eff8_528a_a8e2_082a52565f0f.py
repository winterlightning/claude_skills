"""Chess King.

Plan: Cross atop tapered broad king crown, with one rounded base. Lucide king informs crown and cross; remove collar tier. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68a6d25b-eff8-528a-a8e2-082a52565f0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess king_68a6d25b-eff8-528a-a8e2-082a52565f0f.svg'
AUTHOR = 'gpt-6'


class ChessKing(Solo48):
    icon_id = 'chess-king'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('chess', 'king')

    def build(self):
        self.add_arc('base-right',(36,36),(40,40),radius_x=4)
        self.add_polyline('base-bottom',(40,40),(40,44),(8,44),(8,40))
        self.add_arc('base-left',(8,40),(12,36),radius_x=4)

        self.add_line('left-foot',(12,36),(18,36))
        self.add_line('crown-left',(18,36),(12,24))
        self.add_arc('crown-tl',(12,24),(16,20),radius_x=4)
        self.add_polyline('crown-top',(16,20),(24,20),(32,20))
        self.add_arc('crown-tr',(32,20),(36,24),radius_x=4)
        self.add_polyline('crown-right',(36,24),(30,36),(36,36))
        self.add_contour('piece','base-right','base-bottom-1','base-bottom-2','base-bottom-3','base-left','left-foot','crown-left','crown-tl','crown-top-1','crown-top-2','crown-tr','crown-right-1','crown-right-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['base-bottom','crown-top','crown-right']]
        self.add_line('base-seam',(18,36),(30,36))
        self.relate('connect','base-seam','piece')
        self.add_polyline('cross-upright',(24,4),(24,10),(24,20))
        self.add_polyline('cross-bar',(18,10),(24,10),(30,10))
        self.relate('connect','cross-upright','cross-bar')
        self.relate('connect','cross-upright','piece')
