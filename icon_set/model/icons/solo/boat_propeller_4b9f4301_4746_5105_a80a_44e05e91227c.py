"""A three-bladed marine propeller surrounding a round hub. SQUARE ink (6,6)-(42,42). Lucide fan informed one flowing blade outline; three uneven swept blades preserve the source and the boss ring is reduced to a hub dot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b9f4301-4746-5105-a80a-44e05e91227c'
SOURCE_PATH = 'pictographic-primitives/transportation/boat engine blade_4b9f4301-4746-5105-a80a-44e05e91227c.svg'
SOURCE_REFERENCES = (('4b9f4301-4746-5105-a80a-44e05e91227c', 'pictographic-primitives/transportation/boat engine blade_4b9f4301-4746-5105-a80a-44e05e91227c.svg'),)
AUTHOR = 'gpt-6'

class BoatPropeller(Solo48):
    icon_id = 'boat-propeller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('propeller', 'boat', 'marine', 'engine', 'blade', 'screw', 'ship', 'nautical')

    def build(self) -> None:
        # One pinwheel perimeter; deliberate unequal sweeps retain the marine blade silhouette.
        self.add_line('top-neck',(18,16),(18,12))
        self.add_arc('top-left',(18,12),(24,6),radius_x=6)
        self.add_arc('top-right',(24,6),(32,14),radius_x=8)
        self.add_line('top-edge',(32,14),(33,24))
        self.add_line('right-neck',(33,24),(36,24))
        self.add_arc('right-top',(36,24),(42,30),radius_x=6)
        self.add_line('right-side',(42,30),(42,34))
        self.add_arc('right-tip',(42,34),(34,42),radius_x=8)
        self.add_line('right-edge',(34,42),(20,32))
        self.add_line('left-neck',(20,32),(14,36))
        self.add_arc('left-tip',(14,36),(6,28),radius_x=8)
        self.add_line('left-side',(6,28),(6,24))
        self.add_arc('left-top',(6,24),(12,18),radius_x=6)
        self.add_line('left-edge',(12,18),(18,16))
        self.add_contour('blades','top-neck','top-left','top-right','top-edge','right-neck','right-top','right-side','right-tip','right-edge','left-neck','left-tip','left-side','left-top','left-edge',closed=True)
        self.add_dot('hub',(24,24))
