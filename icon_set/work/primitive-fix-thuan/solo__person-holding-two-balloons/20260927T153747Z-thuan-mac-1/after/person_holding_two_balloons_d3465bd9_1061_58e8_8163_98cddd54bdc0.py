"""Person Holding Balloons.
Plan: Two balloon loops join strings at one held point; a lower-right figure has a circular head above a short torso. Head center (39,27), r=3; neck (39,35), exact 8 centerline / 4 ink gap. Extrema (6,6)-(42,42).
Reference: human_ref/user.svg and full_body_ref.png: circular detached head and simple coherent limbs. Lucide balloon supports the balloon/string construction.
Reduction: Upper-body scene retained; fingers, balloon knots and the reference extraction break omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd3465bd9-1061-58e8-8163-98cddd54bdc0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-holding-two-balloons/20260927T153747Z-thuan-mac-1/reference/balloon party_d3465bd9-1061-58e8-8163-98cddd54bdc0.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'person-holding-two-balloons'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('person', 'holding', 'balloons')

    def build(self):
        # Two unequal balloons rise from the hand of a small seated person.
        for index, (x, radius) in enumerate(((11, 5), (29, 4))):
            top, bottom = (x, 6), (x, 6 + 2 * radius)
            self.add_arc(f'balloon-{index}-a', top, bottom, radius_x=radius)
            self.add_arc(f'balloon-{index}-b', bottom, top, radius_x=radius)
            self.add_contour(f'balloon-{index}', f'balloon-{index}-a', f'balloon-{index}-b', closed=True)
        self.add_bezier('string-left', (11, 16), ((11, 24), (17, 28), (23, 31)))
        self.add_bezier('string-right', (29, 14), ((28, 21), (27, 26), (23, 31)))
        self.relate('connect', 'balloon-0', 'string-left')
        self.relate('connect', 'balloon-1', 'string-right')
        self.relate('connect', 'string-left', 'string-right')
        self.add_arc('head-top', (36, 24), (42, 24), radius_x=3)
        self.add_arc('head-bottom', (42, 24), (36, 24), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso', (39, 35), (42, 42))
        self.add_polyline('arm', (39, 35), (30, 35), (23, 31))
        self.relate('connect', 'arm', 'torso')
        self.relate('connect', 'arm', 'string-left')
        self.relate('connect', 'arm', 'string-right')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
