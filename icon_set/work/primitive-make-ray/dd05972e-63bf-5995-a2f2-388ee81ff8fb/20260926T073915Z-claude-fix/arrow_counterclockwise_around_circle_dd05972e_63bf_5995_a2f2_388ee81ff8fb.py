"""Arrow Counterclockwise around Circle.

Plan: Circular 20-unit centerline radius about (24,24), open quarter at the arrowhead. Direction intentionally asymmetric.
Reduction: A single circular run and an open arrowhead preserve direction; duplicate references map here.
Construction reference: Lucide rotate-ccw.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dd05972e-63bf-5995-a2f2-388ee81ff8fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-counterclockwise-around-circle/20260926T073831Z-thuan-mac/reference/rotate back_dd05972e-63bf-5995-a2f2-388ee81ff8fb.svg'
AUTHOR = "claude-opus-5-5"
SOURCE_REFERENCES = (('dd05972e-63bf-5995-a2f2-388ee81ff8fb', 'pictographic-primitives/arrows/rotate back_dd05972e-63bf-5995-a2f2-388ee81ff8fb.svg'), ('0b53a87a-e04b-4e3c-adfd-dcf1fbf284e1', 'pictographic-primitives/arrows/rotate_0b53a87a-e04b-4e3c-adfd-dcf1fbf284e1.svg'), ('f16056b7-da9d-4235-8ea0-1437b5422e2d', 'pictographic-primitives/arrows/rotate_f16056b7-da9d-4235-8ea0-1437b5422e2d.svg'))

def _circle(icon, name, cx, cy, radius):
    left, right = (cx-radius, cy), (cx+radius, cy)
    icon.add_arc(name+'-upper', left, right, radius_x=radius)
    icon.add_arc(name+'-lower', right, left, radius_x=radius)
    icon.add_contour(name, name+'-upper', name+'-lower', closed=True)


def _box(icon, name, left, top, right, bottom, radius, attachments=()):
    # One rounded rectangle owns all corners and cardinal attachment nodes.
    cx, cy = (left+right)//2, (top+bottom)//2
    points = [(cx,top),(right-radius,top),(right,top+radius),
              (right,cy),(right,bottom-radius),(right-radius,bottom),
              (cx,bottom),(left+radius,bottom),(left,bottom-radius),
              (left,cy),(left,top+radius),(left+radius,top),(cx,top)]
    members = []
    for index, (start,end) in enumerate(zip(points,points[1:])):
        if start == end:
            continue
        member = f'{name}-{index}'
        if index in (1,4,7,10):
            icon.add_arc(member, start, end, radius_x=radius)
        else:
            dx,dy=end[0]-start[0],end[1]-start[1]
            inside=[p for p in attachments if (p[0]-start[0])*dy == (p[1]-start[1])*dx
                    and 0 < (p[0]-start[0])*dx+(p[1]-start[1])*dy < dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-start[0])*dx+(p[1]-start[1])*dy)
            nodes=[start]+inside+[end]
            for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
                part=member+f'-split-{j}'
                icon.add_line(part,a,b)
                members.append(part)
            continue
        members.append(member)
    icon.add_contour(name, *members, closed=True)


class ArrowCounterclockwiseAroundCircle(Solo48):
    icon_id = 'arrow-counterclockwise-around-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'counterclockwise', 'around', 'circle')

    def build(self):
        # Revision per review: the arrowhead sits at the top of the circular path. An r15 arc
        # about (24, 24) starts at the 3-4-5 point (36, 15) (mirrored for counter-clockwise) and
        # sweeps the long way round to the top (24, 9); a short straight run carries on to the
        # tip (29, 9) and a 45-degree chevron's arms end at (24, 4), exactly radius 20, and
        # (24, 14).
        self.add_arc('loop', (12, 15), (24, 9), radius_x=15, large_arc=True, sweep=False)
        self.add_line('run', (24, 9), (19, 9))
        self.add_contour('path', 'loop', 'run')
        self.add_polyline('head', (24, 4), (19, 9), (24, 14))
        self.relate('connect', 'path', 'head')
