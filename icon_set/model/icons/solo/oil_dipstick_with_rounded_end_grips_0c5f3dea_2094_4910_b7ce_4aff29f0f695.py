"""An upright oil dipstick has two rounded end grips and two rightward level marks. VRECT_M 10..38 x4..44. Source supplies grip-stem-mark construction; no useful Lucide dipstick match. Capsules share width8, height16 and radius4; level marks meet the stem at the grip ends to preserve eight-unit spacing. Both capsules expose their real attachment extrema."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0c5f3dea-2094-4910-b7ce-4aff29f0f695'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/dipstick_0c5f3dea-2094-4910-b7ce-4aff29f0f695.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'oil-dipstick-with-rounded-end-grips'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Oil Dipstick with Rounded End Grips']
    keywords = ['dipstick', 'oil', 'level', 'engine', 'measure', 'stem', 'tool']
    def build(self):
        for name,top in [('upper',4),('lower',28)]:
            self.add_arc(name+'-top-right',(14,top),(18,top+4),radius_x=4)
            self.add_line(name+'-right',(18,top+4),(18,top+12))
            self.add_arc(name+'-bottom-right',(18,top+12),(14,top+16),radius_x=4)
            self.add_arc(name+'-bottom-left',(14,top+16),(10,top+12),radius_x=4)
            self.add_line(name+'-left',(10,top+12),(10,top+4))
            self.add_arc(name+'-top-left',(10,top+4),(14,top),radius_x=4)
            self.add_contour(name,*[name+'-'+part for part in ('top-right','right','bottom-right','bottom-left','left','top-left')],closed=True)
        self.add_line('stem',(14,20),(14,28))
        self.add_line('level-high',(14,20),(38,20))
        self.add_line('level-low',(14,28),(30,28))
        self.relate('connect','upper','stem','level-high')
        self.relate('connect','lower','stem','level-low')
