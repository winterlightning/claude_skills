'Adventure car: balanced wheels and cabin, straight window divisions and a clear chassis.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b02948e6-fd8b-5c71-957a-a2dd0f63778b'
SOURCE_PATH = 'pictographic-primitives/transportation/adventure car_b02948e6-fd8b-5c71-957a-a2dd0f63778b.svg'
AUTHOR = 'gpt-6'

class AdventureCar(Solo48):
    icon_id = 'adventure-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('adventure', 'car', 'transportation')

    def build(self):
        # Adventure car: equal circular wheels meet the chassis exactly, with a balanced cabin and clear window.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        p('body',(8,34),(4,34),(4,20),(14,12),(30,12),(34,22),(44,24),(44,34),(42,34))
        l('front',(4,8),(4,20))
        link('connect','front','body')
        p('window',(22,12),(22,22),(34,22))
        link('connect','window','body')
        c('wheel-left',14,34,6)
        c('wheel-right',36,34,6)
        l('chassis',(20,34),(30,34))
        link('connect','chassis','wheel-left')
        link('connect','chassis','wheel-right')
        link('connect','body','wheel-left')
        link('connect','body','wheel-right')
