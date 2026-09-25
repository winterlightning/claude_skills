"""Apple on Weighing Scale."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deb50b30-8dc9-43c7-9d32-ad3dac6a9642'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/scale apple_deb50b30-8dc9-43c7-9d32-ad3dac6a9642.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apple-weighing-scale'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('apple', 'scale', 'weighing', 'kitchen', 'fruit', 'measurement', 'dial')

    def build(self):
        # Plan: Apple on left platform; round scale dial and support at right. Gauge needle simplified to pivot. Lucide apple for fruit silhouette. Bounds (6,6)-(42,42).
        self.add_arc('dial-top',(24,15),(42,15),radius_x=9)
        self.add_arc('dial-br',(42,15),(33,24),radius_x=9)
        self.add_arc('dial-bl',(33,24),(24,15),radius_x=9)
        self.add_contour('dial','dial-top','dial-br','dial-bl',closed=True)
        self.add_dot('pivot',(33,15))
        self.add_line('post',(33,24),(33,42))
        self.add_polyline('base',(6,42),(12,42),(33,42),(42,42))
        self.relate('connect','post','dial');self.relate('connect','post','base')
        self.add_bezier('apple',(12,24),((8,21),(6,24),(6,28)),((6,32),(9,34),(12,34)),((15,34),(18,32),(18,28)),((18,24),(16,21),(12,24)))
        self.add_contour('fruit','apple',closed=True)
        self.add_bezier('stem',(12,24),((12,20),(13,18),(16,17)))
        self.relate('connect','stem','fruit')
        self.add_polyline('platform',(6,34),(12,34),(22,34))
        self.add_line('pedestal',(12,34),(12,42))
        self.relate('connect','platform','fruit');self.relate('connect','pedestal','platform');self.relate('connect','pedestal','base')
