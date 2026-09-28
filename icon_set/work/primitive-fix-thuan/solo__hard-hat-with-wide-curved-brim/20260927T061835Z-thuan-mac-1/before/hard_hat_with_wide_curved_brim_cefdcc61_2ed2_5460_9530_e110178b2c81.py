"""Hard Hat with Wide Curved Brim.

Plan: Symmetric circular crown, single central ridge, broad half-ellipse brim. Centerline extremes (4,8)-(44,40).
Reduction: Raised ridge becomes a single central rib; the wide curved brim is retained.
Construction reference: Lucide hard-hat.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cefdcc61-2ed2-5460-9530-e110178b2c81'
SOURCE_PATH = 'pictographic-primitives/construction/safety helmet mine_cefdcc61-2ed2-5460-9530-e110178b2c81.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cefdcc61-2ed2-5460-9530-e110178b2c81', 'pictographic-primitives/construction/safety helmet mine_cefdcc61-2ed2-5460-9530-e110178b2c81.svg'),)

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


class HardHatWithWideCurvedBrim(Solo48):
    icon_id = 'hard-hat-with-wide-curved-brim'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('hard', 'hat', 'with', 'wide', 'curved', 'brim')

    def build(self):
        axis=24
        self.add_arc('crown-left',(8,24),(axis,8),radius_x=16)
        self.add_arc('crown-right',(axis,8),(40,24),radius_x=16)
        self.add_line('side-left',(8,28),(8,24))
        self.add_line('side-right',(40,24),(40,28))
        self.add_contour('shell','side-left','crown-left','crown-right','side-right')
        self.add_polyline('brim-top',(4,28),(8,28),(40,28),(44,28))
        self.add_arc('brim-bottom',(44,28),(4,28),radius_x=20,radius_y=12)
        self.relate('connect','shell','brim-top')
        self.relate('connect','brim-top','brim-bottom')
        self.add_line('ridge',(axis,8),(axis,20))
        self.relate('connect','ridge','shell')
