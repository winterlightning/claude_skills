"""Worker Pushing Loaded Hand Truck.

Plan: Circular head and upright upper torso share x=36 and an exact 8-unit detached head gap. The extended arm meets the tilted truck at its package edge. Extremes (4,8)-(44,40). Human reference: full_body_ref.png.
Reduction: Figure becomes a clear walking stick figure with one visible pushing arm; loaded tilted trolley and wheel remain.
Construction reference: Lucide package.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a22e440-feef-587a-ba12-555c427f3d8d'
SOURCE_PATH = 'pictographic-primitives/business/supply chain supplier trolley delivery_1a22e440-feef-587a-ba12-555c427f3d8d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a22e440-feef-587a-ba12-555c427f3d8d', 'pictographic-primitives/business/supply chain supplier trolley delivery_1a22e440-feef-587a-ba12-555c427f3d8d.svg'),)

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


class WorkerPushingLoadedHandTruck(Solo48):
    icon_id = 'worker-pushing-loaded-hand-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('worker', 'pushing', 'loaded', 'hand', 'truck')

    def build(self):
        _circle(self,'head',36,12,4)
        self.add_line('torso',(36,24),(36,32))
        self.add_polyline('legs',(28,40),(36,32),(44,40))
        self.relate('connect','torso','legs')
        self.add_polyline('arm',(36,24),(28,24),(20,22))
        self.relate('connect','arm','torso')
        self.add_polyline('package',(8,18),(20,22),(18,28),(16,34),(4,30),closed=True)
        self.add_polyline('truck',(24,18),(20,22),(18,28),(16,34),(14,36))
        self.relate('connect','package','truck')
        self.relate('connect','arm','truck')
        self.relate('connect','arm','package')
        pts=[(12,38),(14,36),(16,38),(14,40)]
        for i,a in enumerate(pts):self.add_arc(f'wheel-{i}',a,pts[(i+1)%4],radius_x=2)
        self.add_contour('wheel',*[f'wheel-{i}' for i in range(4)],closed=True)
        self.relate('connect','wheel','truck')
        self.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
