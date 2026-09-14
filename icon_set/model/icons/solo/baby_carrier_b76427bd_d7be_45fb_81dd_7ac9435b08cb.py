from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b76427bd-d7be-45fb-81dd-7ac9435b08cb'
SOURCE_PATH = 'pictographic-primitives/babies/gear baby strap on holder_b76427bd-d7be-45fb-81dd-7ac9435b08cb.svg'
AUTHOR = 'gpt-6'

class BabyCarrier(Solo48):
    icon_id = 'baby-carrier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('carrier', 'sling', 'baby', 'harness', 'papoose', 'straps', 'infant', 'gear')

    # Designed to centerline extremes (6, 6)–(42, 42).
    def build(self) -> None:
        self.add_arc('panel-1', (10, 18), (38, 18), radius_x=24, radius_y=14, sweep=True)
        self.add_arc('panel-2', (38, 18), (31, 38), radius_x=25, radius_y=25, sweep=False)
        self.add_line('panel-3', (31, 38), (34, 42))
        self.add_line('panel-4', (34, 42), (14, 42))
        self.add_line('panel-5', (14, 42), (17, 38))
        self.add_arc('panel-6', (17, 38), (10, 18), radius_x=25, radius_y=25, sweep=False)
        self.add_contour('panel', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', closed=True)
        self.add_line('strap-left-1', (10, 18), (10, 6))
        self.add_line('strap-left-2', (10, 6), (18, 6))
        self.add_line('strap-left-3', (18, 6), (18, 14))
        self.add_contour('strap-left', 'strap-left-1', 'strap-left-2', 'strap-left-3', closed=False)
        self.add_line('strap-right-1', (30, 14), (30, 6))
        self.add_line('strap-right-2', (30, 6), (38, 6))
        self.add_line('strap-right-3', (38, 6), (38, 18))
        self.add_contour('strap-right', 'strap-right-1', 'strap-right-2', 'strap-right-3', closed=False)
        self.add_line('belt-left-1', (17, 36), (6, 36))
        self.add_line('belt-left-2', (6, 36), (6, 42))
        self.add_line('belt-left-3', (6, 42), (14, 42))
        self.add_contour('belt-left', 'belt-left-1', 'belt-left-2', 'belt-left-3', closed=False)
        self.add_line('belt-right-1', (34, 42), (42, 42))
        self.add_line('belt-right-2', (42, 42), (42, 36))
        self.add_line('belt-right-3', (42, 36), (31, 36))
        self.add_contour('belt-right', 'belt-right-1', 'belt-right-2', 'belt-right-3', closed=False)
        self.relate("connect", "panel", "strap-left")
        self.relate("connect", "panel", "strap-right")
        self.relate("connect", "panel", "belt-left")
        self.relate("connect", "panel", "belt-right")
