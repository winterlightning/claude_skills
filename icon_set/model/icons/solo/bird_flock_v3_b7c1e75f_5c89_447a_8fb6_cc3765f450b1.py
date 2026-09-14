"""Replaced crowded miniature heads and bodies with five repeated paired wings, arranged 2/1/2. Covers both older flock versions.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: bird: reduced curved silhouette; no exact flock match.
"""
# Independent repair of bird-flock; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7c1e75f-5c89-447a-8fb6-cc3765f450b1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_b7c1e75f-5c89-447a-8fb6-cc3765f450b1.svg'
AUTHOR = 'gpt-6'

class BirdFlockVariant3(Solo48):
    icon_id = 'bird-flock-v3'
    variant_of = 'bird-flock'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('birds', 'flock', 'flying', 'group', 'five', 'migration', 'sky', 'flight')

    def build(self) -> None:
        # SQUARE centerlines (6,6)-(42,42). Five repeated paired wings,
        # arranged 2/1/2 with ten units between neighbors. Fine heads omitted.
        span, drop = 6, 4
        for i,(x,y) in enumerate(((6,6),(30,6),(18,22),(6,38),(30,38))):
            self.add_arc(f'left-{i}',(x,y),(x+span,y+drop),radius_x=span,radius_y=drop)
            self.add_arc(f'right-{i}',(x+span,y+drop),(x+2*span,y),radius_x=span,radius_y=drop,sweep=True)
            self.add_contour(f'bird-{i}',f'left-{i}',f'right-{i}')
