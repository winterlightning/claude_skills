"""Plain Crew-Neck T-Shirt.

Plan: Deep circular crew neck, angled sleeve ends and two equal r4 hem corners; all sides mirror x=24. Extremes (4,8)-(44,40).
Reduction: Both references share the same plain crew-neck shirt. Retains deep neck, short angled sleeves and rounded hem.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7', 'pictographic-primitives/clothes/t shirt_5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7.svg'), ('9aa1a37e-7127-4719-8aeb-03b09b01c294', 'pictographic-primitives/clothes/t shirt_9aa1a37e-7127-4719-8aeb-03b09b01c294.svg'))

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


class CrewNeckTShirtWithAngledSleeves(Solo48):
    icon_id = 'crew-neck-t-shirt-with-angled-sleeves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('plain', 'crew-neck', 't-shirt')

    def build(self):
        axis=24
        self.add_arc('neck',(16,8),(32,8),radius_x=8,sweep=False)
        for side in (-1,1):
            def p(x,y):return (axis+side*x,y)
            self.add_polyline(f'upper-{side}',p(8,8),p(14,10),p(20,18),p(14,24),p(12,22),p(12,36))
            self.add_arc(f'hem-{side}',p(12,36),p(8,40),radius_x=4,sweep=side==1)
            self.add_line(f'base-{side}',p(8,40),p(0,40))
            self.relate('connect',f'upper-{side}','neck')
            self.relate('connect',f'upper-{side}',f'hem-{side}')
            self.relate('connect',f'hem-{side}',f'base-{side}')
        self.relate('connect','base--1','base-1')
