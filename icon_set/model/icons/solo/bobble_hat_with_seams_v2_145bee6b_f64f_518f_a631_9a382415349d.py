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
        """Opening repair: Made the bobble a true circle with an open centre."""
        self.add_line('cuff0', (8, 34), (40, 34))
        self.add_arc('cuff1', (40, 34), (42, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff2', (42, 37), (42, 42))
        self.add_arc('cuff3', (42, 42), (40, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff4', (40, 42), (8, 42))
        self.add_arc('cuff5', (8, 42), (6, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_line('cuff6', (6, 42), (6, 37))
        self.add_arc('cuff7', (6, 37), (8, 34), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('cuff', 'cuff0', 'cuff1', 'cuff2', 'cuff3', 'cuff4', 'cuff5', 'cuff6', 'cuff7', closed=True)
        self.add_line('crown-l', (8, 34), (8, 30))
        self.add_arc('crown-a', (8, 30), (24, 14), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('crown-b', (24, 14), (40, 30), radius_x=16, radius_y=16, sweep=True)
        self.add_line('crown-r', (40, 30), (40, 34))
        self.add_contour('crown', 'crown-l', 'crown-a', 'crown-b', 'crown-r', closed=False)
        self.relate('connect', 'crown', 'cuff')
        self.add_arc('bobble-a', (24, 6), (24, 14), sweep=True, radius_x=4, radius_y=4)
        self.add_arc('bobble-b', (24, 14), (24, 6), sweep=True, radius_x=4, radius_y=4)
        self.add_contour('bobble', 'bobble-a', 'bobble-b', closed=True)
        self.relate('connect', 'bobble', 'crown')
