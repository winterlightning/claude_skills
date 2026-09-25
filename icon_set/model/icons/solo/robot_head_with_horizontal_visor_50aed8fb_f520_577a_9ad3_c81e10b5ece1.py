"""Robot Head with Horizontal Visor.

Plan: Rounded head contains one horizontal capsule visor; antenna at top midpoint. Centerline extremes (6,6)-(42,42).
Reduction: Side ears and small mouth omitted to retain a genuinely open horizontal visor.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50aed8fb-f520-577a-9ad3-c81e10b5ece1'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot head_50aed8fb-f520-577a-9ad3-c81e10b5ece1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50aed8fb-f520-577a-9ad3-c81e10b5ece1', 'pictographic-primitives/artificial-intelligence/robot head_50aed8fb-f520-577a-9ad3-c81e10b5ece1.svg'),)

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


class RobotHeadWithHorizontalVisor(Solo48):
    icon_id = 'robot-head-with-horizontal-visor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'head', 'with', 'horizontal', 'visor')

    def build(self):
        _box(self,'head',6,16,42,42,6)
        _box(self,'visor',15,25,33,33,4)
        self.add_line('antenna',(24,6),(24,16))
        self.relate('connect','antenna','head')
