"""Arrow Broken Rise Turning Right. Wide envelope; three disjoint sections retain two bends and rightward head. Shared bend axis x=16 and terminal y=16; omit excess vertical length for clearance.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '4fc35558-7baa-4b75-8a5d-192b22a56d71'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram dash up steady large head_4fc35558-7baa-4b75-8a5d-192b22a56d71.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-broken-rise-turning-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Dashed Up and Right Curved Arrow',)
    keywords = ('arrow', 'broken', 'right', 'up', 'curve', 'path', 'direction')

    def build(self):
        self.add_arc('lower-bend',(4,40),(16,28),radius_x=12,sweep=False)
        self.add_bezier('upper-bend',(16,19),((16,16),(22,16),(27,16)))
        tip=(44,16)
        self.add_line('terminal',(36,16),tip)
        self.add_polyline('head',(36,8),tip,(36,24))
        self.relate('connect','terminal','head')
