"""Frozen regression: the original airmail defect, independent of editable icons."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '055d9bbb-508e-4991-84fd-c6c91f3a1a47'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/airmail_055d9bbb-508e-4991-84fd-c6c91f3a1a47.svg'
AUTHOR = 'gpt-6'

class AsymmetricAirmail(Solo48):
    icon_id = 'airmail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('airmail', '_uncategorized_01')

    def build(self):
        self.add_line('sym-e0', (44, 39), (41, 40))
        self.add_line('sym-e1', (41, 40), (7, 40))
        self.add_line('sym-e2', (7, 40), (4, 39))
        self.add_line('sym-e3', (4, 39), (4, 10))
        self.add_line('sym-e5', (4, 10), (19, 24))
        self.add_line('sym-e6', (19, 24), (23, 27))
        self.add_arc('sym-e7', (23, 27), (24, 27), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e8', (24, 27), (25, 27), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e9', (25, 27), (29, 24))
        self.add_line('sym-e10', (29, 24), (44, 10))
        self.add_line('sym-e11', (44, 10), (44, 37))
        self.add_arc('sym-e12-1', (44, 37), (44, 38), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_arc('sym-e12-2', (44, 38), (44, 39), radius_x=39, radius_y=39, large_arc=False, sweep=False)
        self.add_line('sym-e13', (44, 39), (29, 24))
        self.add_line('sym-e14', (4, 10), (6, 8))
        self.add_line('sym-e15', (6, 8), (42, 8))
        self.add_line('sym-e19', (42, 8), (44, 10))
        self.add_line('sym-e20', (19, 24), (4, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13', closed=False)
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e19', closed=False)
        self.add_contour('sym-c2', 'sym-e20', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
