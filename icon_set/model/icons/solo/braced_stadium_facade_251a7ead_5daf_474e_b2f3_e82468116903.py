"""Braced Stadium Facade.

Plan: Broad roof and dome above repeated triangular braces and sloping walls. Extremes (4,8)-(44,40).
Reduction: Overhead decoration removed; dome, roof and repeating structural braces retained.
Construction reference: Lucide landmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '251a7ead-5daf-474e-b2f3-e82468116903'
SOURCE_PATH = 'pictographic-primitives/building/stadium 2_251a7ead-5daf-474e-b2f3-e82468116903.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('251a7ead-5daf-474e-b2f3-e82468116903', 'pictographic-primitives/building/stadium 2_251a7ead-5daf-474e-b2f3-e82468116903.svg'),)

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


class BracedStadiumFacade(Solo48):
    icon_id = 'braced-stadium-facade'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('braced', 'stadium', 'facade')

    def build(self):
        self.add_polyline('roof',(4,24),(8,16),(16,16),(32,16),(40,16),(44,24),(32,24),(16,24),closed=True)
        self.add_arc('dome',(16,16),(32,16),radius_x=8)
        self.relate('connect','dome','roof')
        self.add_polyline('walls',(4,24),(8,40),(24,40),(40,40),(44,24))
        self.add_polyline('braces',(8,40),(16,24),(24,40),(32,24),(40,40))
        self.relate('connect','walls','roof')
        self.relate('connect','braces','roof')
        self.relate('connect','braces','walls')
