"""Coiled French horn.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the coil is a full circle r13 about (19,29) (x 6..32, y 16..42),
split at its 5-12-13 integer points. The bell flares from the coil's upper
right (between the top (19,16) and (31,24)) out to a vertical mouth at x=42
(y 6..22). Across the coil runs the inner tube as a diameter at y=29, and
two valve pistons drop from it to the lower rim at x=14 and x=24 (5-12-13
points), 10 apart.
Revision: the earlier open G-shaped coil lacked the closed coil, the inner
tubing and the valves; these now carry the French horn identity.
Omissions: the valve keys above the tube and the mouthpiece below the coil
(no room 8 clear of the coil).
Construction reference: no useful local Lucide match; supplied reference governs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e0e5259b-1f4e-49b1-b4fe-796abc5994f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__coiled-french-horn/20260926T125429Z-thuan-mac/reference/instrument french horn_e0e5259b-1f4e-49b1-b4fe-796abc5994f0.svg'
AUTHOR = "claude-opus-5-5"

C, R = (19, 29), 13
MOUTH_X, MOUTH_TOP, MOUTH_BOT = 42, 6, 22


class Drawing(Solo48):
    icon_id = 'coiled-french-horn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('french horn', 'horn')
    keywords = ('coiled', 'french', 'horn', 'brass', 'instrument', 'music')

    def build(self):
        cx, cy = C
        top, neck = (cx, cy - R), (cx + 12, cy - 5)            # (19,16), (31,24)
        right, left = (cx + R, cy), (cx - R, cy)               # (32,29), (6,29)
        valve_r, valve_l = (cx + 5, cy + 12), (cx - 5, cy + 12)  # (24,41), (14,41)
        # coil, clockwise from the top
        self.add_arc('coil-1', top, neck, radius_x=R, sweep=True)
        self.add_arc('coil-2', neck, right, radius_x=R, sweep=True)
        self.add_arc('coil-3', right, valve_r, radius_x=R, sweep=True)
        self.add_arc('coil-4', valve_r, valve_l, radius_x=R, sweep=True)
        self.add_arc('coil-5', valve_l, left, radius_x=R, sweep=True)
        self.add_arc('coil-6', left, top, radius_x=R, sweep=True)
        self.add_contour('coil', *(f'coil-{i}' for i in range(1, 7)), closed=True)
        # bell
        self.add_bezier('bell-upper', top, ((29, 16), (37, 13), (MOUTH_X, MOUTH_TOP)))
        self.add_line('bell-mouth', (MOUTH_X, MOUTH_TOP), (MOUTH_X, MOUTH_BOT))
        self.add_bezier('bell-lower', (MOUTH_X, MOUTH_BOT), ((38, 22), (34, 23), neck))
        self.add_contour('bell', 'bell-upper', 'bell-mouth', 'bell-lower')
        self.relate('connect', 'bell-upper', 'coil-1'); self.relate('connect', 'bell-upper', 'coil-6')
        self.relate('connect', 'bell-lower', 'coil-1'); self.relate('connect', 'bell-lower', 'coil-2')
        # inner tube and valve pistons
        tube_nodes = [left, (valve_l[0], cy), (valve_r[0], cy), right]
        for i in range(3):
            self.add_line(f'tube-{i}', tube_nodes[i], tube_nodes[i + 1])
        self.add_contour('tube', 'tube-0', 'tube-1', 'tube-2')
        self.relate('connect', 'tube-0', 'coil-5'); self.relate('connect', 'tube-0', 'coil-6')
        self.relate('connect', 'tube-2', 'coil-2'); self.relate('connect', 'tube-2', 'coil-3')
        for name, bottom, seg, arcs in (('valve-left', valve_l, ('tube-0', 'tube-1'), ('coil-4', 'coil-5')),
                                         ('valve-right', valve_r, ('tube-1', 'tube-2'), ('coil-3', 'coil-4'))):
            self.add_line(name, (bottom[0], cy), bottom)
            for s in seg + arcs:
                self.relate('connect', name, s)
