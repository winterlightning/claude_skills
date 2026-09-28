"""luggage compartment release: repaired SOLO48 composition.
Plan: Shared body/wheel boundary and matched wheel contours.
Keyshape: HRECT_L matches a broad rear car view.
Reduction: Short bumper ticks omitted. Wheel-top divisions removed; handle opening enlarged.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5f2c92bb-8547-4bda-9a89-b7724021c337'
SOURCE_PATH = 'pictographic-primitives/transportation/luggage compartment release_5f2c92bb-8547-4bda-9a89-b7724021c337.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'car'

class Drawing(Solo48):
    icon_id = 'luggage-compartment-release'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('luggage', 'compartment', 'release')

    def build(self):
        self.add_polyline('car', (6, 32), (4, 32), (4, 22), (12, 8), (36, 8), (44, 22), (44, 32), (42, 32))
        self.add_polyline('underside', (14, 32), (15, 32), (33, 32), (34, 32))
        for (n, x) in [('left', 10), ('right', 38)]:
            self.add_line(n + '-wheel-side', (x - 4, 32), (x - 4, 36))
            self.add_arc(n + '-wheel-round', (x - 4, 36), (x + 4, 36), radius_x=4, sweep=False)
            self.add_line(n + '-wheel-end', (x + 4, 36), (x + 4, 32))
            self.add_contour(n + '-wheel', n + '-wheel-side', n + '-wheel-round', n + '-wheel-end')
            self.relate('connect', n + '-wheel', 'car')
            self.relate('connect', n + '-wheel', 'underside')
        self.add_polyline('luggage', (15, 32), (15, 24), (17, 24), (31, 24), (33, 24), (33, 32))
        self.relate('connect', 'luggage', 'underside')
        self.add_arc('luggage-handle', (17, 24), (31, 24), radius_x=7)
        self.relate('connect', 'luggage-handle', 'luggage')
