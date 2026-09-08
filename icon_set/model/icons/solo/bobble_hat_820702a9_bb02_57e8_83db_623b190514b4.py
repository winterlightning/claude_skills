"""A domed winter beanie with a round pompom and deep cuff; omit knit texture.

Lucide construction: chef-hat: separate cuff and rounded crown.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '820702a9-bb02-57e8-83db-623b190514b4'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/beanie winter_820702a9-bb02-57e8-83db-623b190514b4.svg'
AUTHOR = 'astra-chatgpt'


class BobbleHat(Solo48):
    icon_id = 'bobble-hat'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cap', 'clothing')

    def build(self) -> None:
        # Exact keyshape envelope: (3, 0, 45, 48).
        self.add_arc('pompom-a', (24, 10), (24, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('pompom-b', (24, 2), (24, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('pompom', 'pompom-a', 'pompom-b', closed=True)
        self.add_arc('crown-left', (7, 30), (24, 10), radius_x=17, radius_y=20, sweep=True)
        self.add_arc('crown-right', (24, 10), (41, 30), radius_x=17, radius_y=20, sweep=True)
        self.add_line('crown-r', (41, 30), (41, 34))
        self.add_line('crown-l', (7, 34), (7, 30))
        self.add_contour('crown', 'crown-l', 'crown-left', 'crown-right', 'crown-r', closed=False)
        self.add_line('cuff-0', (8, 34), (40, 34))
        self.add_arc('cuff-1', (40, 34), (43, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff-2', (43, 37), (43, 43))
        self.add_arc('cuff-3', (43, 43), (40, 46), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff-4', (40, 46), (8, 46))
        self.add_arc('cuff-5', (8, 46), (5, 43), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff-6', (5, 43), (5, 37))
        self.add_arc('cuff-7', (5, 37), (8, 34), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('cuff', 'cuff-0', 'cuff-1', 'cuff-2', 'cuff-3', 'cuff-4', 'cuff-5', 'cuff-6', 'cuff-7', closed=True)
        self.relate("connect", 'pompom', 'crown')
        self.relate("connect", 'crown', 'cuff')
