"""Winding Down Arrow.

Plan: One coherent winding route uses matching r4 tangent turns and a downward head. Extremes (8,4)-(40,44).
Reduction: The alternating rounded turns and broad down arrow are retained.
Construction reference: Lucide route.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9155c66d-56ff-42df-81ae-5f5ecee14eb0'
SOURCE_PATH = 'pictographic-primitives/arrows/snake arrow large head_9155c66d-56ff-42df-81ae-5f5ecee14eb0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9155c66d-56ff-42df-81ae-5f5ecee14eb0', 'pictographic-primitives/arrows/snake arrow large head_9155c66d-56ff-42df-81ae-5f5ecee14eb0.svg'),)

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


class ArrowDownWinding(Solo48):
    icon_id = 'arrow-down-winding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('winding', 'down', 'arrow')

    def build(self):
        self.add_arc('entry',(24,4),(28,8),radius_x=4,sweep=False)
        self.add_line('run-top',(28,8),(36,8))
        self.add_arc('turn-right',(36,8),(36,16),radius_x=4)
        self.add_line('run-middle',(36,16),(12,16))
        self.add_arc('turn-left',(12,16),(12,24),radius_x=4,sweep=False)
        self.add_line('run-bottom',(12,24),(20,24))
        self.add_arc('exit',(20,24),(24,28),radius_x=4)
        self.add_line('stem',(24,28),(24,44))
        self.add_contour('route','entry','run-top','turn-right','run-middle','turn-left','run-bottom','exit','stem')
        self.add_polyline('head',(16,36),(24,44),(32,36))
        self.relate('connect','head','route')
