"""Loose beading wires with three rounded beads. SQUARE extremes (2,2)-(46,46). Deliberately asymmetric; fewer beads and no tiny facets preserve legibility. No useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '908acf0d-8561-4efe-bb3d-9ae2e877dcdc'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/diy bead_908acf0d-8561-4efe-bb3d-9ae2e877dcdc.svg'
AUTHOR = 'astra-chatgpt'


class BeadingWireWithBeads(Solo48):
    icon_id = 'beading-wire-with-beads'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bead', 'beading', 'diy', 'jewellery', 'jewelry', 'craft', 'wire', 'making', 'handmade')

    def build(self) -> None:
        self.add_line('left-bead-0', (5, 14), (11, 14))
        self.add_arc('left-bead-1', (11, 14), (14, 17), radius_x=3, radius_y=3, sweep=True)
        self.add_line('left-bead-2', (14, 17), (14, 25))
        self.add_arc('left-bead-3', (14, 25), (11, 28), radius_x=3, radius_y=3, sweep=True)
        self.add_line('left-bead-4', (11, 28), (5, 28))
        self.add_arc('left-bead-5', (5, 28), (2, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_line('left-bead-6', (2, 25), (2, 17))
        self.add_arc('left-bead-7', (2, 17), (5, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left-bead', 'left-bead-0', 'left-bead-1', 'left-bead-2', 'left-bead-3', 'left-bead-4', 'left-bead-5', 'left-bead-6', 'left-bead-7', closed=True)
        self.add_line('left-top', (8, 2), (8, 14))
        self.add_line('left-tail', (8, 28), (8, 46))
        self.relate("connect", 'left-bead', 'left-top')
        self.relate("connect", 'left-bead', 'left-tail')
        self.add_line('right-bead-0', (37, 2), (43, 2))
        self.add_arc('right-bead-1', (43, 2), (46, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_line('right-bead-2', (46, 5), (46, 13))
        self.add_arc('right-bead-3', (46, 13), (43, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_line('right-bead-4', (43, 16), (37, 16))
        self.add_arc('right-bead-5', (37, 16), (34, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_line('right-bead-6', (34, 13), (34, 5))
        self.add_arc('right-bead-7', (34, 5), (37, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right-bead', 'right-bead-0', 'right-bead-1', 'right-bead-2', 'right-bead-3', 'right-bead-4', 'right-bead-5', 'right-bead-6', 'right-bead-7', closed=True)
        self.add_line('low-bead-0', (26, 32), (34, 32))
        self.add_arc('low-bead-1', (34, 32), (37, 35), radius_x=3, radius_y=3, sweep=True)
        self.add_line('low-bead-2', (37, 35), (37, 43))
        self.add_arc('low-bead-3', (37, 43), (34, 46), radius_x=3, radius_y=3, sweep=True)
        self.add_line('low-bead-4', (34, 46), (26, 46))
        self.add_arc('low-bead-5', (26, 46), (23, 43), radius_x=3, radius_y=3, sweep=True)
        self.add_line('low-bead-6', (23, 43), (23, 35))
        self.add_arc('low-bead-7', (23, 35), (26, 32), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('low-bead', 'low-bead-0', 'low-bead-1', 'low-bead-2', 'low-bead-3', 'low-bead-4', 'low-bead-5', 'low-bead-6', 'low-bead-7', closed=True)
        self.add_line('wire-a', (40, 16), (40, 23))
        self.add_arc('wire-b', (40, 23), (30, 32), radius_x=10, radius_y=9, sweep=True)
        self.add_contour('right-wire', 'wire-a', 'wire-b', closed=False)
        self.relate("connect", 'right-wire', 'right-bead')
        self.relate("connect", 'right-wire', 'low-bead')
