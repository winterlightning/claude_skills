"""Hair Clipper with Comb Teeth.

Plan: Integrated comb head and rounded handle; five equal teeth share an8-unit step, with one central switch. Centerline extremes (8,4)-(40,44).
Reduction: The tall switch panel becomes one central switch mark; five evenly spaced teeth and the broad cutting head remain.
Construction reference: Lucide scissors (tool simplification; no exact clipper match).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f12e88a-34be-4f4e-afd9-e5ffc62a8530'
SOURCE_PATH = 'pictographic-primitives/beauty/shaving machine_6f12e88a-34be-4f4e-afd9-e5ffc62a8530.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6f12e88a-34be-4f4e-afd9-e5ffc62a8530', 'pictographic-primitives/beauty/shaving machine_6f12e88a-34be-4f4e-afd9-e5ffc62a8530.svg'),)

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


class HairClipperWithCombTeeth(Solo48):
    icon_id = 'hair-clipper-with-comb-teeth'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('hair', 'clipper', 'with', 'comb', 'teeth')

    def build(self):
        self.add_polyline('head-top',(8,12),(16,12),(24,12),(32,12),(40,12))
        self.add_polyline('side-right',(40,12),(40,16),(34,22),(34,34))
        self.add_arc('handle-right',(34,34),(24,44),radius_x=10)
        self.add_arc('handle-left',(24,44),(14,34),radius_x=10)
        self.add_polyline('side-left',(14,34),(14,22),(8,16),(8,12))
        self.relate('connect','head-top','side-right')
        self.relate('connect','head-top','side-left')
        self.relate('connect','side-right','handle-right')
        self.relate('connect','side-left','handle-left')
        self.relate('connect','handle-left','handle-right')
        for i,x in enumerate(range(8,41,8)):
            self.add_line(f'tooth-{i}',(x,4),(x,12))
            self.relate('connect',f'tooth-{i}','head-top')
            if x==8:self.relate('connect',f'tooth-{i}','side-left')
            if x==40:self.relate('connect',f'tooth-{i}','side-right')
        self.add_line('switch',(24,26),(24,32))
