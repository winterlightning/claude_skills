"""Color palette sample (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca1b998f-0a5f-47b5-a6aa-2effc22a4f39'
SOURCE_PATH = 'icons-json/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.json'
AUTHOR = 'gpt-6'

class ColorPaletteSample(Solo48):
    icon_id = 'color-palette-sample'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('color', 'palette', 'sample', 'design')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (19, 21), (21, 22))
        self.add_line('e1', (28, 13), (28, 17))
        self.add_line('e2', (19, 33), (22, 32))
        self.add_line('e3', (37, 23), (34, 26))
        self.add_line('e4', (32, 31), (32, 36))
        self.add_line('e5', (34, 26), (32, 31))
        self.add_arc('e6-1', (32, 36), (24, 44), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e6-2', (24, 44), (13, 39), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('e6-3', (13, 39), (8, 26), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e6-4', (8, 26), (8, 23), radius_x=50, radius_y=50, large_arc=False, sweep=False)
        self.add_arc('e6-5', (8, 23), (13, 11), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_arc('e6-6', (13, 11), (26, 4), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('e6-7', (26, 4), (34, 6))
        self.add_arc('e6-8', (34, 6), (38, 10), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('e6-9', (38, 10), (40, 17))
        self.add_arc('e6-10', (40, 17), (37, 23), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3', 'e5', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e6-9', 'e6-10'), closed=True)
