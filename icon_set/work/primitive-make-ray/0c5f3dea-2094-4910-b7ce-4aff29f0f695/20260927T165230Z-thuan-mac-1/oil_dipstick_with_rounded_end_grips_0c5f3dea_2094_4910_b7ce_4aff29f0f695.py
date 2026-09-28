"""An upright oil dipstick has two rounded end grips and two rightward level marks. VRECT_M 10..38 x4..44. Source supplies grip-stem-mark construction; no useful Lucide dipstick match. Capsules share width8, height16 and radius4; level marks meet the stem at the grip ends to preserve eight-unit spacing. Both capsules expose their real attachment extrema."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '0c5f3dea-2094-4910-b7ce-4aff29f0f695'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__oil-dipstick-with-rounded-end-grips/20260927T164916Z-thuan-mac-1/reference/dipstick_0c5f3dea-2094-4910-b7ce-4aff29f0f695.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'oil-dipstick-with-rounded-end-grips'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Oil Dipstick with Rounded End Grips']
    keywords = ['dipstick', 'oil', 'level', 'engine', 'measure', 'stem', 'tool']
    def build(self):
        # Two rounded grips share one diagonal measuring shaft.
        def grip(name, x, top):
            self.add_arc(name+'-tr',(x,top),(x+4,top+4),radius_x=4)
            self.add_line(name+'-r',(x+4,top+4),(x+4,top+8))
            self.add_arc(name+'-br',(x+4,top+8),(x,top+12),radius_x=4)
            self.add_arc(name+'-bl',(x,top+12),(x-4,top+8),radius_x=4)
            self.add_line(name+'-l',(x-4,top+8),(x-4,top+4))
            self.add_arc(name+'-tl',(x-4,top+4),(x,top),radius_x=4)
            self.add_contour(name,*(name+'-'+part for part in ('tr','r','br','bl','l','tl')),closed=True)
        grip('upper',14,4)
        grip('lower',34,32)
        self.add_line('shaft',(14,16),(34,32))
        self.add_line('measure',(24,24),(30,20))
        self.relate('connect','shaft','upper','lower','measure')
