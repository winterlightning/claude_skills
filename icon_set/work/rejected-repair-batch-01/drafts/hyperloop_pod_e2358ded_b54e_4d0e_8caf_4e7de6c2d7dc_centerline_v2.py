"""Replace the pod’s flattened asymmetric nose arcs with exact matching half-ellipse quarters, preserving a smooth tangent at the forward tip.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e2358ded-b54e-4d0e-8caf-4e7de6c2d7dc'
SOURCE_PATH = 'pictographic-primitives/technology/hyperloop_e2358ded-b54e-4d0e-8caf-4e7de6c2d7dc.svg'
AUTHOR = 'gpt-6'

class HyperloopPod(Solo48):
    icon_id = 'hyperloop-pod-centerline-v2'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('hyperloop', 'pod', 'train', 'capsule', 'transport', 'vehicle', 'travel')

    def build(self):

        def line(n, a, b):
            self.add_line(n, a, b)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(n, *p, closed=False):
            self.add_polyline(n, *p, closed=closed)

        def chain(n, *p):
            for i, (a, b) in enumerate(zip(p, p[1:]), 1):
                line(f'{n}-{i}', a, b)

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
        line('roof', (14, 14), (24, 14))
        arc('nose-top', (24, 14), (44, 24), 20, 10)
        arc('nose-bottom', (44, 24), (24, 34), 20, 10)
        line('bottom', (24, 34), (14, 34))
        arc('rear', (14, 34), (14, 14), 10)
        contour('pod', 'roof', 'nose-top', 'nose-bottom', 'bottom', 'rear', closed=True)
        line('side-mark', (13, 24), (16, 24))
        arc('window-curve', (24, 14), (32, 24), 8, 10, sweep=False)
        line('window-bottom', (32, 24), (44, 24))
        contour('window', 'window-curve', 'window-bottom')
        connect('window', 'pod')
    variant_of = 'hyperloop-pod'
    variant_label = 'Batch 01 centerline repair'
