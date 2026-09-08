"""A beaded necklace with a large hexagonal pendant. SQUARE extremes (2,2)-(46,46). Lucide gem informs a clean faceted outline; internal facets omitted. Symmetric round beads and exposed links replace densely packed elongated beads."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '841a5bf7-536d-4e60-990e-9259f832c6ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/necklace stone_841a5bf7-536d-4e60-990e-9259f832c6ea.svg'
AUTHOR = 'astra-chatgpt'


class BeadedNecklaceWithHexagonStone(Solo48):
    icon_id = 'beaded-necklace-with-hexagon-stone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necklace', 'bead', 'stone', 'hexagon', 'gem', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self) -> None:
        self.add_arc('left-upper-0', (8, 5), (5, 8), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-upper-1', (5, 8), (2, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-upper-2', (2, 5), (5, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-upper-3', (5, 2), (8, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left-upper', 'left-upper-0', 'left-upper-1', 'left-upper-2', 'left-upper-3', closed=True)
        self.add_arc('right-upper-0', (46, 5), (43, 8), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-upper-1', (43, 8), (40, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-upper-2', (40, 5), (43, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-upper-3', (43, 2), (46, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right-upper', 'right-upper-0', 'right-upper-1', 'right-upper-2', 'right-upper-3', closed=True)
        self.add_arc('left-low-0', (16, 15), (13, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-low-1', (13, 18), (10, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-low-2', (10, 15), (13, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-low-3', (13, 12), (16, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left-low', 'left-low-0', 'left-low-1', 'left-low-2', 'left-low-3', closed=True)
        self.add_arc('right-low-0', (38, 15), (35, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-low-1', (35, 18), (32, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-low-2', (32, 15), (35, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-low-3', (35, 12), (38, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right-low', 'right-low-0', 'right-low-1', 'right-low-2', 'right-low-3', closed=True)
        self.add_line('link', (24, 21), (24, 28))
        self.add_polyline('stone', (24, 28), (34, 33), (34, 41), (24, 46), (14, 41), (14, 33), closed=True)
        self.relate("connect", 'link', 'stone')
        self.add_line('wire-left-upper', (5, 8), (10, 15))
        self.add_line('wire-right-upper', (43, 8), (38, 15))
        self.add_line('wire-left-low', (16, 15), (24, 21))
        self.add_line('wire-right-low', (32, 15), (24, 21))
        self.relate('connect', 'wire-left-upper', 'left-upper')
        self.relate('connect', 'wire-left-upper', 'left-low')
        self.relate('connect', 'wire-right-upper', 'right-upper')
        self.relate('connect', 'wire-right-upper', 'right-low')
        self.relate('connect', 'wire-left-low', 'left-low')
        self.relate('connect', 'wire-right-low', 'right-low')
        self.relate('connect', 'wire-left-low', 'wire-right-low')
        self.relate('connect', 'wire-left-low', 'link')
        self.relate('connect', 'wire-right-low', 'link')
