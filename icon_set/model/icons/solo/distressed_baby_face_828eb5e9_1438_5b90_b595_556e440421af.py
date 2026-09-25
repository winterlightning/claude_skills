'Distressed baby face.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '828eb5e9-1438-5b90-b595-556e440421af'
SOURCE_PATH = 'pictographic-primitives/babies/colic baby_828eb5e9-1438-5b90-b595-556e440421af.svg'
AUTHOR = 'gpt-6'

class DistressedBabyFace(Solo48):
    icon_id = 'distressed-baby-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('distressed', 'baby', 'face', 'infant', 'nursery')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_20 = (10, 20)
        p_38_20 = (38, 20)
        p_38_28 = (38, 28)
        p_10_28 = (10, 28)
        p_19_21 = (19, 21)
        p_29_21 = (29, 21)
        p_20_32 = (20, 32)
        p_28_32 = (28, 32)
        self.add_arc('crown', p_10_20, p_38_20, radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('ear-right', p_38_20, p_38_28, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('jaw', p_38_28, p_10_28, radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('ear-left', p_10_28, p_10_20, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('eye-left', p_19_21, p_19_21)
        self.add_line('eye-right', p_29_21, p_29_21)
        self.add_arc('frown', p_20_32, p_28_32, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('face', 'crown', 'ear-right', 'jaw', 'ear-left', closed=True)
