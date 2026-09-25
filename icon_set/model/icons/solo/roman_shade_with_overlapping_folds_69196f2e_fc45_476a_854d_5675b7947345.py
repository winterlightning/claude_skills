"""Roman Shade with Overlapping Folds.

Plan: Top rail owns a left pull cord and two broad slightly tapered fabric tiers. Centerline extremes (6,6)-(42,42).
Reduction: Rounded rail thickness and teardrop weight omitted; two layered trapezoidal fabric folds remain.
Construction reference: Lucide blinds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69196f2e-fc45-476a-854d-5675b7947345'
SOURCE_PATH = 'pictographic-primitives/building/roman shade closed_69196f2e-fc45-476a-854d-5675b7947345.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('69196f2e-fc45-476a-854d-5675b7947345', 'pictographic-primitives/building/roman shade closed_69196f2e-fc45-476a-854d-5675b7947345.svg'),)

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


class RomanShadeWithOverlappingFolds(Solo48):
    icon_id = 'roman-shade-with-overlapping-folds'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('roman', 'shade', 'with', 'overlapping', 'folds')

    def build(self):
        self.add_polyline('rail',(6,6),(8,6),(20,6),(38,6),(42,6))
        self.add_line('cord',(8,6),(8,42))
        self.relate('connect','cord','rail')
        self.add_polyline('upper-fold',(20,6),(18,24),(40,24),(38,6))
        self.relate('connect','upper-fold','rail')
        self.add_polyline('lower-fold',(18,24),(20,42),(38,42),(40,24))
        self.relate('connect','upper-fold','lower-fold')
