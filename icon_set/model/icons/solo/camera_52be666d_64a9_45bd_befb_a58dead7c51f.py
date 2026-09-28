"""Front camera with raised housing and centered lens; Lucide camera informs rounded body and lens axis."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '52be666d-64a9-45bd-befb-a58dead7c51f'
SOURCE_PATH = 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'
AUTHOR = 'gpt-6'

class Camera(Solo48):
    icon_id = 'camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    categories = ('video', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('camera', 'photography', 'lens', 'photo', 'device', 'optics', 'snapshot')

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        ids = []
        for i, a in enumerate(pts):
            b = pts[(i + 1) % 8]
            ident = name + '-' + str(i)
            ids.append(ident)
            if i % 2:
                self.add_arc(ident, a, b, radius_x=r)
            else:
                self.add_line(ident, a, b)
        self.add_contour(name, *ids, closed=True)

    def build(self):
        # Lucide camera: tangent quarter-circle body corners and a centered lens; raised housing retained.
        self.add_line('housing-1', (8, 14), (12, 14))
        self.add_line('housing-2', (12, 14), (18, 8))
        self.add_line('housing-3', (18, 8), (30, 8))
        self.add_line('housing-4', (30, 8), (36, 14))
        self.add_line('housing-5', (36, 14), (40, 14))
        self.add_arc('tr', (40, 14), (44, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_line('right', (44, 18), (44, 36))
        self.add_arc('br', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (40, 40), (8, 40))
        self.add_arc('bl', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (4, 36), (4, 18))
        self.add_arc('tl', (4, 18), (8, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('body', 'housing-1', 'housing-2', 'housing-3', 'housing-4', 'housing-5', 'tr', 'right', 'br', 'bottom', 'bl', 'left', 'tl', closed=True)
        self.add_arc('lens-a', (18, 25), (30, 25), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('lens-b', (30, 25), (18, 25), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('lens', 'lens-a', 'lens-b', closed=True)
