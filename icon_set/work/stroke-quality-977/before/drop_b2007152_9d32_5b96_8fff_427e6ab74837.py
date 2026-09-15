"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2007152-9d32-5b96-8fff-427e6ab74837'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_b2007152-9d32-5b96-8fff-427e6ab74837.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DropB2007152(Solo48):
    icon_id = 'drop-b2007152'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.053, 44), (23.947, 44), (24, 44)))
        self.add_bezier('sym-e1', (24, 44), ((24.106, 44), (23.892, 44), (24, 44)))
        self.add_bezier('sym-e2', (24, 44), ((24.14, 43.991), (24.85, 44), (25, 44)))
        self.add_bezier('sym-e3', (25, 44), ((32.68, 44), (40, 36.982), (40, 30)))
        self.add_bezier('sym-e4', (40, 30), ((40, 29.927), (40, 30.073), (40, 30)))
        self.add_bezier('sym-e5', (40, 30), ((40, 29.782), (40, 29.218), (40, 29)))
        self.add_bezier('sym-e6', (40, 29), ((40, 23.191), (32.83, 14.564), (29, 10)))
        self.add_bezier('sym-e7', (29, 10), ((27.79, 8.555), (26.27, 6.409), (25, 5)))
        self.add_bezier('sym-e8', (25, 5), ((24.922, 4.905), (24.212, 4.227), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((23.788, 4.227), (23.078, 4.905), (23, 5)))
        self.add_bezier('sym-e10', (23, 5), ((21.73, 6.409), (20.21, 8.555), (19, 10)))
        self.add_bezier('sym-e11', (19, 10), ((15.17, 14.564), (8, 23.191), (8, 29)))
        self.add_bezier('sym-e12', (8, 29), ((8, 29.218), (8, 29.782), (8, 30)))
        self.add_bezier('sym-e13', (8, 30), ((8, 30.073), (8, 29.927), (8, 30)))
        self.add_bezier('sym-e14', (8, 30), ((8, 36.982), (15.32, 44), (23, 44)))
        self.add_bezier('sym-e15', (23, 44), ((23.15, 44), (23.86, 43.991), (24, 44)))
        self.add_bezier('sym-e16', (24, 44), ((24.108, 44), (23.894, 44), (24, 44)))
        self.add_bezier('sym-e17', (24, 44), ((24.053, 44), (23.947, 44), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
