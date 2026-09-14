"""Massage pillow (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91f652e5-405c-55eb-a732-b57512c93cdb'
SOURCE_PATH = 'icons-json/health/massage pillow_91f652e5-405c-55eb-a732-b57512c93cdb.json'
AUTHOR = 'gpt-6'

class MassagePillow(Solo48):
    icon_id = 'massage-pillow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('massage', 'pillow', 'health')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (31, 17), (34, 24), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (34, 24), (31, 31), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (17, 17), (14, 24), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (14, 24), (17, 31), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e4', (39, 39), (37, 39))
        self.add_arc('sym-e5', (37, 39), (34, 39), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e6', (34, 39), (29, 40))
        self.add_line('sym-e7', (29, 40), (24, 40))
        self.add_arc('sym-e8', (24, 40), (19, 40), radius_x=61, radius_y=61, large_arc=False, sweep=False)
        self.add_arc('sym-e9', (19, 40), (14, 39), radius_x=36, radius_y=36, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (14, 39), (11, 39), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e11', (11, 39), (9, 39))
        self.add_arc('sym-e12-1', (9, 39), (6, 40), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e12-2', (6, 40), (5, 39), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('sym-e13', (5, 39), (4, 38), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e15', (4, 38), (4, 37))
        self.add_line('sym-e16', (4, 37), (5, 34))
        self.add_arc('sym-e17', (5, 34), (5, 31), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('sym-e18', (5, 31), (4, 24))
        self.add_line('sym-e21', (4, 24), (5, 17))
        self.add_arc('sym-e22', (5, 17), (5, 14), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('sym-e23', (5, 14), (4, 11))
        self.add_line('sym-e24', (4, 11), (4, 10))
        self.add_line('sym-e26', (4, 10), (5, 9))
        self.add_arc('sym-e27-1', (5, 9), (6, 8), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('sym-e27-2', (6, 8), (9, 9), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e28', (9, 9), (11, 9), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('sym-e29', (11, 9), (14, 9), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('sym-e30', (14, 9), (19, 8), radius_x=35, radius_y=35, large_arc=False, sweep=False)
        self.add_arc('sym-e31', (19, 8), (24, 8), radius_x=61, radius_y=61, large_arc=False, sweep=False)
        self.add_line('sym-e32', (24, 8), (29, 8))
        self.add_arc('sym-e33', (29, 8), (34, 9), radius_x=35, radius_y=35, large_arc=False, sweep=False)
        self.add_arc('sym-e34', (34, 9), (37, 9), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('sym-e35', (37, 9), (39, 9), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('sym-e36-1', (39, 9), (42, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e36-2', (42, 8), (43, 9), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e37', (43, 9), (44, 10))
        self.add_arc('sym-e39', (44, 10), (44, 11), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e40', (44, 11), (43, 14))
        self.add_line('sym-e41', (43, 14), (43, 17))
        self.add_arc('sym-e42', (43, 17), (44, 24), radius_x=41, radius_y=41, large_arc=False, sweep=True)
        self.add_arc('sym-e45', (44, 24), (43, 31), radius_x=41, radius_y=41, large_arc=False, sweep=True)
        self.add_line('sym-e46', (43, 31), (43, 34))
        self.add_line('sym-e47', (43, 34), (44, 37))
        self.add_line('sym-e48', (44, 37), (44, 38))
        self.add_line('sym-e50', (44, 38), (43, 39))
        self.add_arc('sym-e51-1', (43, 39), (42, 40), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e51-2', (42, 40), (39, 39))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=False)
        self.add_contour('sym-c1', *('sym-e2', 'sym-e3'), closed=False)
        self.add_contour('sym-c2', *('sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27-1', 'sym-e27-2', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36-1', 'sym-e36-2', 'sym-e37', 'sym-e39', 'sym-e40', 'sym-e41', 'sym-e42', 'sym-e45', 'sym-e46', 'sym-e47', 'sym-e48', 'sym-e50', 'sym-e51-1', 'sym-e51-2'), closed=True)
