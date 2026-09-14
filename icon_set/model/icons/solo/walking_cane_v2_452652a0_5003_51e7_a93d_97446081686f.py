# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '452652a0-5003-51e7-a93d-97446081686f'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/cane_452652a0-5003-51e7-a93d-97446081686f.svg'
AUTHOR = 'gpt-6'

class WalkingCaneVariant2(Solo48):
    icon_id = 'walking-cane-v2'
    variant_of = 'walking-cane'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('cane', 'walking stick', 'crook', 'stick', 'handle', 'accessory', 'mobility', 'hook')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Tilt the shaft while keeping a compact hook.
        # Circular crown, short tangent bend, then a straight shaft on a 3:2 slope.
        self.add_arc('hook',(22,16),(42,16),radius_x=10)
        self.add_bezier('bend',(42,16),((42,18),(39,20),(36,22)))
        self.add_line('shaft',(36,22),(6,42))
        self.add_contour('cane','hook','bend','shaft')
