"""Five flying birds, each exactly two joined curved wings. HRECT_XL (2,5)-(46,43). Removed miniature heads, bellies and angular wing segments. Lucide bird informed reduction, but no useful exact flock match."""
# Variant of bird-flock; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7c1e75f-5c89-447a-8fb6-cc3765f450b1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_b7c1e75f-5c89-447a-8fb6-cc3765f450b1.svg'
AUTHOR = 'gpt-6'

class BirdFlockVariant2(Solo48):
    icon_id = 'bird-flock-v2'
    variant_of = 'bird-flock'
    variant_label = 'Two curves per bird'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('birds', 'flock', 'flying', 'group', 'five', 'migration', 'sky', 'flight')

    def build(self) -> None:
        # Five birds, each two quarter-ellipse wing curves; extremes (2,5)-(46,43).
        for i, (x, y) in enumerate(((2,5),(28,5),(15,21),(2,37),(28,37))):
            self.add_arc(f'left-{i}', (x,y), (x+9,y+6), radius_x=9, radius_y=6)
            self.add_arc(f'right-{i}', (x+9,y+6), (x+18,y), radius_x=9, radius_y=6)
            self.add_contour(f'bird-{i}', f'left-{i}', f'right-{i}')
