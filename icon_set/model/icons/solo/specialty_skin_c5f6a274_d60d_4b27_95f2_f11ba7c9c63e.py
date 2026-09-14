"""Specialty skin (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5f6a274-d60d-4b27-95f2-f11ba7c9c63e'
SOURCE_PATH = 'icons-json/health/specialty skin_c5f6a274-d60d-4b27-95f2-f11ba7c9c63e.json'
AUTHOR = 'gpt-6'

class SpecialtySkin(Solo48):
    icon_id = 'specialty-skin'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('specialty', 'skin', 'health')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('sym-e0', (4, 8), (44, 8))
        self.add_arc('sym-e1-1', (24, 18), (26, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('sym-e1-2', (26, 18), (32, 24), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('sym-e2', (32, 24), (37, 18), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (37, 18), (40, 17), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e4', (29, 32), (29, 40))
        self.add_line('sym-e5', (37, 40), (37, 32))
        self.add_arc('sym-e6-1', (24, 18), (22, 18), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('sym-e6-2', (22, 18), (16, 24), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (16, 24), (11, 18), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e8', (11, 18), (8, 17), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e9', (19, 32), (19, 40))
        self.add_line('sym-e10', (11, 40), (11, 32))
        self.add_contour('sym-c0', *('sym-e0',), closed=False)
        self.add_contour('sym-c1', *('sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e3'), closed=False)
        self.add_contour('sym-c2', *('sym-e4',), closed=False)
        self.add_contour('sym-c3', *('sym-e5',), closed=False)
        self.add_contour('sym-c4', *('sym-e6-1', 'sym-e6-2', 'sym-e7', 'sym-e8'), closed=False)
        self.add_contour('sym-c5', *('sym-e9',), closed=False)
        self.add_contour('sym-c6', *('sym-e10',), closed=False)
        self.relate('connect', *('sym-c1', 'sym-c4'))
