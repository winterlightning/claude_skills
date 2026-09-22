"""Arrow Dashed Rising Curve with Close Tip. Wide envelope (4,8)-(44,40); rising curve uses three runs with tangent horizontal base and upward terminal. Reduce five source dashes to three to maintain clearance; symmetric 8-unit arrowhead arms.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '29bc6a39-fbf3-41a5-a99e-727e5271d5bb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram dash fast up_29bc6a39-fbf3-41a5-a99e-727e5271d5bb.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-dashed-rising-curve-with-close-tip'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Curved Upward Dashed Arrow',)
    keywords = ('arrow', 'dashed', 'up', 'curve', 'path', 'direction', 'pointer')

    def build(self):
        self.add_line('base',(4,40),(11,40))
        self.add_bezier('middle',(20,37),((24,36),(27,34),(29,31)))
        tip=(36,8)
        self.add_bezier('terminal',(34,23),((35,18),(36,13),tip))
        self.add_polyline('head',(28,16),tip,(44,16))
        self.relate('connect','terminal','head')
