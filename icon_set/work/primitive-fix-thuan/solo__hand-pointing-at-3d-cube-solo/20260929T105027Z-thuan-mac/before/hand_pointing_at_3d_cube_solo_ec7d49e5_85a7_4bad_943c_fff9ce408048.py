"""Hand Pointing at 3D Cube. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ec7d49e5-85a7-4bad-943c-fff9ce408048'
SOURCE_PATH = 'pictographic-primitives/state/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pointing-at-3d-cube-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('sub icon', 'hand pointing at 3d cube')
    def build(self):
        # Cube occupies the upper right; pointing hand remains below-left.
        self.add_polyline('cube-outline',(24,11),(33,6),(42,11),(42,22),(33,27),(24,22),closed=True)
        self.add_polyline('cube-ridge',(24,11),(33,16),(42,11))
        self.add_line('cube-vertical',(33,16),(33,27))
        self.relate('connect','cube-outline','cube-ridge','cube-vertical')
        self.add_bezier('thumb',(6,36),((6,32),(10,32),(10,36)))
        self.add_line('finger-left',(10,36),(10,29))
        self.add_arc('fingertip',(10,29),(18,29),radius_x=4)
        self.add_polyline('palm',(18,29),(18,38),(24,40),(24,42))
        self.relate('connect','thumb','finger-left')
        self.relate('connect','finger-left','fingertip')
        self.relate('connect','fingertip','palm')
