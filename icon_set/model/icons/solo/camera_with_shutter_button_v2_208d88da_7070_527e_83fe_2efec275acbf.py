# Variant of camera-with-shutter-button; parent file remains unchanged.
"""Camera with a raised shutter control and centered lens; secondary lens ring omitted; Lucide camera informs rounded body and lens axis."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '208d88da-7070-527e-83fe-2efec275acbf'
SOURCE_PATH = 'pictographic-primitives/video/camera small_208d88da-7070-527e-83fe-2efec275acbf.svg'
AUTHOR = 'gpt-6'

class CameraWithShutterButtonVariant2(Solo48):
    icon_id = 'camera-with-shutter-button-v2'
    variant_of = 'camera-with-shutter-button'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('camera', 'photography', 'lens', 'shutter', 'photo', 'device', 'optics')

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
        self.add_polyline('housing', (8, 14), (12, 14), (18, 8), (30, 8), (36, 14), (40, 14), closed=False)
        self.add_arc('tr', (40, 14), (44, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_line('right', (44, 18), (44, 36))
        self.add_arc('br', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (40, 40), (8, 40))
        self.add_arc('bl', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (4, 36), (4, 18))
        self.add_arc('tl', (4, 18), (8, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('body', 'housing-1', 'housing-2', 'housing-3', 'housing-4', 'housing-5', 'tr', 'right', 'br', 'bottom', 'bl', 'left', 'tl', closed=True)
        self.add_arc('lens-a', (18, 26), (30, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('lens-b', (30, 26), (18, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('lens', 'lens-a', 'lens-b', closed=True)
        self.add_line('shutter', (8, 14), (8, 8))
        self.relate("connect", 'shutter', 'body')
