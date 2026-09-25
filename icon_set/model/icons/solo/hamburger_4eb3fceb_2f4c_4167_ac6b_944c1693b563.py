"""hamburger: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eb3fceb-2f4c-4167-ac6b-944c1693b563'
SOURCE_PATH = 'pictographic-primitives/symbol/hamburger_4eb3fceb-2f4c-4167-ac6b-944c1693b563.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Hamburger(Solo48):
    icon_id = 'hamburger'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('hamburger', 'symbol')

    def build(self):
        # Plan: HRECT_L; circular paired bun corners, smooth filling ends and shared dividers; retain wavy versus plain filling.
        # Reference: Geometric mirrored bun and repeated wave.
        self.add_arc('bun-left',(8,20),(20,8),radius_x=12)
        self.add_line('bun-top',(20,8),(28,8))
        self.add_arc('bun-right',(28,8),(40,20),radius_x=12)
        self.add_bezier('filling-right',(40,20),((42,20),(44,22),(44,25)),((44,28),(42,30),(40,30)))
        self.add_arc('base-right',(40,30),(30,40),radius_x=10)
        self.add_line('base',(30,40),(18,40))
        self.add_arc('base-left',(18,40),(8,30),radius_x=10)
        self.add_bezier('filling-left',(8,30),((6,30),(4,28),(4,25)),((4,22),(6,20),(8,20)))
        self.add_contour('outline','bun-left','bun-top','bun-right','filling-right','base-right','base','base-left','filling-left',closed=True)
        self.add_line('lower-divider',(8,30),(40,30))
        self.relate('connect','lower-divider','outline')

        self.add_bezier('upper-divider',(8,20),((11,22),(13,22),(16,20)),((19,18),(21,18),(24,20)),((27,22),(29,22),(32,20)),((35,18),(37,18),(40,20)))
        self.relate('connect','upper-divider','outline')
