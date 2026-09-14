# Variant of anteater-v3; parent file remains unchanged.
'Anteater v3. Refit snout and quarter-ellipse tail to the current forty-unit horizontal bounds; preserve widened legs.\nOriginal subject geometry is retained and refitted to the current native keyshape. Directional asymmetry is intentional. Construction review: original drawing; sprout or bug principles for the plant and beetle.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR = 'gpt-6'

class AnteaterVariant4(Solo48):
    icon_id = 'anteater-v4'
    variant_of = 'anteater-v3'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('anteater', 'animal', 'mammal', 'snout', 'wildlife', 'zoo', 'silhouette', 'nose')

    def build(self) -> None:
        self.add_line('snout-top', (4, 29), (16, 15))
        self.add_arc('back', (16, 15), (36, 15), radius_x=10, radius_y=7)
        self.add_arc('tail-top', (36, 15), (44, 37), radius_x=8, radius_y=22)
        self.add_arc('tail-bottom', (44, 37), (34, 28), radius_x=10, radius_y=9)
        self.add_line('hind-leg-1', (34, 28), (34, 40))
        self.add_line('hind-leg-2', (34, 40), (26, 40))
        self.add_line('hind-leg-3', (26, 40), (26, 29))
        self.add_line('belly', (26, 29), (18, 29))
        self.add_line('front-leg-1', (18, 29), (18, 40))
        self.add_line('front-leg-2', (18, 40), (10, 40))
        self.add_line('front-leg-3', (10, 40), (10, 29))
        self.add_line('snout-bottom', (10, 29), (4, 29))
        self.add_contour('outline', 'snout-top', 'back', 'tail-top', 'tail-bottom', 'hind-leg-1', 'hind-leg-2', 'hind-leg-3', 'belly', 'front-leg-1', 'front-leg-2', 'front-leg-3', 'snout-bottom', closed=True)
