"""Beading wire with beads.

Symbol plan: shared integer nodes preserve contour order, repeated stations and real
attachments. The VRECT_L visible envelope is (6, 2, 42, 46).
The parent remains available for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '908acf0d-8561-4efe-bb3d-9ae2e877dcdc'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/diy bead_908acf0d-8561-4efe-bb3d-9ae2e877dcdc.svg'
AUTHOR = 'gpt-6'

class BeadingWireWithBeads(Solo48):
    icon_id = 'beading-wire-with-beads'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('bead', 'beading', 'diy', 'jewellery', 'jewelry', 'craft', 'wire', 'making', 'handmade')

    def build(self) -> None:
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""
        p_10_15 = (10, 15)
        p_15_15 = (15, 15)
        p_17_18 = (17, 18)
        p_17_25 = (17, 25)
        p_15_28 = (15, 28)
        p_10_28 = (10, 28)
        p_8_25 = (8, 25)
        p_8_18 = (8, 18)
        p_12_4 = (12, 4)
        p_12_15 = (12, 15)
        p_12_28 = (12, 28)
        p_12_44 = (12, 44)
        p_33_4 = (33, 4)
        p_38_4 = (38, 4)
        p_40_7 = (40, 7)
        p_40_14 = (40, 14)
        p_38_17 = (38, 17)
        p_33_17 = (33, 17)
        p_31_14 = (31, 14)
        p_31_7 = (31, 7)
        p_25_31 = (25, 31)
        p_31_31 = (31, 31)
        p_33_34 = (33, 34)
        p_33_41 = (33, 41)
        p_31_44 = (31, 44)
        p_25_44 = (25, 44)
        p_23_41 = (23, 41)
        p_23_34 = (23, 34)
        p_36_17 = (36, 17)
        p_36_23 = (36, 23)
        p_28_31 = (28, 31)
        self.add_line('left-bead-0', p_10_15, p_15_15)
        self.add_arc('left-bead-1', p_15_15, p_17_18, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left-bead-2', p_17_18, p_17_25)
        self.add_arc('left-bead-3', p_17_25, p_15_28, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left-bead-4', p_15_28, p_10_28)
        self.add_arc('left-bead-5', p_10_28, p_8_25, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left-bead-6', p_8_25, p_8_18)
        self.add_arc('left-bead-7', p_8_18, p_10_15, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left-top', p_12_4, p_12_15)
        self.add_line('left-tail', p_12_28, p_12_44)
        self.add_line('right-bead-0', p_33_4, p_38_4)
        self.add_arc('right-bead-1', p_38_4, p_40_7, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('right-bead-2', p_40_7, p_40_14)
        self.add_arc('right-bead-3', p_40_14, p_38_17, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('right-bead-4', p_38_17, p_33_17)
        self.add_arc('right-bead-5', p_33_17, p_31_14, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('right-bead-6', p_31_14, p_31_7)
        self.add_arc('right-bead-7', p_31_7, p_33_4, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('low-bead-0', p_25_31, p_28_31)
        self.add_line('low-bead-0b', p_28_31, p_31_31)
        self.add_arc('low-bead-1', p_31_31, p_33_34, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('low-bead-2', p_33_34, p_33_41)
        self.add_arc('low-bead-3', p_33_41, p_31_44, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('low-bead-4', p_31_44, p_25_44)
        self.add_arc('low-bead-5', p_25_44, p_23_41, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('low-bead-6', p_23_41, p_23_34)
        self.add_arc('low-bead-7', p_23_34, p_25_31, radius_x=2, radius_y=3, sweep=True, large_arc=False)
        self.add_line('wire-a', p_36_17, p_36_23)
        self.add_arc('wire-b', p_36_23, p_28_31, radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('left-bead', 'left-bead-0', 'left-bead-1', 'left-bead-2', 'left-bead-3', 'left-bead-4', 'left-bead-5', 'left-bead-6', 'left-bead-7', closed=True)
        self.add_contour('right-bead', 'right-bead-0', 'right-bead-1', 'right-bead-2', 'right-bead-3', 'right-bead-4', 'right-bead-5', 'right-bead-6', 'right-bead-7', closed=True)
        self.add_contour('low-bead', 'low-bead-0', 'low-bead-0b', 'low-bead-1', 'low-bead-2', 'low-bead-3', 'low-bead-4', 'low-bead-5', 'low-bead-6', 'low-bead-7', closed=True)
        self.add_contour('right-wire', 'wire-a', 'wire-b', closed=False)
        self.relate('connect', 'left-bead', 'left-top')
        self.relate('connect', 'left-bead', 'left-tail')
        self.relate('connect', 'right-wire', 'right-bead')
        self.relate('connect', 'right-wire', 'low-bead')
