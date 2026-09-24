"""Smart Car Wi-Fi Connection. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'f59286ba-b86a-4e53-9fe0-93f931efec10'
SOURCE_PATH = 'pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smart-car-wi-fi-connection-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'smart car wi-fi connection')
    def build(self):
        self.add_bezier('outer-wave',(8,10),((13,7),(18,4),(24,4)),((30,4),(35,7),(40,10)))
        self.add_bezier('inner-wave',(17,18),((20,14),(28,14),(31,18)))
        self.add_polyline('roof',(14,34),(18,26),(30,26),(34,34))
        rounded_rect(self,'car',8,34,40,44,4)
        self.relate('connect','roof','car')
