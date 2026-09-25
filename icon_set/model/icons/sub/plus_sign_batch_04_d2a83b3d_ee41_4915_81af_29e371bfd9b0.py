"""Independent plus-sign component from the supplied split brief. Shared center16; Lucide plus/zap construction; original lightning is an open zigzag."""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd2a83b3d-ee41-4915-81af-29e371bfd9b0'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/08-zoom-in-magnifying-glass/reference.svg'
AUTHOR = 'gpt-6'
class Drawing(Sub32):
    icon_id = 'plus-sign-batch-04'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('plus', 'sign')
    def build(self):
        for name,end in [('left',(2,16)),('right',(30,16)),('top',(16,2)),('bottom',(16,30))]:
            self.add_line(name,(16,16),end)
        self.relate('connect','left','right','top','bottom')
