# Variant of dinosaur-skull; parent file remains unchanged.
'dinosaur-skull: Used the square envelope to widen both jaw gaps; the eye becomes a dot and the nostril is omitted. Keyshape SQUARE; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8b2772e-1a7e-4a46-b432-a5aa1ea004a8'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/dinosaur skull fossil_f8b2772e-1a7e-4a46-b432-a5aa1ea004a8.svg'
AUTHOR = 'gpt-6'

class DinosaurSkullVariant5(Solo48):
    icon_id = 'dinosaur-skull-v5'
    variant_of = 'dinosaur-skull'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('dinosaur', 'skull', 'fossil', 'prehistoric', 'palaeontology', 'bone', 'raptor', 'museum')

    def build(self) -> None:
        # Square envelope gives the eye and both jaw levels nine-unit bands.
        top = [(6, 24), (6, 20), (10, 10), (28, 6), (30, 6)]
        jaw = [(30, 42), (14, 42), (6, 33), (28, 33), (32, 24), (6, 24)]
        for name, points in [('snout', top), ('jaw', jaw)]:
            for i, (a, b) in enumerate(zip(points, points[1:]), 1):
                self.add_line(f'{name}-{i}', a, b)
        self.add_arc('braincase', (30, 6), (42, 18), radius_x=12)
        self.add_line('back', (42, 18), (42, 30))
        self.add_arc('jaw-back', (42, 30), (30, 42), radius_x=12)
        self.add_contour('skull', 'snout-1', 'snout-2', 'snout-3', 'snout-4', 'braincase', 'back', 'jaw-back', 'jaw-1', 'jaw-2', 'jaw-3', 'jaw-4', 'jaw-5', closed=True)
        self.add_dot('eye', (30, 15))
        # Nostril omitted to preserve clearance inside the snout.
