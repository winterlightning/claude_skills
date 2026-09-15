'Home-office user: circular head with exact 4-unit shoulder gap, clear laptop and straight house frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265d6a4b-dfe3-4566-af33-cc74f18fb7bc'
SOURCE_PATH = 'pictographic-primitives/office/small office laptop user_265d6a4b-dfe3-4566-af33-cc74f18fb7bc.svg'
AUTHOR = 'gpt-6'

class SmallOfficeLaptopUser(Solo48):
    icon_id = 'small-office-laptop-user'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('small', 'office', 'laptop', 'user')

    def build(self):
        # Home-office user: balanced roof, round head, exact 4-unit shoulder gap and a clear open laptop.
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

        # full_body_ref.png: circular head; bottom 27 to shoulder top 35 gives exactly 4 ink units.
        p('house',(4,40),(4,20),(24,8),(44,20),(44,40))
        c('head',24,23,4)
        a('shoulders',(14,40),(34,40),10,5)
        p('laptop',(4,30),(12,30),(14,40))
        link('connect','laptop','house')
        link('connect','laptop','shoulders')
