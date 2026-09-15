"""Partly Lowered Roller Shade.

Plan: Rounded cylindrical rail above partial rectangular fabric; long left cord. Centerline extremes (6,6)-(42,42).
Reduction: Teardrop pull weight reduced to round cord end; cylindrical end indicated by the rail radius.
Construction reference: Lucide blinds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25578102-c356-4f32-b572-9117fb24fd6b'
SOURCE_PATH = 'pictographic-primitives/building/roller shade open_25578102-c356-4f32-b572-9117fb24fd6b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('25578102-c356-4f32-b572-9117fb24fd6b', 'pictographic-primitives/building/roller shade open_25578102-c356-4f32-b572-9117fb24fd6b.svg'),)

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


class PartlyLoweredRollerShade(Solo48):
    icon_id = 'partly-lowered-roller-shade'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('partly', 'lowered', 'roller', 'shade')

    def build(self):
        _box(self,'roll',6,6,42,14,4,attachments=((18,14),))
        self.add_polyline('fabric',(18,14),(18,30),(38,30),(38,14))
        self.relate('connect','fabric','roll')
        self.add_line('cord',(10,14),(10,42))
        self.relate('connect','cord','roll')
