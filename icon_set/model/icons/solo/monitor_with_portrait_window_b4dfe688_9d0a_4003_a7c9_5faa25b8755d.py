"""Monitor showing a portrait application window. Portrait envelope provides room for the upright inner window and detached baseline; Lucide smartphone rounded UI shapes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4dfe688-9d0a-4003-a7c9-5faa25b8755d'
SOURCE_PATH = 'pictographic-primitives/technology/element presentation_b4dfe688-9d0a-4003-a7c9-5faa25b8755d.svg'
AUTHOR = 'gpt-6'

class MonitorWithPortraitWindow(Solo48):
    icon_id = 'monitor-with-portrait-window'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('monitor', 'screen', 'presentation', 'window', 'display', 'interface', 'element')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.

        def line(n, a, b):
            self.add_line(n, a, b)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(n, *p, closed=False):
            self.add_polyline(n, *p, closed=closed)

        def contour(n, *m, closed=False):
            self.add_contour(n, *m, closed=closed)

        def connect(a, b):
            self.relate('connect', a, b)

        def circle(n, x, y, r):
            arc(n + 'a', (x, y - r), (x, y + r), r)
            arc(n + 'b', (x, y + r), (x, y - r), r)
            contour(n, n + 'a', n + 'b', closed=True)

        def box(n, l, t, r, b, rad=4):
            line(n + 't', (l + rad, t), (r - rad, t))
            arc(n + 'tr', (r - rad, t), (r, t + rad), rad)
            line(n + 'r', (r, t + rad), (r, b - rad))
            arc(n + 'br', (r, b - rad), (r - rad, b), rad)
            line(n + 'b', (r - rad, b), (l + rad, b))
            arc(n + 'bl', (l + rad, b), (l, b - rad), rad)
            line(n + 'l', (l, b - rad), (l, t + rad))
            arc(n + 'tl', (l, t + rad), (l + rad, t), rad)
            contour(n, *[n + s for s in ('t', 'tr', 'r', 'br', 'b', 'bl', 'l', 'tl')], closed=True)
        box('screen', 8, 4, 40, 35, 4)
        box('portrait', 19, 13, 29, 26, 2)
        line('base', (16, 44), (32, 44))
