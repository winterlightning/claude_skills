"""Two dam piers flank a spillway face and water; one wave retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6411cee5-9e14-533a-9adf-d5bcd2213734'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_6411cee5-9e14-533a-9adf-d5bcd2213734.svg'
AUTHOR = 'gpt-6'

class HydroelectricDam(Solo48):
    icon_id = 'hydroelectric-dam'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'hydroelectric', 'water', 'reservoir', 'spillway', 'power', 'energy', 'infrastructure')

    def build(self) -> None:
        # HRECT_XL centerline extremes (2,5)-(46,43).
        self.add_polyline('left-pier', (2, 33), (5, 5), (13, 5), (13, 13), (10, 33))
        self.add_polyline('right-pier', (36, 33), (39, 13), (39, 5), (46, 5), (46, 33))
        self.add_line('crest', (13, 13), (39, 13))
        self.relate('connect', 'crest', 'left-pier')
        self.relate('connect', 'crest', 'right-pier')
        self.add_line('flow-left', (22, 22), (20, 31))
        self.add_line('flow-right', (30, 22), (28, 31))
        self.add_arc('wave-left', (2, 40), (24, 40), radius_x=11, radius_y=3, sweep=False)
        self.add_arc('wave-right', (24, 40), (46, 40), radius_x=11, radius_y=3, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right')
