'Three flying birds.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd7a738c-4a9b-4749-ad10-1147ea353f15'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_bd7a738c-4a9b-4749-ad10-1147ea353f15.svg'
AUTHOR = 'gpt-6'

class ThreeFlyingBirds(Solo48):
    icon_id = 'three-flying-birds'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('birds', 'three', 'flying', 'flock', 'doves', 'sky', 'flight', 'group')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_15_20 = (15, 20)
        p_24_6 = (24, 6)
        p_24_18 = (24, 18)
        p_33_32 = (33, 32)
        p_42_18 = (42, 18)
        p_6_28 = (6, 28)
        p_15_42 = (15, 42)
        p_24_28 = (24, 28)
        self.add_arc('wing-left-0', p_6_6, p_15_20, radius_x=9, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('wing-right-0', p_15_20, p_24_6, radius_x=9, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('wing-left-1', p_24_18, p_33_32, radius_x=9, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('wing-right-1', p_33_32, p_42_18, radius_x=9, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('wing-left-2', p_6_28, p_15_42, radius_x=9, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('wing-right-2', p_15_42, p_24_28, radius_x=9, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('bird-0', 'wing-left-0', 'wing-right-0', closed=False)
        self.add_contour('bird-1', 'wing-left-1', 'wing-right-1', closed=False)
        self.add_contour('bird-2', 'wing-left-2', 'wing-right-2', closed=False)
