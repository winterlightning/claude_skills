"""A diagonal flathead screwdriver with chamfered grip and a broad transverse tip; tiny collar and handle marks omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4ff13a33-c5c0-5e99-bb2d-a3a9f2cfd59d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flathead-screwdriver/20260927T075459Z-thuan-mac-1/reference/tools screwdriver_4ff13a33-c5c0-5e99-bb2d-a3a9f2cfd59d.svg'
AUTHOR = "gpt-6"

class FlatheadScrewdriver(Solo48):
    icon_id = 'flathead-screwdriver'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('screwdriver', 'flathead', 'screw', 'hardware', 'repair', 'fix', 'shaft', 'tool')

    def build(self) -> None:


        # The source has a rounded diagonal grip, not a square loop.
        self.add_arc('grip-round', (6, 12), (12, 6), radius_x=6)
        self.add_line('grip-top', (12, 6), (25, 19))
        self.add_line('grip-end-1', (25, 19), (25, 23))
        self.add_line('grip-end-2', (25, 23), (23, 25))
        self.add_line('grip-end-3', (23, 25), (19, 25))
        self.add_line('grip-bottom', (19, 25), (6, 12))
        self.add_contour('handle', 'grip-round', 'grip-top', 'grip-end-1', 'grip-end-2', 'grip-end-3', 'grip-bottom', closed=True)
        self.add_line('shaft',(24,24),(40,40))
        # A short transverse edge reads as a flat blade at this stroke budget.
        self.add_line('flat-tip',(38,42),(42,38))
        self.relate('connect','shaft','handle')
        self.relate('connect','shaft','flat-tip')
