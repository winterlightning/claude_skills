"""Flared Shorts with Fly.

Plan: Mirrored flared legs around x=24, common 8-unit waistband and angled hems. Extremes (4,8)-(44,40).
Reduction: Retains waistband and flared silhouette; fly shortened to leave an open crotch gap.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54a90eb1-6d5e-55d9-bff7-530f45b3a97b'
SOURCE_PATH = 'pictographic-primitives/clothes/shorts_54a90eb1-6d5e-55d9-bff7-530f45b3a97b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('54a90eb1-6d5e-55d9-bff7-530f45b3a97b', 'pictographic-primitives/clothes/shorts_54a90eb1-6d5e-55d9-bff7-530f45b3a97b.svg'),)

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


class FlaredShortsWithFly(Solo48):
    icon_id = 'flared-shorts-with-fly'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('flared', 'shorts', 'with', 'fly')

    def build(self):
        self.add_polyline('outline',(10,8),(38,8),(38,16),(44,36),(30,40),(24,32),(18,40),(4,36),(10,16),closed=True)
        self.add_polyline('waistband',(10,16),(24,16),(38,16))
        self.relate('connect','waistband','outline')
        self.add_line('fly',(24,16),(24,24))
        self.relate('connect','fly','waistband')
