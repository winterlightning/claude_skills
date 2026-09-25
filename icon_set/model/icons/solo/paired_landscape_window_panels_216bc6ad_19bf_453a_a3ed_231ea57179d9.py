'Paired landscape window panels.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '216bc6ad-19bf-453a-a3ed-231ea57179d9'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-05/windows_216bc6ad-19bf-453a-a3ed-231ea57179d9.svg'
AUTHOR = 'gpt-6'

class PairedLandscapeWindowPanels(Solo48):
    icon_id = 'paired-landscape-window-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('paired', 'landscape', 'window', 'panels')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_31 = (6, 31)
        p_6_6 = (6, 6)
        p_19_6 = (19, 6)
        p_19_25 = (19, 25)
        p_19_42 = (19, 42)
        p_6_42 = (6, 42)
        p_6_19 = (6, 19)
        p_11_19 = (11, 19)
        p_19_19 = (19, 19)
        p_29_31 = (29, 31)
        p_29_6 = (29, 6)
        p_42_6 = (42, 6)
        p_42_25 = (42, 25)
        p_42_42 = (42, 42)
        p_29_42 = (29, 42)
        p_29_19 = (29, 19)
        p_32_19 = (32, 19)
        p_42_19 = (42, 19)
        self.add_line('left-frame-1', p_6_31, p_6_6)
        self.add_line('left-frame-2', p_6_6, p_19_6)
        self.add_line('left-frame-3', p_19_6, p_19_25)
        self.add_line('left-frame-4', p_19_25, p_19_42)
        self.add_line('left-frame-5', p_19_42, p_6_42)
        self.add_line('left-frame-6', p_6_42, p_6_31)
        self.add_arc('left-hill', p_6_31, p_19_25, radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_line('left-cloud-base', p_6_19, p_11_19)
        self.add_arc('left-cloud-dome', p_11_19, p_19_19, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('right-frame-1', p_29_31, p_29_6)
        self.add_line('right-frame-2', p_29_6, p_42_6)
        self.add_line('right-frame-3', p_42_6, p_42_25)
        self.add_line('right-frame-4', p_42_25, p_42_42)
        self.add_line('right-frame-5', p_42_42, p_29_42)
        self.add_line('right-frame-6', p_29_42, p_29_31)
        self.add_arc('right-hill', p_29_31, p_42_25, radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_line('right-cloud-base', p_29_19, p_32_19)
        self.add_arc('right-cloud-dome', p_32_19, p_42_19, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('left-frame', 'left-frame-1', 'left-frame-2', 'left-frame-3', 'left-frame-4', 'left-frame-5', 'left-frame-6', closed=False)
        self.add_contour('left-cloud', 'left-cloud-base', 'left-cloud-dome', closed=False)
        self.add_contour('right-frame', 'right-frame-1', 'right-frame-2', 'right-frame-3', 'right-frame-4', 'right-frame-5', 'right-frame-6', closed=False)
        self.add_contour('right-cloud', 'right-cloud-base', 'right-cloud-dome', closed=False)
        self.relate('connect', 'left-hill', 'left-frame')
        self.relate('connect', 'left-cloud', 'left-frame')
        self.relate('connect', 'right-hill', 'right-frame')
        self.relate('connect', 'right-cloud', 'right-frame')
