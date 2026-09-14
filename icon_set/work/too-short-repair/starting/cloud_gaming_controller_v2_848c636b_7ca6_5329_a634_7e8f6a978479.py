# Variant of cloud-gaming-controller; parent file remains unchanged.
"""Cloud Gaming Controller Connected, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '848c636b-7ca6-5329-a634-7e8f6a978479'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/cloud gamimg service joystick connected_848c636b-7ca6-5329-a634-7e8f6a978479.svg'
AUTHOR = 'gpt-6'

class CloudGamingControllerVariant2(Solo48):
    icon_id = 'cloud-gaming-controller-v2'
    variant_of = 'cloud-gaming-controller'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('cloud gaming', 'cloud', 'gamepad', 'controller', 'connected', 'streaming', 'online', 'game')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name + '-a', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(name + '-b', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(name, name + '-a', name + '-b', closed=True)

        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(name, *pts):
            for i, (a, b) in enumerate(zip(pts, pts[1:]), 1):
                self.add_line(f'{name}-{i}', a, b)
        arc('cloud-left', (16, 22), (16, 10), 6)
        arc('cloud-top', (16, 10), (32, 10), 8, 6)
        arc('cloud-right', (32, 10), (32, 22), 6)
        poly('cloud-base', (32, 22), (24, 22), (16, 22))
        self.add_contour('cloud', 'cloud-left', 'cloud-top', 'cloud-right', 'cloud-base-1', 'cloud-base-2', closed=True)
        self.add_line('link', (24, 22), (24, 31))
        self.relate('connect', 'link', 'cloud')
        self.add_polyline('controller', (24, 31), (35, 31), (40, 42), (31, 42), (27, 39), (21, 39), (17, 42), (8, 42), (13, 31), (24, 31), closed=True)
        self.relate('connect', 'link', 'controller')
