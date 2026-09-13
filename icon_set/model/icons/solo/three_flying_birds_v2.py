# Variant of three-flying-birds; parent file remains unchanged.
"""Three flying birds reduced to two curved wings each; extremes (2,2)-(46,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd7a738c-4a9b-4749-ad10-1147ea353f15'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_bd7a738c-4a9b-4749-ad10-1147ea353f15.svg'
AUTHOR = 'gpt-6'

class ThreeFlyingBirdsVariant2(Solo48):
    icon_id = 'three-flying-birds-v2'
    variant_of = 'three-flying-birds'
    variant_label = 'Two curved wings per bird'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('birds', 'three', 'flying', 'flock', 'doves', 'sky', 'flight', 'group')

    def build(self) -> None:
        # SQUARE centerline extremes: (2, 2)-(46, 46).
        # Preserve the staggered flock; each bird is two elliptical wing arcs.
        for index, (x, y) in enumerate(((2, 2), (26, 19), (4, 30))):
            left = f"wing-left-{index}"
            right = f"wing-right-{index}"
            self.add_arc(left, (x, y), (x + 10, y + 16),
                         radius_x=10, radius_y=16, sweep=True)
            self.add_arc(right, (x + 10, y + 16), (x + 20, y),
                         radius_x=10, radius_y=16, sweep=True)
            self.add_contour(f"bird-{index}", left, right)
