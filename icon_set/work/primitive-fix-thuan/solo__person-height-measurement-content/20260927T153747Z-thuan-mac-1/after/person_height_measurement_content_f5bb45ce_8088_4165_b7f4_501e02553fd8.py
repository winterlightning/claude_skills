"""Person Height Measurement.
Symbol plan: Ruler with evenly spaced ticks alongside a symmetric stick figure; head radius 5, neck y24, exact 4-unit head/body ink gap. Bounds (4,4)-(44,44).
Construction: Lucide battery for tangent rounded rectangles; shared human reference for people.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f5bb45ce-8088-4165-b7f4-501e02553fd8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-height-measurement-content/20260927T153747Z-thuan-mac-1/reference/person with ruler_f5bb45ce-8088-4165-b7f4-501e02553fd8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-height-measurement-content'
    keyshape = Keyshape.SQUARE
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('person height measurement',)
    def build(self):
        # Ruler with three graduations beside a rounded shoulder bust.
        self.add_line('ruler', (6, 6), (6, 42))
        for index, y in enumerate((12, 24, 36)):
            self.add_line(f'tick-{index}', (6, y), (12, y))
            self.relate('connect', 'ruler', f'tick-{index}')
        self.add_arc('head-upper', (27, 11), (37, 11), radius_x=5)
        self.add_arc('head-lower', (37, 11), (27, 11), radius_x=5)
        self.add_contour('head', 'head-upper', 'head-lower', closed=True)
        self.add_polyline('body', (22, 42), (22, 30), (26, 24), (38, 24), (42, 30), (42, 42), closed=True)
