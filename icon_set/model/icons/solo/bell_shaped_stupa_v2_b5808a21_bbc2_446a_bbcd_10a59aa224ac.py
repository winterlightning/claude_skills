# Variant of bell-shaped-stupa; parent file remains unchanged.
"""Bell dome, needle finial and broad plinth. Lucide bell informs the coherent dome; stepped bands reduced to one base."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b5808a21-bbc2-446a-bbcd-10a59aa224ac'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/wat phra kaew_b5808a21-bbc2-446a-bbcd-10a59aa224ac.svg'
AUTHOR = 'gpt-6'

class BellShapedStupaVariant2(Solo48):
    icon_id = 'bell-shaped-stupa-v2'
    variant_of = 'bell-shaped-stupa'
    variant_label = 'Not like the concept name'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('wat phra kaew', 'stupa', 'chedi', 'thailand', 'temple', 'buddhist', 'landmark', 'religion')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46): tapered spire, bell and joined plinth.
        self.add_polyline('spire', (17,16), (24,2), (31,16), closed=True)
        self.add_line('dome-top', (17,16), (31,16))
        self.add_arc('dome-right', (31,16), (39,38), radius_x=8, radius_y=22)
        self.add_line('dome-base', (39,38), (9,38))
        self.add_arc('dome-left', (9,38), (17,16), radius_x=8, radius_y=22)
        self.add_contour('dome', 'dome-top', 'dome-right', 'dome-base', 'dome-left', closed=True)
        self.relate('connect', 'spire', 'dome')
        self.add_polyline('plinth', (9,38), (5,38), (5,46), (43,46), (43,38), (39,38))
        self.relate('connect', 'plinth', 'dome')
