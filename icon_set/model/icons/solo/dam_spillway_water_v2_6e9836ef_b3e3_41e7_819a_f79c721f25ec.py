# Variant of dam-spillway-water; parent file remains unchanged.
'Three falling streams. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6e9836ef-b3e3-41e7-819a-f79c721f25ec'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/renewable energy water dam_6e9836ef-b3e3-41e7-819a-f79c721f25ec.svg'
AUTHOR = 'gpt-6'

class DamSpillwayWaterVariant2(Solo48):
    icon_id = 'dam-spillway-water-v2'
    variant_of = 'dam-spillway-water'
    variant_label = 'Three falling streams'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'spillway', 'water', 'hydro', 'energy', 'flow', 'waterfall', 'renewable', 'power')

    def build(self) -> None:
        for i, x in enumerate((7, 22, 37)):
            self.add_line(f'fall-{i}', (x, 5), (x, 25))
            self.add_arc(f'foot-{i}', (x, 25), (x + 5, 30), radius_x=5, sweep=False)
            self.add_contour(f'stream-{i}', f'fall-{i}', f'foot-{i}')
        self.add_arc('water-left', (2, 40), (24, 40), radius_x=11, radius_y=3, sweep=False)
        self.add_arc('water-right', (24, 40), (46, 40), radius_x=11, radius_y=3, sweep=False)
        self.add_contour('water', 'water-left', 'water-right')
