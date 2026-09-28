"""Crossed knitting needles with knob ends above a hanging fabric panel.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: two mirrored 45-degree needles crossing on the axis x=24; each
needle ends at the bottom in a round knob (r3 ring, the reviewer's requested
circle); the fabric panel hangs from the two needles like a house, so the
needles double as its roof. Budget: knob 6 + gap 8 + fabric 12 + gap 8 + knob 6 = 40.
Revision: added the knob circles at the lower needle ends (review feedback) and
moved to HRECT_L so the knobs fit 8 units clear of the fabric walls.
Construction reference: no useful local Lucide subject match; supplied reference governs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '42e0445b-86b9-4a5a-b1c7-898db65d5c28'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-knitting-needles-with-fabric-batch-013-12/20260926T125429Z-thuan-mac/reference/sewing_42e0445b-86b9-4a5a-b1c7-898db65d5c28.svg'
AUTHOR = 'claude-opus-5-5'

AXIS = 24
KNOB_R = 3
KNOB_C = (7, 33)          # left knob centre; right knob mirrored
WALL_X = 18               # left fabric wall; right wall mirrored
WALL_TOP = 25             # on the needle x + y = 43
BOTTOM = 40
TOP = 8


def mx(p):
    return (2 * AXIS - p[0], p[1])


class GeneratedSolo(Solo48):
    icon_id = 'crossed-knitting-needles-with-fabric-batch-013-12'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('knitting', 'needles', 'fabric', 'craft', 'textile', 'sewing')

    def ring(self, name, c, r):
        cx, cy = c
        e, s, w, n = (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)
        self.add_arc(f'{name}-1', e, s, radius_x=r, sweep=True)
        self.add_arc(f'{name}-2', s, w, radius_x=r, sweep=True)
        self.add_arc(f'{name}-3', w, n, radius_x=r, sweep=True)
        self.add_arc(f'{name}-4', n, e, radius_x=r, sweep=True)
        self.add_contour(name, f'{name}-1', f'{name}-2', f'{name}-3', f'{name}-4', closed=True)
        return e

    def build(self):
        attach_l = self.ring('knob-left', KNOB_C, KNOB_R)            # (10, 33)
        attach_r = mx(attach_l)                                      # (38, 33)
        self.ring('knob-right', mx(KNOB_C), KNOB_R)
        wall_l, wall_r = (WALL_X, WALL_TOP), mx((WALL_X, WALL_TOP))
        top_l_end = (WALL_X + (WALL_TOP - TOP), TOP)                 # (35, 8)
        # needle from the left knob up to the right: x + y = 43
        self.add_line('needle-a-low', attach_l, wall_l)
        self.add_line('needle-a-high', wall_l, top_l_end)
        self.add_contour('needle-a', 'needle-a-low', 'needle-a-high')
        self.add_line('needle-b-low', attach_r, wall_r)
        self.add_line('needle-b-high', wall_r, mx(top_l_end))
        self.add_contour('needle-b', 'needle-b-low', 'needle-b-high')
        self.relate("connect", 'needle-a-high', 'needle-b-high')
        self.relate("connect", 'needle-a-low', 'knob-left-1')
        self.relate("connect", 'needle-b-low', 'knob-right-3')
        self.add_polyline('fabric', wall_l, (WALL_X, BOTTOM), mx((WALL_X, BOTTOM)), wall_r)
        self.relate("connect", 'fabric-1', 'needle-a-low')
        self.relate("connect", 'fabric-1', 'needle-a-high')
        self.relate("connect", 'fabric-3', 'needle-b-low')
        self.relate("connect", 'fabric-3', 'needle-b-high')
