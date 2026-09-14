# Variant of bell-shaped-stupa-v2; parent file remains unchanged.
"""Bell dome, needle finial and broad plinth. Lucide bell informs the coherent dome; stepped bands reduced to one base."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b5808a21-bbc2-446a-bbcd-10a59aa224ac'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/wat phra kaew_b5808a21-bbc2-446a-bbcd-10a59aa224ac.svg'
AUTHOR = 'gpt-6'

class BellShapedStupaVariant3(Solo48):
    icon_id = 'bell-shaped-stupa-v3'
    variant_of = 'bell-shaped-stupa-v2'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('wat phra kaew', 'stupa', 'chedi', 'thailand', 'temple', 'buddhist', 'landmark', 'religion')

    def build(self) -> None:
        self.add_polyline('spire', (17, 16), (24, 6), (31, 16), closed=True)
        self.add_line('dome-top', (17, 16), (31, 16))
        self.add_arc('dome-right', (31, 16), (39, 38), radius_x=8, radius_y=22)
        self.add_line('dome-base', (39, 38), (9, 38))
        self.add_arc('dome-left', (9, 38), (17, 16), radius_x=8, radius_y=22)
        self.add_contour('dome', 'dome-top', 'dome-right', 'dome-base', 'dome-left', closed=True)
        self.relate('connect', 'spire', 'dome')
        self.add_polyline('plinth', (9, 38), (6, 38), (6, 42), (42, 42), (42, 38), (39, 38))
        self.relate('connect', 'plinth', 'dome')
