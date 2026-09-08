"""Domed knit cap with deep cuff. HRECT_XL (2,5)-(46,43) keeps the wide silhouette. No details dropped. Symmetric crown and tangent quarter-circle corners."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e562e3f9-df4c-5aa5-883f-3833004c6400'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/beanie_e562e3f9-df4c-5aa5-883f-3833004c6400.svg'
AUTHOR = 'astra-chatgpt'


class CuffedBeanie(Solo48):
    icon_id = 'cuffed-beanie'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('beanie', 'hat', 'winter', 'knit', 'cap', 'cuff', 'clothing', 'headwear')

    def build(self) -> None:
        self.add_line('cuff0', (5, 31), (6, 31))
        self.add_line('cuff-top', (6, 31), (42, 31))
        self.add_line('cuff-end', (42, 31), (43, 31))
        self.add_arc('cuff1', (43, 31), (46, 34), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff2', (46, 34), (46, 40))
        self.add_arc('cuff3', (46, 40), (43, 43), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff4', (43, 43), (5, 43))
        self.add_arc('cuff5', (5, 43), (2, 40), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cuff6', (2, 40), (2, 34))
        self.add_arc('cuff7', (2, 34), (5, 31), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('cuff', 'cuff0', 'cuff-top', 'cuff-end', 'cuff1', 'cuff2', 'cuff3', 'cuff4', 'cuff5', 'cuff6', 'cuff7', closed=True)
        self.add_line('crown-l', (6, 31), (6, 23))
        self.add_arc('crown', (6, 23), (42, 23), radius_x=18, radius_y=18, sweep=True, large_arc=False)
        self.add_line('crown-r', (42, 23), (42, 31))
        self.add_contour('crown-outline', 'crown-l', 'crown', 'crown-r', closed=False)
        self.relate("connect", 'cuff', 'crown-outline')
