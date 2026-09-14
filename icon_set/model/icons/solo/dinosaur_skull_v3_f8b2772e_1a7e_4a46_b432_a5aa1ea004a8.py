"""Left-facing dinosaur skull with a larger eye cavity, nostril and open lower jaw. Remove the narrow return band of bone. SQUARE centerline bounds (6,6)-(42,42). No useful exact Lucide skull match; asymmetry preserves side-view anatomy."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8b2772e-1a7e-4a46-b432-a5aa1ea004a8'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/dinosaur skull fossil_f8b2772e-1a7e-4a46-b432-a5aa1ea004a8.svg'
AUTHOR = 'gpt-6'

class DinosaurSkullVariant3(Solo48):
    icon_id = 'dinosaur-skull-v3'
    variant_of = 'dinosaur-skull'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('dinosaur', 'skull', 'fossil', 'prehistoric', 'palaeontology', 'bone', 'raptor', 'museum')

    def build(self):
        self.add_line('nose', (6, 32), (6, 10))
        self.add_arc('nose-corner', (6, 10), (10, 6), radius_x=4)
        self.add_line('forehead', (10, 6), (30, 6))
        self.add_arc('braincase', (30, 6), (42, 18), radius_x=12)
        self.add_line('back', (42, 18), (42, 30))
        self.add_arc('jaw-back', (42, 30), (30, 42), radius_x=12)
        self.add_line('lower-jaw', (30, 42), (10, 42))
        self.add_contour('skull', 'nose', 'nose-corner', 'forehead', 'braincase', 'back', 'jaw-back', 'lower-jaw')
        self.add_line('upper-jaw', (6, 32), (30, 32))
        self.relate('connect', 'skull', 'upper-jaw')
        self.add_arc('eye-a', (29, 15), (29, 23), radius_x=4)
        self.add_arc('eye-b', (29, 23), (29, 15), radius_x=4)
        self.add_contour('eye', 'eye-a', 'eye-b', closed=True)
        self.add_dot('nostril', (15, 20))
