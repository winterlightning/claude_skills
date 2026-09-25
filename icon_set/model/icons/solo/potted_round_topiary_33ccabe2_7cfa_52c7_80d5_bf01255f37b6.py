'Topiary: a true round crown, centered trunk and symmetric 8-unit-deep pot.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33ccabe2-7cfa-52c7-80d5-bf01255f37b6'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_33ccabe2-7cfa-52c7-80d5-bf01255f37b6.svg'
AUTHOR = 'gpt-6'


class PottedRoundTopiary(Solo48):
    icon_id = 'potted-round-topiary'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        # Topiary: a true round crown, centered trunk and symmetric 8-unit-deep pot.
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

        c('crown',24,18,14)
        l('trunk',(24,32),(24,36))
        p('pot',(8,36),(14,44),(34,44),(40,36),(8,36))
        link('connect','trunk','crown')
        link('connect','trunk','pot')
