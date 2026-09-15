"""Fitted Short-Sleeved Collared Shirt.

Plan: Mirrored sleeve and body shapes share neck and hem dimensions; inward waist arcs retain the fitted silhouette. Centerline extremes (4,8)-(44,40).
Reduction: Buttons and small seams removed; folded collar flaps retained. The defining fitted waist and pointed opening remains.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6ff2e30-c7d6-40c0-8f9d-ea9546f757eb'
SOURCE_PATH = 'pictographic-primitives/clothes/shirt female_b6ff2e30-c7d6-40c0-8f9d-ea9546f757eb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b6ff2e30-c7d6-40c0-8f9d-ea9546f757eb', 'pictographic-primitives/clothes/shirt female_b6ff2e30-c7d6-40c0-8f9d-ea9546f757eb.svg'),)

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


class FittedShortSleevedCollaredShirt(Solo48):
    icon_id = 'fitted-short-sleeved-collared-shirt'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('fitted', 'short-sleeved', 'collared', 'shirt')

    def build(self):
        self.add_polyline('left-upper',(16,8),(8,12),(4,28),(12,28))
        self.add_arc('left-waist',(12,28),(12,38),radius_x=3,radius_y=5)
        self.add_arc('hem',(12,38),(36,38),radius_x=12,radius_y=2,sweep=False)
        self.add_arc('right-waist',(36,38),(36,28),radius_x=3,radius_y=5)
        self.add_polyline('right-upper',(36,28),(44,28),(40,12),(32,8))
        self.relate('connect','left-upper','left-waist')
        self.relate('connect','left-waist','hem')
        self.relate('connect','hem','right-waist')
        self.relate('connect','right-waist','right-upper')
        self.add_polyline('neckline',(32,8),(24,20),(16,8))
        self.relate('connect','neckline','left-upper')
        self.relate('connect','neckline','right-upper')
        self.add_polyline('collar-left',(16,8),(12,16),(24,20))
        self.add_polyline('collar-right',(24,20),(36,16),(32,8))
        self.relate('connect','collar-left','neckline')
        self.relate('connect','collar-right','neckline')
        self.relate('connect','collar-left','left-upper')
        self.relate('connect','collar-right','right-upper')
        self.relate('connect','collar-left','collar-right')
