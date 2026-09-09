# Variant of bobble-hat-with-seams; parent file remains unchanged.
"""A bobble hat with a deep cuff and two short crown seams."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '145bee6b-f64f-518f-a631-9a382415349d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/beanie winter_145bee6b-f64f-518f-a631-9a382415349d.svg'
AUTHOR = 'gpt-6'

class BobbleHatWithSeamsVariant2(Solo48):
    icon_id = 'bobble-hat-with-seams-v2'
    variant_of = 'bobble-hat-with-seams'
    variant_label = 'remove two lines inside'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cap', 'clothing')

    def build(self) -> None:
        self.add_line('cuff0', (8, 34), (40, 34))
        self.add_arc('cuff1', (40, 34), (43, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff2', (43, 37), (43, 43))
        self.add_arc('cuff3', (43, 43), (40, 46), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff4', (40, 46), (8, 46))
        self.add_arc('cuff5', (8, 46), (5, 43), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff6', (5, 43), (5, 37))
        self.add_arc('cuff7', (5, 37), (8, 34), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('cuff', 'cuff0', 'cuff1', 'cuff2', 'cuff3', 'cuff4', 'cuff5', 'cuff6', 'cuff7', closed=True)
        self.add_line('crown-l', (8, 34), (8, 30))
        self.add_arc('crown-a', (8, 30), (24, 14), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('crown-b', (24, 14), (40, 30), radius_x=16, radius_y=16, sweep=True)
        self.add_line('crown-r', (40, 30), (40, 34))
        self.add_contour('crown', 'crown-l', 'crown-a', 'crown-b', 'crown-r', closed=False)
        self.relate('connect', 'crown', 'cuff')
        self.add_arc('bobble-a', (24, 2), (24, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('bobble-b', (24, 14), (24, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('bobble', 'bobble-a', 'bobble-b', closed=True)
        self.relate('connect', 'bobble', 'crown')
