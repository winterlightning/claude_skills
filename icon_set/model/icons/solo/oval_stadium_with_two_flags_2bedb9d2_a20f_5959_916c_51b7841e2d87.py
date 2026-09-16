"""Oval Stadium with Two Flags.

Plan: Horizontal capsule arena above an outer-wall band, with repeated rectangular pennants. Extremes (4,8)-(44,40).
Reduction: Oval arena simplified to a clean capsule; 2 flags retained as rectangular cloth outlines to keep clear interiors.
Construction reference: Lucide flag and landmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bedb9d2-a20f-5959-916c-51b7841e2d87'
SOURCE_PATH = 'pictographic-primitives/building/stadium classic_2bedb9d2-a20f-5959-916c-51b7841e2d87.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2bedb9d2-a20f-5959-916c-51b7841e2d87', 'pictographic-primitives/building/stadium classic_2bedb9d2-a20f-5959-916c-51b7841e2d87.svg'),)

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


class OvalStadiumWithTwoFlags(Solo48):
    icon_id = 'oval-stadium-with-two-flags'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('oval', 'stadium', 'with', 'two', 'flags')

    def build(self):
        _box(self,'bowl',4,24,44,40,8,attachments=((20,24),))
        self.add_line('band',(4,32),(44,32))
        self.relate('connect','band','bowl')
        for n,x in enumerate((12, 36)):
            y=32 if x==4 else 24
            self.add_polyline(f'flag-{n}',(x,y),(x,16),(x,8),(x+8,8),(x+8,16),(x,16))
            self.relate('connect',f'flag-{n}','bowl')
            if x==4:self.relate('connect',f'flag-{n}','band')
