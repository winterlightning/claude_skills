"""Diving mask above a fish, with a tall hooked snorkel on the right.
HRECT_L (4,8)-(44,40) budgets three separated objects. Mask lobes mirror x16;
fish outline mirrors y36. Source supplies arrangement; Lucide fish supplies
continuous lens contour. Omit eye, gill and double mask rim at native scale.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "6803aca6-23a8-44ba-9b90-120d6647b7db"
SOURCE_PATH = "pictographic-primitives/_uncategorized_15/diving mask fish_6803aca6-23a8-44ba-9b90-120d6647b7db.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "diving-mask-snorkel-and-fish-set"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ("Diving Mask Snorkel and Fish",)
    keywords = ("diving", "mask", "snorkel", "fish", "underwater", "equipment", "swimming")
    def build(self):
        self.add_line("mask-top",(10,8),(22,8))
        self.add_arc("mask-right",(22,8),(22,20),radius_x=6)
        self.add_bezier("mask-nose",(22,20),((19,20),(18,18),(16,16)),((14,18),(13,20),(10,20)))
        self.add_arc("mask-left",(10,20),(10,8),radius_x=6)
        self.add_contour("mask","mask-top","mask-right","mask-nose","mask-left",closed=True)
        self.add_line("tube",(44,8),(44,24))
        self.add_arc("tube-turn",(44,24),(36,32),radius_x=8)
        self.add_line("tube-end",(36,32),(32,32))
        self.add_contour("snorkel","tube","tube-turn","tube-end")
        self.add_arc("mouth-top",(32,32),(24,32),radius_x=4)
        self.add_arc("mouth-bottom",(24,32),(32,32),radius_x=4)
        self.add_contour("mouthpiece","mouth-top","mouth-bottom",closed=True)
        self.relate("connect","snorkel","mouthpiece")
        self.add_bezier("fish-body",(8,36),((10,31),(14,31),(16,36)),((14,41),(10,41),(8,36)))
        self.add_contour("fish","fish-body",closed=True)
        self.add_polyline("tail",(4,32),(8,36),(4,40))
        self.relate("connect","fish","tail")
