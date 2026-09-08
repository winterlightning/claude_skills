"""A circular stud suspends a diamond drop; omit the crowded vertical facet.

Lucide construction: gem: tapered silhouette and one horizontal facet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05f75c0e-e1ea-4769-8e00-7f882502017e'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/earring diamond_05f75c0e-e1ea-4769-8e00-7f882502017e.svg'
AUTHOR = 'astra-chatgpt'


class DiamondDropEarring(Solo48):
    icon_id = 'diamond-drop-earring'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('earring', 'diamond', 'gem', 'jewel', 'jewellery', 'jewelry', 'stud', 'drop', 'accessory')

    def build(self) -> None:
        # Exact keyshape envelope: (9, 0, 39, 48).
        self.add_arc('stud-a', (24, 12), (24, 2), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('stud-b', (24, 2), (24, 12), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('stud', 'stud-a', 'stud-b', closed=True)
        self.add_line('post', (24, 12), (24, 20))
        self.add_polyline('gem', (18, 20), (24, 20), (30, 20), (37, 28), (24, 46), (11, 28), (18, 20), closed=True)
        self.add_line('facet', (11, 28), (37, 28))
        self.relate("connect", 'post', 'stud')
        self.relate("connect", 'post', 'gem')
        self.relate("connect", 'facet', 'gem')
