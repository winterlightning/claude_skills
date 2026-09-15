"""Robot Head with Twin Antennae.

Plan: Flat top and bowl-shaped lower corners; paired antennae and vertical eyes share x=16,32. Centerline extremes (6,6)-(42,42).
Reduction: Preserves both long antennae and simple vertical eyes; no additional decoration.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c1610b9-bbb1-4bc2-a858-53d1cdc71603'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8c1610b9-bbb1-4bc2-a858-53d1cdc71603', 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'), ('dbe0f105-1e06-44cc-8dc4-597b67509f96', 'pictographic-primitives/artificial-intelligence/robot_dbe0f105-1e06-44cc-8dc4-597b67509f96.svg'))

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


class RobotHeadWithTwinAntennae(Solo48):
    icon_id = 'robot-head-with-twin-antennae'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'head', 'with', 'twin', 'antennae')

    def build(self):
        for i,(a,b) in enumerate(zip([(6,18),(16,18),(32,18),(42,18)],[(16,18),(32,18),(42,18),(42,28)]),1):
            self.add_line(f'top-{i}',a,b)
        self.add_arc('lower-right',(42,28),(28,42),radius_x=14)
        self.add_line('base',(28,42),(20,42))
        self.add_arc('lower-left',(20,42),(6,28),radius_x=14)
        self.add_line('left',(6,28),(6,18))
        self.add_contour('head','top-1','top-2','top-3','top-4','lower-right','base','lower-left','left',closed=True)
        for i,x in enumerate((16,32)):
            self.add_line(f'antenna-{i}',(x,6),(x,18))
            self.relate('connect',f'antenna-{i}','head')
            self.add_line(f'eye-{i}',(x,27),(x,30))
