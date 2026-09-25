'Single curved hair ending in a rounded root bulb; one open strand joins root at its top. No useful Lucide hair match. Use constant stroke instead of microscopic tapered walls.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '568e5c06-4fee-4be4-bcf3-09ec376c501b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/hair_568e5c06-4fee-4be4-bcf3-09ec376c501b.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'single-hair-with-root-bulb-batch-057'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hair', 'root', 'strand', 'follicle', 'body', 'care')

    def build(self):
        self.add_arc('root-right',(18,28),(18,44),radius_x=8)
        self.add_arc('root-left',(18,44),(18,28),radius_x=8)
        self.add_contour('root','root-right','root-left',closed=True)
        self.add_arc('strand',(18,28),(38,4),radius_x=30,radius_y=32)
        self.relate('connect','strand','root')
