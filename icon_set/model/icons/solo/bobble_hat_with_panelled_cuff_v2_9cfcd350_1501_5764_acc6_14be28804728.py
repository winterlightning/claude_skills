# Variant of bobble-hat-with-panelled-cuff; parent file remains unchanged.
"""Bobble hat with three cuff panels. VRECT_XL extremes (6,6)-(42,42). Mirrored crown and cuff; pompom meets the crown at its apex. No exact useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9cfcd350-1501-5764-acc6-14be28804728'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/beanie winter_9cfcd350-1501-5764-acc6-14be28804728.svg'
AUTHOR = 'gpt-6'

class BobbleHatWithPanelledCuffVariant2(Solo48):
    icon_id = 'bobble-hat-with-panelled-cuff-v2'
    variant_of = 'bobble-hat-with-panelled-cuff'
    variant_label = 'remove two lines inside the hat, only one line between'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cuff', 'clothing')

    def build(self) -> None:
        self.add_line('cuff-0-attach-0', (8, 32), (18, 32))
        self.add_line('cuff-0-attach-1', (18, 32), (30, 32))
        self.add_line('cuff-0-attach-2', (30, 32), (40, 32))
        self.add_arc('cuff-1', (40, 32), (42, 35), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff-2', (42, 35), (42, 42))
        self.add_arc('cuff-3', (42, 42), (40, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff-4-attach-0', (40, 42), (30, 42))
        self.add_line('cuff-4-attach-1', (30, 42), (18, 42))
        self.add_line('cuff-4-attach-2', (18, 42), (8, 42))
        self.add_arc('cuff-5', (8, 42), (6, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff-6', (6, 42), (6, 35))
        self.add_arc('cuff-7', (6, 35), (8, 32), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('cuff', 'cuff-0-attach-0', 'cuff-0-attach-1', 'cuff-0-attach-2', 'cuff-1', 'cuff-2', 'cuff-3', 'cuff-4-attach-0', 'cuff-4-attach-1', 'cuff-4-attach-2', 'cuff-5', 'cuff-6', 'cuff-7', closed=True)
        self.add_arc('crown-left', (8, 32), (24, 12), radius_x=16, radius_y=20, sweep=True)
        self.add_arc('crown-right', (24, 12), (40, 32), radius_x=16, radius_y=20, sweep=True)
        self.add_contour('crown', 'crown-left', 'crown-right', closed=False)
        self.add_arc('bobble-0', (24, 6), (29, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('bobble-1', (29, 7), (24, 12), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('bobble-2', (24, 12), (19, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('bobble-3', (19, 7), (24, 6), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('bobble', 'bobble-0', 'bobble-1', 'bobble-2', 'bobble-3', closed=True)
        self.relate('connect', 'bobble', 'crown')
        self.relate('connect', 'cuff', 'crown')
