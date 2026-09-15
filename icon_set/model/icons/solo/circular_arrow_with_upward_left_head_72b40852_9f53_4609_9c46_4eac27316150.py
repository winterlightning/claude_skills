"""Circular Arrow with Upward Left Head.

Plan: Circular run about (28,24), with an upward tangent stem and broad open head on the left. Centerline extremes (4,8)-(44,40); directional asymmetry preserves the source.
Reduction: Single open arrowhead retains the upward direction and a generous break at upper-left.
Construction reference: Lucide rotate-ccw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72b40852-9f53-4609-9c46-4eac27316150'
SOURCE_PATH = 'pictographic-primitives/arrows/round large head_72b40852-9f53-4609-9c46-4eac27316150.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('72b40852-9f53-4609-9c46-4eac27316150', 'pictographic-primitives/arrows/round large head_72b40852-9f53-4609-9c46-4eac27316150.svg'),)

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


class CircularArrowWithUpwardLeftHead(Solo48):
    icon_id = 'circular-arrow-with-upward-left-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('circular', 'arrow', 'with', 'upward', 'left', 'head')

    def build(self):
        self.add_arc('round-run',(28,8),(12,24),radius_x=16,large_arc=True)
        self.add_line('stem',(12,24),(12,16))
        self.add_contour('loop','round-run','stem')
        self.add_polyline('head',(4,24),(12,16),(20,24))
        self.relate('connect','head','loop')
