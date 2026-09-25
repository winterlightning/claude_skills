'Orchid in shallow planter.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1671babf-646b-4546-9934-15f0b91cdf66'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/orchid_1671babf-646b-4546-9934-15f0b91cdf66.svg'
AUTHOR = 'gpt-6'

class OrchidInShallowPlanter(Solo48):
    icon_id = 'orchid-in-shallow-planter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('orchid', 'flowers', 'blossoms', 'planter', 'leaves', 'stems', 'plant')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_18 = (6, 18)
        p_14_18 = (14, 18)
        p_10_22 = (10, 22)
        p_10_34 = (10, 34)
        p_20_10 = (20, 10)
        p_28_10 = (28, 10)
        p_24_14 = (24, 14)
        p_24_34 = (24, 34)
        p_34_18 = (34, 18)
        p_42_18 = (42, 18)
        p_38_22 = (38, 22)
        p_38_34 = (38, 34)
        p_6_34 = (6, 34)
        p_42_34 = (42, 34)
        p_38_42 = (38, 42)
        p_10_42 = (10, 42)
        self.add_arc('flower-0-top', p_6_18, p_14_18, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('flower-0-bottom', p_14_18, p_6_18, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('stem-0', p_10_22, p_10_34)
        self.add_arc('flower-1-top', p_20_10, p_28_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('flower-1-bottom', p_28_10, p_20_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('stem-1', p_24_14, p_24_34)
        self.add_arc('flower-2-top', p_34_18, p_42_18, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('flower-2-bottom', p_42_18, p_34_18, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('stem-2', p_38_22, p_38_34)
        self.add_line('planter-0', p_6_34, p_10_34)
        self.add_line('planter-1', p_10_34, p_24_34)
        self.add_line('planter-2', p_24_34, p_38_34)
        self.add_line('planter-3', p_38_34, p_42_34)
        self.add_line('planter-4', p_42_34, p_38_42)
        self.add_line('planter-5', p_38_42, p_10_42)
        self.add_line('planter-6', p_10_42, p_6_34)
        self.add_contour('flower-0', 'flower-0-top', 'flower-0-bottom', closed=True)
        self.add_contour('flower-1', 'flower-1-top', 'flower-1-bottom', closed=True)
        self.add_contour('flower-2', 'flower-2-top', 'flower-2-bottom', closed=True)
        self.add_contour('planter', 'planter-0', 'planter-1', 'planter-2', 'planter-3', 'planter-4', 'planter-5', 'planter-6', closed=True)
        self.relate('connect', 'flower-0', 'stem-0')
        self.relate('connect', 'stem-0', 'planter')
        self.relate('connect', 'flower-1', 'stem-1')
        self.relate('connect', 'stem-1', 'planter')
        self.relate('connect', 'flower-2', 'stem-2')
        self.relate('connect', 'stem-2', 'planter')
