"""Anteater with long downturned snout and domed back; centerline extremes (6,11)-(42,37). Overlapping far legs omitted. No useful Lucide match; natural profile asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR = 'gpt-6'

class Anteater(Solo48):
    icon_id = 'anteater'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('anteater', 'animal', 'mammal', 'snout', 'wildlife', 'zoo', 'silhouette', 'nose')

    def build(self):
        # Long sloping snout, domed back and tapering tail identify a left-facing anteater. Two broad legs preserve open negative space. No useful Lucide anteater match; natural profile asymmetry is intentional.
        self.add_arc('back', (18, 20), (36, 20), radius_x=9, radius_y=12, sweep=True)
        self.add_line('tail-top', (36, 20), (44, 32))
        self.add_line('tail-bottom', (44, 32), (34, 30))
        self.add_line('hind-leg', (34, 30), (34, 40))
        self.add_line('hind-foot', (34, 40), (26, 40))
        self.add_line('hind-inner', (26, 40), (26, 30))
        self.add_line('belly', (26, 30), (18, 30))
        self.add_line('fore-inner', (18, 30), (18, 40))
        self.add_line('fore-foot', (18, 40), (10, 40))
        self.add_line('fore-front', (10, 40), (12, 26))
        self.add_line('snout-lower', (12, 26), (4, 30))
        self.add_line('snout-tip', (4, 30), (4, 24))
        self.add_line('snout-top', (4, 24), (18, 20))
        self.add_contour('animal', 'back', 'tail-top', 'tail-bottom', 'hind-leg', 'hind-foot', 'hind-inner', 'belly', 'fore-inner', 'fore-foot', 'fore-front', 'snout-lower', 'snout-tip', 'snout-top', closed=True)
