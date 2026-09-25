"""A sweeping arrow curves from lower left into an upright tip at upper right. Square 6..42 fits the sweep. Source supplies direction and large open head; Lucide corner-down-right teaches tangent arc-to-line shaft. Mirror 10-unit head arms about x32; no omitted identity features."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'a172051c-eb5c-49c5-b43c-cc6cfed28d0b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram up large head_a172051c-eb5c-49c5-b43c-cc6cfed28d0b.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'arrow-sweeping-up-from-lower-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Arrow Sweeping Up from Lower Left']
    keywords = ['arrow', 'up', 'curve', 'sweep', 'direction', 'pointer', 'bend']
    def build(self):
        self.add_arc('sweep',(6,42),(32,16),radius_x=26,sweep=False)
        self.add_line('end',(32,16),(32,6))
        self.add_contour('shaft','sweep','end')
        self.add_polyline('head',(22,16),(32,6),(42,16))
        self.relate('connect','shaft','head')
