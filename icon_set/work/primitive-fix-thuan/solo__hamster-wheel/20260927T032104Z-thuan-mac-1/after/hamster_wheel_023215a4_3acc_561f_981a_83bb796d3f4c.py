"""Hamster Wheel.

Plan: Circular wheel radius 15 on an A-frame with exact circle/leg intersection nodes; wide baseline. Upper spokes and hub ring omitted.
Centerline extremes: (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '023215a4-3acc-561f-981a-83bb796d3f4c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hamster-wheel/20260927T032104Z-thuan-mac-1/reference/hamster wheel_023215a4-3acc-561f-981a-83bb796d3f4c.svg'
AUTHOR = "gpt-6"

class HamsterWheel(Solo48):
    icon_id = 'hamster-wheel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('hamster-wheel', 'wheel', 'hamster', 'exercise', 'rodent', 'cage', 'pet')

    def build(self):
        # The original has a hub and spokes inside a wheel on a low stand.
        points = [(24, 4), (39, 19), (33, 31), (24, 34), (15, 31), (9, 19), (24, 4)]
        members = []
        for i, (start, end) in enumerate(zip(points, points[1:])):
            name = f'rim-{i}'
            self.add_arc(name, start, end, radius_x=15)
            members.append(name)
        self.add_contour('wheel', *members, closed=True)
        self.add_arc('hub-upper', (21, 19), (27, 19), radius_x=3)
        self.add_arc('hub-lower', (27, 19), (21, 19), radius_x=3)
        self.add_contour('hub', 'hub-upper', 'hub-lower', closed=True)
        self.add_line('top-spoke', (24, 16), (24, 4))
        self.relate('connect', 'hub', 'top-spoke')
        self.relate('connect', 'wheel', 'top-spoke')
        for name, start, end in ((
            'left-spoke', (21, 19), (9, 19),
        ), (
            'right-spoke', (27, 19), (39, 19),
        ), (
            'bottom-spoke', (24, 22), (24, 34),
        )):
            self.add_line(name, start, end)
            self.relate('connect', 'hub', name)
            self.relate('connect', 'wheel', name)
        self.add_polyline('stand-left', (15, 31), (9, 42), (8, 44))
        self.add_polyline('stand-right', (33, 31), (39, 42), (40, 44))
        self.add_line('base', (8, 44), (40, 44))
        for side in ('stand-left', 'stand-right'):
            self.relate('connect', side, 'wheel')
            self.relate('connect', side, 'base')
