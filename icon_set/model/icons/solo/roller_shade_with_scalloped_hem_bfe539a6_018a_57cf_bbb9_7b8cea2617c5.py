"""Roller Shade with Scalloped Hem.

Plan: Broad fabric body with two smooth equal scallops; centered pull cord from their junction. Centerline extremes (6,6)-(42,42).
Reduction: Outer window frame and small pull weight omitted to emphasize fabric, scalloped hem, and central cord.
Construction reference: Lucide blinds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfe539a6-018a-57cf-bbb9-7b8cea2617c5'
SOURCE_PATH = 'pictographic-primitives/building/roller shade closed_bfe539a6-018a-57cf-bbb9-7b8cea2617c5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfe539a6-018a-57cf-bbb9-7b8cea2617c5', 'pictographic-primitives/building/roller shade closed_bfe539a6-018a-57cf-bbb9-7b8cea2617c5.svg'),)

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


class RollerShadeWithScallopedHem(Solo48):
    icon_id = 'roller-shade-with-scalloped-hem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('roller', 'shade', 'with', 'scalloped', 'hem')

    def build(self):
        for i,(a,b) in enumerate(zip([(6,24),(6,6),(42,6)],[(6,6),(42,6),(42,24)]),1):
            self.add_line(f'upper-{i}',a,b)
        self.add_arc('hem-right',(42,24),(24,24),radius_x=9,radius_y=4)
        self.add_arc('hem-left',(24,24),(6,24),radius_x=9,radius_y=4)
        self.add_contour('shade','upper-1','upper-2','upper-3','hem-right','hem-left',closed=True)
        self.add_line('cord',(24,24),(24,42))
        self.relate('connect','cord','shade')
