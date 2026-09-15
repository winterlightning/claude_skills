"""Broadened the diamond at its facet and inset the stud and drop ends; retained the facet.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
Lucide gem: broad diamond and a single horizontal facet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '05f75c0e-e1ea-4769-8e00-7f882502017e'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/earring diamond_05f75c0e-e1ea-4769-8e00-7f882502017e.svg'
AUTHOR = 'gpt-6'

class DiamondDropEarring(Solo48):
    icon_id = 'diamond-drop-earring'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'diamond', 'gem', 'jewel', 'jewellery', 'jewelry', 'stud', 'drop', 'accessory')

    def build(self) -> None:
        self.add_arc('stud-a', (24, 14), (24, 4), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('stud-b', (24, 4), (24, 14), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('stud', 'stud-a', 'stud-b', closed=True)
        self.add_line('post', (24, 14), (24, 22))
        self.add_polyline('gem', (18, 22), (24, 22), (30, 22), (40, 30), (24, 44), (8, 30), (18, 22), closed=True)
        self.add_line('facet', (8, 30), (40, 30))
        self.relate('connect', 'post', 'stud')
        self.relate('connect', 'post', 'gem')
        self.relate('connect', 'facet', 'gem')
