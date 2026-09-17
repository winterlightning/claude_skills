"""Person Holding Balloons.
Plan: Two balloon loops join strings at one held point; a lower-right figure has a circular head above a short torso. Head center (39,27), r=3; neck (39,35), exact 8 centerline / 4 ink gap. Extrema (6,6)-(42,42).
Reference: human_ref/user.svg and full_body_ref.png: circular detached head and simple coherent limbs. Lucide balloon supports the balloon/string construction.
Reduction: Upper-body scene retained; fingers, balloon knots and the reference extraction break omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3465bd9-1061-58e8-8163-98cddd54bdc0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/balloon party_d3465bd9-1061-58e8-8163-98cddd54bdc0.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'person-holding-two-balloons'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/celebrations"
    aliases = ()
    keywords = ('person', 'holding', 'balloons')

    def build(self):

        for i,(x,r) in enumerate(((11,5),(29,4))):
            self.add_arc(f'balloon-{i}-a',(x,6),(x,6+2*r),radius_x=r)
            self.add_arc(f'balloon-{i}-b',(x,6+2*r),(x,6),radius_x=r)
            self.add_contour(f'balloon-{i}',f'balloon-{i}-a',f'balloon-{i}-b',closed=True)
        self.add_bezier('string-left',(11,16),((11,25),(17,28),(23,31)))
        self.add_line('string-right',(29,14),(23,31))
        for i,s in enumerate(('string-left','string-right')):self.relate('connect',f'balloon-{i}',s)
        self.relate('connect','string-left','string-right')
        self.add_arc('head-a',(36,24),(42,24),radius_x=3)
        self.add_arc('head-b',(42,24),(36,24),radius_x=3)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('torso',(39,35),(39,42))
        self.add_polyline('arm',(39,35),(30,35),(23,31))
        self.relate('connect','arm','torso')
        self.relate('connect','arm','string-left')
        self.relate('connect','arm','string-right')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
