"""Independent lightning-bolt component from the supplied split brief. Shared center16; Lucide plus/zap construction; original lightning is an open zigzag."""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8b71e7e7-15cf-4d31-8c76-295ef5576f53'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/07-wrench-with-lightning-bolt/reference.svg'
AUTHOR = 'gpt-6'
class Drawing(Sub32):
    icon_id = 'lightning-bolt-batch-04'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('lightning', 'bolt')
    def build(self):
        self.add_polyline('bolt',(30,2),(2,16),(30,16),(2,30))
