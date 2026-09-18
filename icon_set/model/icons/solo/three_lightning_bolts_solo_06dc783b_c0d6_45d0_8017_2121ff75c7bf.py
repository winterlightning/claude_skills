"""Three Lightning Bolts. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '06dc783b-c0d6-45d0-8017-2121ff75c7bf'
SOURCE_PATH = 'pictographic-primitives/state/thunder heavy_06dc783b-c0d6-45d0-8017-2121ff75c7bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-lightning-bolts-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'three lightning bolts')
    def build(self):
        # Three identical open bolts, 17 units apart and 6 units wide with unequal diagonal slopes.
        for n,x in enumerate((4,21,38)):
            self.add_polyline('bolt-'+str(n),(x+6,8),(x,21),(x+6,25),(x,40))
