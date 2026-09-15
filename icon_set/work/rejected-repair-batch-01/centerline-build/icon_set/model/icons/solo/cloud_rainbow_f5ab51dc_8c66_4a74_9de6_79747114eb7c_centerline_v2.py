"""Open the gap between the two rainbow curves by lifting the outer arch; keep each arc attached to the cloud and preserve its clean quarter-ellipse construction.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5ab51dc-8c66-4a74-9de6-79747114eb7c'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud rainbow_f5ab51dc-8c66-4a74-9de6-79747114eb7c.svg'
AUTHOR = 'gpt-6'

class CloudRainbow(Solo48):
    icon_id = 'cloud-rainbow-centerline-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('cloud', 'rainbow', 'sky', 'weather', 'arc', 'sunlight')

    def build(self) -> None:
        self.add_arc('cloud-left', (12, 40), (12, 30), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('cloud-crown-left', (12, 30), (20, 24), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-crown-right', (20, 24), (28, 30), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-right', (28, 30), (28, 40), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('cloud-base', (28, 40), (12, 40))
        self.add_contour('cloud', 'cloud-left', 'cloud-crown-left', 'cloud-crown-right', 'cloud-right', 'cloud-base', closed=True)
        self.add_arc('rainbow-outer', (20, 24), (44, 8), radius_x=24, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('rainbow-inner', (28, 30), (44, 20), radius_x=16, radius_y=10, sweep=True, large_arc=False)
        self.relate('connect', 'cloud', 'rainbow-outer')
        self.relate('connect', 'cloud', 'rainbow-inner')
    variant_of = 'cloud-rainbow'
    variant_label = 'Batch 01 centerline repair'
