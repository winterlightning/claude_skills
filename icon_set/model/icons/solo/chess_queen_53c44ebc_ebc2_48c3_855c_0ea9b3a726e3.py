"""Chess Queen.

Plan: Three-point crown, circular finial, tapered stem and broad rounded foot. Shared axis and mirrored points. Lucide queen informs crown. Bounds (8,4)-(40,44); omit narrow collar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53c44ebc-ebc2-48c3-855c-0ea9b3a726e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess queen_53c44ebc-ebc2-48c3-855c-0ea9b3a726e3.svg'
AUTHOR = 'gpt-6'


class ChessQueen(Solo48):
    icon_id = 'chess-queen'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('chess', 'queen')

    def build(self):
        self.add_arc('base-right',(36,36),(40,40),radius_x=4)
        self.add_polyline('base-bottom',(40,40),(40,44),(8,44),(8,40))
        self.add_arc('base-left',(8,40),(12,36),radius_x=4)

        self.add_polyline('crown-stem',(12,36),(18,36),(14,30),(8,18),(16,24),(24,18),(32,24),(40,18),(34,30),(30,36),(36,36))
        self.add_contour('piece','base-right','base-bottom-1','base-bottom-2','base-bottom-3','base-left',*[f'crown-stem-{i}' for i in range(1,11)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['base-bottom','crown-stem']]
        self.add_line('base-seam',(18,36),(30,36))
        self.relate('connect','piece','base-seam')
        self.add_arc('finial-right',(24,10),(24,4),radius_x=3,sweep=False)
        self.add_arc('finial-left',(24,4),(24,10),radius_x=3,sweep=False)
        self.add_contour('finial','finial-right','finial-left',closed=True)
        self.add_line('finial-stem',(24,10),(24,18))
        self.relate('connect','finial','finial-stem')
        self.relate('connect','piece','finial-stem')
