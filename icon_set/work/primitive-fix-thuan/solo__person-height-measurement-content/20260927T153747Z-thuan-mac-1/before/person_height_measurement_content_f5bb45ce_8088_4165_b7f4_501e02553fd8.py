"""Person Height Measurement.
Symbol plan: Ruler with evenly spaced ticks alongside a symmetric stick figure; head radius 5, neck y24, exact 4-unit head/body ink gap. Bounds (4,4)-(44,44).
Construction: Lucide battery for tangent rounded rectangles; shared human reference for people.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle
SOURCE_ICON_ID = 'f5bb45ce-8088-4165-b7f4-501e02553fd8'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f5bb45ce-8088-4165-b7f4-501e02553fd8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-height-measurement-content'
    keyshape = Keyshape.SQUARE
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('person height measurement',)
    def build(self):
        self.add_line('ruler',(6,6),(6,42))
        for i,y in enumerate((6,18,30,42)):
            self.add_line(f'tick-{i}',(6,y),(12,y))
            self.relate('connect','ruler',f'tick-{i}')
        circle(self,'head',32,11,5)
        self.add_line('torso',(32,24),(32,32))
        self.add_polyline('arms',(22,24),(32,24),(42,24))
        self.add_polyline('legs',(24,42),(32,32),(40,42))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
