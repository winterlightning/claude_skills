"""Apple vision pro space volume (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3d52a574-2cf8-4bbf-95ef-7eaebf475a4e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/apple vision pro space volume_3d52a574-2cf8-4bbf-95ef-7eaebf475a4e.svg'
AUTHOR = 'gpt-6'

class AppleVisionProSpaceVolume(Solo48):
    icon_id = 'apple-vision-pro-space-volume'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('apple', 'vision', 'pro', 'space', 'volume', '_uncategorized_03')

    def build(self):
        self.add_line('sym-e0', (39, 8), (8, 8))
        self.add_arc('sym-e3', (8, 8), (7, 9), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e4-1', (7, 9), (5, 12))
        self.add_arc('sym-e4-2', (5, 12), (4, 17), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('sym-e5', (4, 17), (4, 25))
        self.add_line('sym-e10-1', (4, 25), (6, 35))
        self.add_arc('sym-e10-2', (6, 35), (11, 40), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e11', (11, 40), (13, 40))
        self.add_arc('sym-e12-1', (13, 40), (14, 40), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_arc('sym-e12-2', (14, 40), (15, 40), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_arc('sym-e14', (15, 40), (19, 38), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e15', (19, 38), (24, 34), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('sym-e16', (24, 34), (29, 38), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('sym-e17', (29, 38), (33, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e19-1', (33, 40), (37, 40))
        self.add_arc('sym-e21-1', (37, 40), (42, 35), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e21-2', (42, 35), (44, 25))
        self.add_line('sym-e23', (44, 25), (44, 17))
        self.add_arc('sym-e27-1', (44, 17), (43, 12), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('sym-e27-2', (43, 12), (41, 9))
        self.add_arc('sym-e28', (41, 9), (40, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e29', (40, 8), (39, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19-1', 'sym-e21-1', 'sym-e21-2', 'sym-e23', 'sym-e27-1', 'sym-e27-2', 'sym-e28', 'sym-e29', closed=True)
