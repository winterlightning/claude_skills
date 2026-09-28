"""Crawdad (crayfish) seen from above.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: mirrored about x=24. A long body 10 wide (x 19..29) has a
rounded head (r5 about (24,17)) and one abdomen segment line at y=28; a fan
tail flares from the body's end (y=36) to y=44. Each side carries an arm
from (19,18) to the wrist (10,15) ending in an open pincer of two fingers
(30 degrees apart) reaching the top edge, and two walking legs from the body
at y=26 and y=34, 8 apart.
Revision: the earlier short body with balloon-like oval claws read as a
robot; the long segmented body, open pincers and fan tail now read as a
crayfish.
Omissions: antennae, eyes, the third leg pair and the tail-fan lobes.
Construction reference: no useful local Lucide match (`shrimp` checked for
segmentation only).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f4812ef0-fce6-4380-9124-384916ee103d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crawdad/20260926T125429Z-thuan-mac/reference/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg'
AUTHOR = "claude-opus-5-5"

AXIS = 24
HALF_W = 5
HEAD_Y = 17            # head arc centre; head top at 12
ARM_Y, LEG_YS, BODY_END = 18, (26, 34), 36
SEGMENT_Y = 28
WRIST = (10, 15)
FINGER_OUT, FINGER_IN = (8, 4), (14, 4)
LEG_ENDS = ((10, 28), (10, 38))
FAN_HALF = 8
TAIL_Y = 44


def mx(p):
    return (2 * AXIS - p[0], p[1])


class Drawing(Solo48):
    icon_id = 'crawdad'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('crayfish', 'crawfish')
    keywords = ('crawdad', 'crayfish', 'crawfish', 'lobster', 'seafood', 'claws', 'animal')

    def build(self):
        xl = AXIS - HALF_W
        nodes_l = [(xl, HEAD_Y), (xl, ARM_Y), (xl, LEG_YS[0]), (xl, LEG_YS[1]), (xl, BODY_END)]
        # body outline: head arc, right side down, end line, left side up
        self.add_arc('head', nodes_l[0], mx(nodes_l[0]), radius_x=HALF_W, sweep=True)
        right = [mx(p) for p in nodes_l]
        members = ['head']
        for i in range(len(right) - 1):
            self.add_line(f'side-right-{i}', right[i], right[i + 1])
            members.append(f'side-right-{i}')
        self.add_line('body-end', right[-1], nodes_l[-1])
        members.append('body-end')
        for i in range(len(nodes_l) - 1, 0, -1):
            self.add_line(f'side-left-{i - 1}', nodes_l[i], nodes_l[i - 1])
            members.append(f'side-left-{i - 1}')
        self.add_contour('body', *members, closed=True)
        # abdomen segment
        self.add_line('segment', (xl, SEGMENT_Y), mx((xl, SEGMENT_Y)))
        self.relate('connect', 'segment', 'side-left-2')
        self.relate('connect', 'segment', 'side-right-2')
        # tail fan hanging from the body end
        self.add_polyline('tail', nodes_l[-1], (AXIS - FAN_HALF, TAIL_Y), (AXIS + FAN_HALF, TAIL_Y), right[-1])
        self.relate('connect', 'tail-1', 'body-end'); self.relate('connect', 'tail-1', 'side-left-3')
        self.relate('connect', 'tail-3', 'body-end'); self.relate('connect', 'tail-3', 'side-right-3')
        # arms, pincers and legs, mirrored
        for side, f in (('left', lambda p: p), ('right', mx)):
            s = 'left' if side == 'left' else 'right'
            self.add_line(f'{s}-arm', f(nodes_l[1]), f(WRIST))
            self.relate('connect', f'{s}-arm', f'side-{s}-0'); self.relate('connect', f'{s}-arm', f'side-{s}-1')
            self.add_line(f'{s}-finger-out', f(WRIST), f(FINGER_OUT))
            self.add_line(f'{s}-finger-in', f(WRIST), f(FINGER_IN))
            for finger in ('out', 'in'):
                self.relate('connect', f'{s}-finger-{finger}', f'{s}-arm')
            self.relate('connect', f'{s}-finger-out', f'{s}-finger-in')
            for k, (node, end) in enumerate(zip(nodes_l[2:4], LEG_ENDS)):
                self.add_line(f'{s}-leg-{k}', f(node), f(end))
                self.relate('connect', f'{s}-leg-{k}', f'side-{s}-{k + 1}')
                self.relate('connect', f'{s}-leg-{k}', f'side-{s}-{k + 2}')
