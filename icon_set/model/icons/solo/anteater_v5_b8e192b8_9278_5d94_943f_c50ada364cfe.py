# Variant of anteater; parent file remains unchanged.
"""Anteater with long downturned snout and domed back; centerline extremes (6,11)-(42,37). Overlapping far legs omitted. No useful Lucide match; natural profile asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR = 'gpt-6'

class AnteaterVariant5(Solo48):
    icon_id = 'anteater-v5'
    variant_of = 'anteater'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('anteater', 'animal', 'mammal', 'snout', 'wildlife', 'zoo', 'silhouette', 'nose')

    def build(self):
        # Long tapered snout and domed back on a left-facing animal with two broad legs. No useful Lucide anteater match; natural profile asymmetry is intentional.
        self.add_arc('back', (18, 22), (44, 22), radius_x=13, radius_y=14, sweep=True)
        self.add_line('rear', (44, 22), (44, 40))
        self.add_line('hind-foot', (44, 40), (36, 40))
        self.add_line('hind-leg', (36, 40), (34, 29))
        self.add_line('belly', (34, 29), (26, 29))
        self.add_line('fore-leg', (26, 29), (24, 40))
        self.add_line('fore-foot', (24, 40), (16, 40))
        self.add_line('fore-front', (16, 40), (16, 28))
        self.add_line('snout-lower', (16, 28), (4, 32))
        self.add_line('snout-front', (4, 32), (4, 26))
        self.add_line('face', (4, 26), (18, 22))
        self.add_contour('animal', 'back', 'rear', 'hind-foot', 'hind-leg', 'belly', 'fore-leg', 'fore-foot', 'fore-front', 'snout-lower', 'snout-front', 'face', closed=True)
