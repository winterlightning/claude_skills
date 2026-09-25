"""Arrow Clockwise around Circle.

Plan: Circular 20-unit centerline radius about (24,24), open quarter at the arrowhead. Direction intentionally asymmetric.
Reduction: A single circular run and an open arrowhead preserve direction; duplicate references map here.
Construction reference: Lucide rotate-ccw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f09df4e8-4631-484f-aab2-1ad12c86a6d3'
SOURCE_PATH = 'pictographic-primitives/arrows/rotate forward_f09df4e8-4631-484f-aab2-1ad12c86a6d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f09df4e8-4631-484f-aab2-1ad12c86a6d3', 'pictographic-primitives/arrows/rotate forward_f09df4e8-4631-484f-aab2-1ad12c86a6d3.svg'),)

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


class ArrowClockwiseAroundCircle(Solo48):
    icon_id = 'arrow-clockwise-around-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'clockwise', 'around', 'circle')

    def build(self):
        self.add_arc('loop',(44,24),(36,8),radius_x=20,large_arc=True,sweep=True)
        self.add_polyline('head',(28,8),(36,8),(36,16))
        self.relate('connect','loop','head')
