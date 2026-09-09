"""Side-view anteater with long pointed snout, two visible legs and bushy tail. HRECT_L (2,8)-(46,40). Removed anonymous dome silhouette and overlapping detail. No useful exact Lucide match; intentional profile asymmetry."""
# Variant of anteater; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR = 'gpt-6'

class AnteaterVariant2(Solo48):
    icon_id = 'anteater-v2'
    variant_of = 'anteater'
    variant_label = 'Long snout and bushy tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('anteater', 'animal', 'mammal', 'snout', 'wildlife', 'zoo', 'silhouette', 'nose')

    def build(self) -> None:
        # Side profile: tapered muzzle on left, long bushy tail on right.
        # Centerline extremes (2,8)-(46,40).
        self.add_line('snout-top',(2,29),(16,15))
        self.add_arc('back',(16,15),(36,15),radius_x=10,radius_y=7)
        self.add_arc('tail-top',(36,15),(46,37),radius_x=10,radius_y=22)
        self.add_arc('tail-bottom',(46,37),(33,28),radius_x=13,radius_y=9)
        self.add_line('hind-leg-1', (33, 28), (33, 40))
        self.add_line('hind-leg-2', (33, 40), (26, 40))
        self.add_line('hind-leg-3', (26, 40), (26, 29))
        self.add_line('belly',(26,29),(20,29))
        self.add_line('front-leg-1', (20, 29), (17, 40))
        self.add_line('front-leg-2', (17, 40), (10, 40))
        self.add_line('front-leg-3', (10, 40), (13, 25))
        self.add_line('snout-bottom',(13,25),(2,29))
        self.add_contour('outline','snout-top','back','tail-top','tail-bottom','hind-leg-1','hind-leg-2','hind-leg-3','belly','front-leg-1','front-leg-2','front-leg-3','snout-bottom',closed=True)
