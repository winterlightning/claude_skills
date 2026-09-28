"""Arrow Dashed Counterclockwise Circle. Circle radial envelope; broken loop uses four separated curved dashes and a tangent right-pointing terminal. Reduce seven source dashes to five runs to preserve negative space; terminal shares one tip.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '86ee206a-80e8-4959-a6ec-c45dd3bfc655'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram dash circle_86ee206a-80e8-4959-a6ec-c45dd3bfc655.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-dashed-counterclockwise-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Dashed Circular Arrow',)
    keywords = ('arrow', 'circle', 'dashed', 'loop', 'rotation', 'path', 'direction')

    def build(self):
        self.add_bezier('upper-left',(9,14),((10,11),(12,8),(14,7)))
        self.add_bezier('top',(24,4),((28,4),(32,6),(35,9)))
        self.add_bezier('right',(40,20),((40,23),(39,26),(38,28)))
        self.add_bezier('lower-left',(8,24),((9,28),(11,31),(14,33)))
        tip=(32,36)
        self.add_line('tail',(24,36),tip)
        self.add_polyline('head',(24,28),tip,(24,44))
        self.relate('connect','tail','head')
