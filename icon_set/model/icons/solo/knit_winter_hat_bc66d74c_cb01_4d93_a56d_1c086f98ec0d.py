"""A domed knit hat on a deep rolled cuff. HRECT_XL extremes (2,5)-(46,43). Shared circular radii and straight tangents; no useful exact Lucide match. No knitted texture added."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc66d74c-cb01-4d93-a56d-1c086f98ec0d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/hat winter_bc66d74c-cb01-4d93-a56d-1c086f98ec0d.svg'
AUTHOR = 'astra-chatgpt'


class KnitWinterHat(Solo48):
    icon_id = 'knit-winter-hat'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hat', 'winter hat', 'beanie', 'knit', 'cuff', 'cold', 'headwear', 'clothing')

    def build(self) -> None:
        self.add_line('crown-left', (6, 29), (6, 23))
        self.add_arc('dome', (6, 23), (42, 23), radius_x=18, radius_y=18, sweep=True)
        self.add_line('crown-right', (42, 23), (42, 29))
        self.add_contour('crown', 'crown-left', 'dome', 'crown-right', closed=False)
        self.add_line('cuff-0', (6, 29), (42, 29))
        self.add_arc('cuff-1', (42, 29), (46, 33), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cuff-2', (46, 33), (46, 39))
        self.add_arc('cuff-3', (46, 39), (42, 43), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cuff-4', (42, 43), (6, 43))
        self.add_arc('cuff-5', (6, 43), (2, 39), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cuff-6', (2, 39), (2, 33))
        self.add_arc('cuff-7', (2, 33), (6, 29), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('cuff', 'cuff-0', 'cuff-1', 'cuff-2', 'cuff-3', 'cuff-4', 'cuff-5', 'cuff-6', 'cuff-7', closed=True)
        self.relate("connect", 'crown', 'cuff')
