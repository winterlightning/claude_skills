# Variant of grand-canyon-with-river; parent file remains unchanged.
'Simpler canyon and river. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '021a0b5f-bd2d-4f08-b36b-7afe509eb0fc'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa 1_021a0b5f-bd2d-4f08-b36b-7afe509eb0fc.svg'
AUTHOR = 'gpt-6'

class GrandCanyonWithRiverVariant2(Solo48):
    icon_id = 'grand-canyon-with-river-v2'
    variant_of = 'grand-canyon-with-river'
    variant_label = 'Simpler canyon and river'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('grand canyon', 'canyon', 'usa', 'arizona', 'river', 'cliff', 'landscape', 'nature', 'landmark')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46); asymmetric mesas frame the river.
        self.add_polyline('left-cliff',(2,2),(13,2),(16,13),(11,13),(8,29),(2,33))
        self.add_polyline('right-cliff',(46,7),(35,7),(32,19),(37,19),(40,34),(46,38))
        self.add_arc('river-upper',(25,18),(17,32),radius_x=8,radius_y=14,sweep=False)
        self.add_arc('river-lower',(17,32),(9,46),radius_x=8,radius_y=14,sweep=True)
        self.add_contour('river','river-upper','river-lower')
