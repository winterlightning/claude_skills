"""Arrow Dashed Rising Curve with Open Gaps. Wide envelope; three rising runs and shared tip. Wider interruptions than the close-tip source preserve the named distinction. Reduce five dashes to three; head mirrors around x=36.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '962df00e-8b8f-4536-9900-5bd0d171a1ea'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram dash steady up large head_962df00e-8b8f-4536-9900-5bd0d171a1ea.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-dashed-rising-curve-with-open-gaps'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Dashed Upward Trend Arrow',)
    keywords = ('arrow', 'dashed', 'up', 'curve', 'trend', 'direction', 'path')

    def build(self):
        self.add_line('base',(4,40),(10,40))
        self.add_bezier('middle',(21,37),((24,36),(27,34),(29,31)))
        tip=(36,8)
        self.add_bezier('terminal',(35,21),((36,17),(36,12),tip))
        self.add_polyline('head',(28,16),tip,(44,16))
        self.relate('connect','terminal','head')
