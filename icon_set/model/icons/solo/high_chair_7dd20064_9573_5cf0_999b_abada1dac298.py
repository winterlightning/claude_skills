from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7dd20064-9573-5cf0-999b-abada1dac298'
SOURCE_PATH = 'pictographic-primitives/babies/food feeding table_7dd20064-9573-5cf0-999b-abada1dac298.svg'
AUTHOR = 'gpt-6'

class HighChair(Solo48):
    icon_id = 'high-chair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('highchair', 'chair', 'feeding', 'baby', 'mealtime', 'infant', 'furniture', 'toddler')

    # Designed to centerline extremes (2, 2)–(46, 46).
    def build(self) -> None:
        self.add_line('tray-1', (2, 19), (46, 19))
        self.add_line('tray-2', (46, 19), (46, 27))
        self.add_line('tray-3', (46, 27), (2, 27))
        self.add_line('tray-4', (2, 27), (2, 19))
        self.add_contour('tray', 'tray-1', 'tray-2', 'tray-3', 'tray-4', closed=True)
        self.add_line('back-1', (13, 19), (11, 9))
        self.add_arc('back-2', (11, 9), (18, 2), radius_x=7, radius_y=7, sweep=True)
        self.add_line('back-3', (18, 2), (30, 2))
        self.add_arc('back-4', (30, 2), (37, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_line('back-5', (37, 9), (35, 19))
        self.add_contour('back', 'back-1', 'back-2', 'back-3', 'back-4', 'back-5', closed=False)
        self.add_line('left-leg-1', (8, 27), (3, 46))
        self.add_contour('left-leg', 'left-leg-1', closed=False)
        self.add_line('right-leg-1', (40, 27), (45, 46))
        self.add_contour('right-leg', 'right-leg-1', closed=False)
        self.add_line('seat-1', (17, 27), (19, 36))
        self.add_line('seat-2', (19, 36), (29, 36))
        self.add_line('seat-3', (29, 36), (31, 27))
        self.add_contour('seat', 'seat-1', 'seat-2', 'seat-3', closed=False)
        self.relate("connect", "tray", "back")
        self.relate("connect", "tray", "left-leg")
        self.relate("connect", "tray", "right-leg")
        self.relate("connect", "tray", "seat")
