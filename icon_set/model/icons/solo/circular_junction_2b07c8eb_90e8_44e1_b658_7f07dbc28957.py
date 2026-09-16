"""Circular Junction.

Plan: One circular node and three branch levels; matching quarter turns own the upper/lower runs. Extremes (4,8)-(44,40).
Reduction: Preserves all three connections and the round junction, with even branch spacing.
Construction reference: Lucide circle-dot and network.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b07c8eb-90e8-44e1-b658-7f07dbc28957'
SOURCE_PATH = 'pictographic-primitives/construction/straight cap_2b07c8eb-90e8-44e1-b658-7f07dbc28957.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b07c8eb-90e8-44e1-b658-7f07dbc28957', 'pictographic-primitives/construction/straight cap_2b07c8eb-90e8-44e1-b658-7f07dbc28957.svg'),)

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


class CircularJunction(Solo48):
    icon_id = 'circular-junction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('circular', 'junction')

    def build(self):
        pts=[(4,24),(12,16),(20,24),(12,32)]
        for i,a in enumerate(pts):self.add_arc(f'node-{i}',a,pts[(i+1)%4],radius_x=8)
        self.add_contour('node',*[f'node-{i}' for i in range(4)],closed=True)
        self.add_arc('upper-turn',(12,16),(20,8),radius_x=8)
        self.add_line('upper-run',(20,8),(44,8))
        self.add_contour('upper','upper-turn','upper-run')
        self.add_arc('lower-turn',(12,32),(20,40),radius_x=8,sweep=False)
        self.add_line('lower-run',(20,40),(44,40))
        self.add_contour('lower','lower-turn','lower-run')
        self.add_line('middle',(20,24),(44,24))
        for name in ('upper','middle','lower'):self.relate('connect',name,'node')
