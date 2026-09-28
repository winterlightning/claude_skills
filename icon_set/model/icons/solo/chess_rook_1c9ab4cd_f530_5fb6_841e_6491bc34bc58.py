"""Chess Rook.

Plan: Tall rook with two broad battlements and one notch, taper and rounded base. Lucide rook informs tower silhouette. Three source battlements reduced to two. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c9ab4cd-f530-5fb6-841e-6491bc34bc58'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess rook_1c9ab4cd-f530-5fb6-841e-6491bc34bc58.svg'
AUTHOR = 'gpt-6'


class ChessRook(Solo48):
    icon_id = 'chess-rook'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('chess', 'rook')

    def build(self):
        self.add_arc('base-right',(36,36),(40,40),radius_x=4)
        self.add_polyline('base-bottom',(40,40),(40,44),(8,44),(8,40))
        self.add_arc('base-left',(8,40),(12,36),radius_x=4)

        self.add_polyline('tower',(12,36),(14,20),(8,20),(8,4),(20,4),(20,12),(28,12),(28,4),(40,4),(40,20),(34,20),(36,36))
        self.add_contour('piece','base-right','base-bottom-1','base-bottom-2','base-bottom-3','base-left',*[f'tower-{i}' for i in range(1,12)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['base-bottom','tower']]
        self.add_line('crown-seam',(14,20),(34,20))
        self.add_line('base-seam',(12,36),(36,36))
        self.relate('connect','piece','crown-seam')
        self.relate('connect','piece','base-seam')
