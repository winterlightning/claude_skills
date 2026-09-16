"""Round Table Mirror.

Plan: Round mirror inside a broad U cradle, with axis-aligned stem and long base. Extremes (8,4)-(40,44).
Reduction: Mirror frame thickness removed; circular glass, U cradle and tabletop base remain.
Construction reference: Lucide circle-dot and lamp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92c57e8e-ef7f-45f1-9076-c7df797cbaa7'
SOURCE_PATH = 'pictographic-primitives/beauty/table mirror_92c57e8e-ef7f-45f1-9076-c7df797cbaa7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('92c57e8e-ef7f-45f1-9076-c7df797cbaa7', 'pictographic-primitives/beauty/table mirror_92c57e8e-ef7f-45f1-9076-c7df797cbaa7.svg'),)

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


class RoundTableMirror(Solo48):
    icon_id = 'round-table-mirror'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('round', 'table', 'mirror')

    def build(self):
        _circle(self,'mirror',24,12,8)
        self.add_line('cradle-left',(8,16),(8,20))
        self.add_arc('cradle-curve-left',(8,20),(24,36),radius_x=16,sweep=False)
        self.add_arc('cradle-curve-right',(24,36),(40,20),radius_x=16,sweep=False)
        self.add_line('cradle-right',(40,20),(40,16))
        self.add_contour('cradle','cradle-left','cradle-curve-left','cradle-curve-right','cradle-right')
        self.add_line('stem',(24,36),(24,44))
        self.add_polyline('base',(8,44),(24,44),(40,44))
        self.relate('connect','stem','cradle')
        self.relate('connect','stem','base')
