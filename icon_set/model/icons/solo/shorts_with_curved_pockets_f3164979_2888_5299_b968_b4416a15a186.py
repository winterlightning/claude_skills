"""Shorts with Curved Pockets.

Plan: Two matching quarter-circle pockets share waistband attachment nodes; fly on x=24. Extremes (6,6)-(42,42).
Reduction: Keeps both curved pockets, waistband and fly; leg openings use simple angled inner hems.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3164979-2888-5299-b968-b4416a15a186'
SOURCE_PATH = 'pictographic-primitives/clothes/shorts_f3164979-2888-5299-b968-b4416a15a186.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f3164979-2888-5299-b968-b4416a15a186', 'pictographic-primitives/clothes/shorts_f3164979-2888-5299-b968-b4416a15a186.svg'),)

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


class ShortsWithCurvedPockets(Solo48):
    icon_id = 'shorts-with-curved-pockets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('shorts', 'with', 'curved', 'pockets')

    def build(self):
        self.add_polyline('outline',(6,6),(42,6),(42,14),(42,24),(42,42),(30,42),(24,32),(18,42),(6,42),(6,24),(6,14),closed=True)
        self.add_polyline('waistband',(6,14),(16,14),(24,14),(32,14),(42,14))
        self.relate('connect','waistband','outline')
        self.add_arc('pocket-left',(16,14),(6,24),radius_x=10)
        self.add_arc('pocket-right',(42,24),(32,14),radius_x=10)
        for name in ('pocket-left','pocket-right'):
            self.relate('connect',name,'outline')
            self.relate('connect',name,'waistband')
        self.add_line('fly',(24,14),(24,24))
        self.relate('connect','fly','waistband')
