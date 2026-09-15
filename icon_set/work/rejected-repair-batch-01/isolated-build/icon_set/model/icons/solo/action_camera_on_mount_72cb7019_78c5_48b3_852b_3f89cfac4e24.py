"""Large-lens alternative: enlarge and center the circular lens; remove the adjacent screen mark to keep clearance. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '72cb7019-78c5-48b3-852b-3f89cfac4e24'
SOURCE_PATH = 'pictographic-primitives/photography/go pro_72cb7019-78c5-48b3-852b-3f89cfac4e24.svg'
AUTHOR = 'gpt-6'

class ActionCameraOnMount(Solo48):
    icon_id = 'action-camera-on-mount'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/photography'
    aliases = ()
    keywords = ('action camera', 'gopro', 'camera', 'mount', 'video', 'sports', 'adventure', 'lens')

    def build(self):
        """Symbol plan: Large-lens alternative: enlarge and center the circular lens; remove the adjacent screen mark to keep clearance. Reference: Lucide disc: concentric circular geometry."""

        def line(n, a, b):
            self.add_line(n, a, b)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(n, *p, closed=False):
            self.add_polyline(n, *p, closed=closed)

        def segments(n, *p):
            for j, (a, b) in enumerate(zip(p, p[1:]), 1):
                line(n + '-' + str(j), a, b)

        def contour(n, *m, closed=False):
            self.add_contour(n, *m, closed=closed)

        def connect(a, b):
            self.relate('connect', a, b)

        def circle(n, x, y, r):
            arc(n + '-top', (x - r, y), (x + r, y), r)
            arc(n + '-bottom', (x + r, y), (x - r, y), r)
            contour(n, n + '-top', n + '-bottom', closed=True)
        segments('top', (10, 6), (38, 6))
        arc('tr', (38, 6), (42, 10), 4)
        line('right', (42, 10), (42, 26))
        arc('br', (42, 26), (38, 30), 4)
        segments('bottom', (38, 30), (24, 30), (10, 30))
        arc('bl', (10, 30), (6, 26), 4)
        line('left', (6, 26), (6, 10))
        arc('tl', (6, 10), (10, 6), 4)
        contour('body', 'top-1', 'tr', 'right', 'br', 'bottom-1', 'bottom-2', 'bl', 'left', 'tl', closed=True)
        circle('lens', 24, 18, 3)
        line('post', (24, 30), (24, 42))
        connect('post', 'body')
        poly('foot', (14, 42), (24, 42), (34, 42))
        connect('post', 'foot')
