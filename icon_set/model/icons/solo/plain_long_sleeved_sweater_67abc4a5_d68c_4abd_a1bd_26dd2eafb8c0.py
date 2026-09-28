"""Plain Long-Sleeved Sweater.

Plan: Shared x=24 axis generates long sleeves and body; a shallow elliptical crew neck preserves upper-front space. Extremes (4,8)-(44,40).
Reduction: Thin cuff bands simplify to clean stepped sleeve ends; short underarm seams separate the long sleeves; the broad unmarked front remains plain.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67abc4a5-d68c-4abd-a1bd-26dd2eafb8c0'
SOURCE_PATH = 'pictographic-primitives/clothes/sweater_67abc4a5-d68c-4abd-a1bd-26dd2eafb8c0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('67abc4a5-d68c-4abd-a1bd-26dd2eafb8c0', 'pictographic-primitives/clothes/sweater_67abc4a5-d68c-4abd-a1bd-26dd2eafb8c0.svg'),)

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


class PlainLongSleevedSweater(Solo48):
    icon_id = 'plain-long-sleeved-sweater'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('plain', 'long-sleeved', 'sweater')

    def build(self):
        axis=24
        self.add_arc('neck',(16,8),(32,8),radius_x=8,radius_y=5,sweep=False)
        for side in (-1,1):
            def p(x,y):return (axis+side*x,y)
            self.add_line(f'shoulder-{side}',p(8,8),p(12,8))
            self.add_arc(f'round-{side}',p(12,8),p(20,16),radius_x=8,sweep=side==1)
            pts=[p(20,16),p(20,32),p(10,32),p(10,40),p(0,40)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'edge-{side}-{i}',a,b)
            self.add_contour(f'side-{side}',f'shoulder-{side}',f'round-{side}',*[f'edge-{side}-{i}' for i in range(4)])
            self.add_line(f'underarm-{side}',p(10,24),p(10,32))
            self.relate('connect',f'underarm-{side}',f'side-{side}')
            self.relate('connect',f'side-{side}','neck')
        self.relate('connect','side--1','side-1')
