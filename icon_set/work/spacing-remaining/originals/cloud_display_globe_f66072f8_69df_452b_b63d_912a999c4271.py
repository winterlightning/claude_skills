'Cloud globe: a true circular globe around one smooth, balanced cloud; the cramped base is omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f66072f8-69df-452b-b63d-912a999c4271'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/sphere_f66072f8-69df-452b-b63d-912a999c4271.svg'
AUTHOR = 'gpt-6'


class CloudDisplayGlobe(Solo48):
    icon_id = 'cloud-display-globe'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('globe', 'cloud', 'sphere', 'pedestal', 'display', 'ornament', 'decor')

    def build(self):
        # Cloud globe: a true circular globe around one smooth, balanced cloud; the cramped base is omitted.
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

        c('globe',24,24,20)
        a('cloud-left',(18,29),(18,19),5)
        a('cloud-crown',(18,19),(30,19),6)
        a('cloud-right',(30,19),(30,29),5)
        l('cloud-bottom',(30,29),(18,29))
        self.add_contour('cloud','cloud-left','cloud-crown','cloud-right','cloud-bottom',closed=True)
