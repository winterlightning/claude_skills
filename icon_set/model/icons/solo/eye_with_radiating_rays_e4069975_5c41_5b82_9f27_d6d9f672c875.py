"""Eye with Radiating Rays.

Plan: Two equal circular arcs form an almond around one pupil; six mirrored rays are generated around x=24 and y=24. Centerline extremes (6,6)-(42,42).
Reduction: The nested iris ring is removed; one round pupil and all six rays remain.
Construction reference: Lucide eye.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4069975-5c41-5b82-9f27-d6d9f672c875'
SOURCE_PATH = 'pictographic-primitives/business/seo eye_e4069975-5c41-5b82-9f27-d6d9f672c875.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e4069975-5c41-5b82-9f27-d6d9f672c875', 'pictographic-primitives/business/seo eye_e4069975-5c41-5b82-9f27-d6d9f672c875.svg'),)

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


class EyeWithRadiatingRays(Solo48):
    icon_id = 'eye-with-radiating-rays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('eye', 'with', 'radiating', 'rays')

    def build(self):
        self.add_arc('lid-top',(6,24),(42,24),radius_x=24)
        self.add_arc('lid-bottom',(42,24),(6,24),radius_x=24)
        self.add_contour('eye','lid-top','lid-bottom',closed=True)
        self.add_dot('pupil',(24,24))
        for side in (-1,1):
            def point(x,y):return (24+side*x,y)
            for vertical in (-1,1):
                self.add_line(f'ray-{side}-{vertical}',(24+side*16,24+vertical*18),(24+side*12,24+vertical*14))
        for vertical in (-1,1):
            self.add_line(f'center-ray-{vertical}',(24,24+vertical*18),(24,24+vertical*17))
