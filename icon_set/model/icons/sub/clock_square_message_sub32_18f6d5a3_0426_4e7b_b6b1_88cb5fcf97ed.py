"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed'
SOURCE_PATH = 'pictographic-primitives/symbol/chat time clock_18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square speech bubble', 'lower-left tail', 'complete clock circle', 'vertical upward hand and horizontal right hand')

class Drawing(Sub32):
    icon_id = 'clock-square-message-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    keywords = ('chat', 'bubble', 'with', 'clock')


    def build(self):
        self.message()
        self.circle('clock',16,14,7)
        self.add_polyline('hands',(16,12),(16,15),(18,15))

    def message(self):
        self.add_line('frame-top',(4,2),(28,2))
        self.add_arc('frame-tr',(28,2),(30,4),radius_x=2)
        self.add_line('frame-right',(30,4),(30,23))
        self.add_arc('frame-br',(30,23),(28,25),radius_x=2)
        tail=[(28,25),(15,25),(9,30),(9,25),(4,25)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1):self.add_line(f'frame-tail-{i}',a,b)
        self.add_arc('frame-bl',(4,25),(2,23),radius_x=2)
        self.add_line('frame-left',(2,23),(2,4))
        self.add_arc('frame-tl',(2,4),(4,2),radius_x=2)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br',*[f'frame-tail-{i}' for i in range(1,5)],'frame-bl','frame-left','frame-tl',closed=True)

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

