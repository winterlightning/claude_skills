"""Archery Target on Feet.

Plan: Circular target with an open upper-right quadrant, mirrored feet and diagonal arrow; plain target face. Extremes (6,6)-(42,42).
Reduction: Arrow tail simplified to two clean feather strokes; both matching references share the same plain target.
Construction reference: Lucide target.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a13fefa-dc3f-4a87-a280-cc766a52f462'
SOURCE_PATH = 'pictographic-primitives/business/target center_7a13fefa-dc3f-4a87-a280-cc766a52f462.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7a13fefa-dc3f-4a87-a280-cc766a52f462', 'pictographic-primitives/business/target center_7a13fefa-dc3f-4a87-a280-cc766a52f462.svg'), ('95837240-8ef3-49ed-a3f0-513c4f947fe2', 'pictographic-primitives/business/target center_95837240-8ef3-49ed-a3f0-513c4f947fe2.svg'))

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


class ArcheryTargetOnFeet(Solo48):
    icon_id = 'archery-target-on-feet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('archery', 'target', 'on', 'feet')

    def build(self):
        # Target center (21,24), r15; integer 3-4-5 points anchor both feet.
        self.add_arc('rim-top',(6,24),(21,9),radius_x=15)
        self.add_arc('rim-bottom-left',(12,36),(6,24),radius_x=15)
        self.add_arc('rim-bottom',(30,36),(12,36),radius_x=15)
        self.add_arc('rim-right',(36,24),(30,36),radius_x=15)
        self.add_contour('rim','rim-right','rim-bottom','rim-bottom-left','rim-top')
        for n,(a,b) in enumerate([((12,36),(6,42)),((30,36),(36,42))]):
            self.add_line(f'foot-{n}',a,b)
            self.relate('connect',f'foot-{n}','rim')
        self.add_polyline('shaft',(21,24),(33,12),(39,6))
        self.add_polyline('feather',(33,6),(33,12),(42,12))
        self.relate('connect','shaft','feather')
