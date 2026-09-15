"""A Cupid arrow pierces a heart diagonally; one fletching chevron replaces tiny feathers.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32295af4-defa-5f3c-af21-d930830f3a88'
SOURCE_PATH = 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg'
AUTHOR = 'gpt-6'

class HeartPiercedByArrow(Solo48):
    icon_id = 'heart-pierced-by-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('heart', 'arrow', 'cupid', 'love', 'romance', 'pierced')

    def build(self) -> None:
        """Remove the crowded upper barb beside the heart lobe; the remaining open arrowhead preserves direction."""
        self.add_arc('lobe-l', (24, 12), (12, 12), radius_x=6, sweep=False)
        self.add_arc('shoulder-l', (12, 12), (14, 16), radius_x=5, sweep=False)
        self.add_line('side-l-upper', (14, 16), (20, 28))
        self.add_line('side-l-lower', (20, 28), (24, 34))
        self.add_line('side-r-lower', (24, 34), (28, 28))
        self.add_line('side-r-upper', (28, 28), (34, 16))
        self.add_arc('shoulder-r', (34, 16), (36, 12), radius_x=5, sweep=False)
        self.add_arc('lobe-r', (36, 12), (24, 12), radius_x=6, sweep=False)
        self.add_contour('heart', 'lobe-l', 'shoulder-l', 'side-l-upper', 'side-l-lower', 'side-r-lower', 'side-r-upper', 'shoulder-r', 'lobe-r', closed=True)
        self.add_line('arrow-inside', (28, 20), (36, 12))
        self.add_line('arrow-outside', (36, 12), (42, 6))
        self.add_contour('arrow-front', 'arrow-inside', 'arrow-outside')
        self.add_polyline('arrowhead', (42, 6), (42, 14))
        self.relate('connect', 'arrow-front', 'arrowhead')
        self.relate('connect', 'arrow-front', 'heart')
        self.add_line('arrow-back', (6, 42), (20, 28))
        self.add_polyline('fletching', (6, 34), (6, 42), (14, 42))
        self.relate('connect', 'arrow-back', 'fletching')
        self.relate('connect', 'arrow-back', 'heart')
