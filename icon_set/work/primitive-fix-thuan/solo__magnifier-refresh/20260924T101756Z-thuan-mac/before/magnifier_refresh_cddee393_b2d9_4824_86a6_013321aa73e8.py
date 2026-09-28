"""Magnifier with Circular Arrows.

Plan: Two circular arrow runs define a lens with a lower-right handle attached to an exact circle point. Direction is intentionally asymmetric. Centerline extremes (8,4)-(40,44).
Reduction: The two breaks are opened up to separate the arrowheads clearly; the lens itself remains the circular-arrow construction.
Construction reference: Lucide search and rotate-ccw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cddee393-b2d9-4824-86a6-013321aa73e8'
SOURCE_PATH = 'pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cddee393-b2d9-4824-86a6-013321aa73e8', 'pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg'),)

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


class MagnifierRefresh(Solo48):
    icon_id = 'magnifier-refresh'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('magnifier', 'with', 'circular', 'arrows')

    def build(self):
        self.add_arc('right-loop',(23,4),(32,31),radius_x=15)
        self.add_polyline('right-head',(40,31),(32,31),(32,23))
        self.relate('connect','right-loop','right-head')
        self.add_arc('left-loop',(23,34),(8,19),radius_x=15)
        self.add_polyline('left-head',(16,27),(8,19),(16,19))
        self.relate('connect','left-loop','left-head')
        self.add_line('handle',(32,31),(40,44))
        self.relate('connect','handle','right-loop')
        self.relate('connect','handle','right-head')
