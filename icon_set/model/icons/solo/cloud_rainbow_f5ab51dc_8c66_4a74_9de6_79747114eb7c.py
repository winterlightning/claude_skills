"""A rounded cloud fills the lower-left portion of the image. Three nested rainbow arcs rise from behind its upper edge and sweep toward the upper right.

Reduced rainbow from three arcs to two, retaining cloud endpoints; balanced only for the paired-cloud scene.
Construction reference: Lucide cloud: clean small lobes; concentric rainbow arcs with shared center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5ab51dc-8c66-4a74-9de6-79747114eb7c'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud rainbow_f5ab51dc-8c66-4a74-9de6-79747114eb7c.svg'
AUTHOR = 'gpt-6'

class CloudRainbow(Solo48):
    icon_id = 'cloud-rainbow'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('cloud', 'rainbow', 'sky', 'weather', 'arc', 'sunlight')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-left', (12, 40), (12, 30), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('cloud-crown-left', (12, 30), (20, 24), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-crown-right', (20, 24), (28, 30), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-right', (28, 30), (28, 40), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('cloud-base', (28, 40), (12, 40))
        self.add_contour('cloud', 'cloud-left', 'cloud-crown-left', 'cloud-crown-right', 'cloud-right', 'cloud-base', closed=True)
        self.add_arc('rainbow-outer', (20, 24), (42, 8), radius_x=24, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('rainbow-inner', (28, 30), (42, 18), radius_x=16, radius_y=12, sweep=True, large_arc=False)
        self.relate("connect", 'cloud', 'rainbow-outer')
        self.relate("connect", 'cloud', 'rainbow-inner')
