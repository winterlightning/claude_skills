"""Robot Bust with Ball Antenna.

Plan: Rounded rectangular robot head with paired eyes, single structural neck, broad shoulder arc; ball antenna uses a compact circular tip. Centerline extremes (8,4)-(40,44).
Reduction: Mouth, ear boxes, and double neck walls removed; ball tip retained as a small circle. Robot is a mechanical bust, not a detached human figure.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fa8e623-6585-5690-b43a-11c168d0469f'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot head_0fa8e623-6585-5690-b43a-11c168d0469f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fa8e623-6585-5690-b43a-11c168d0469f', 'pictographic-primitives/artificial-intelligence/robot head_0fa8e623-6585-5690-b43a-11c168d0469f.svg'),)

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


class RobotBustWithBallAntenna(Solo48):
    icon_id = 'robot-bust-with-ball-antenna'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'bust', 'with', 'ball', 'antenna')

    def build(self):
        _box(self,'head',8,16,40,34,4)
        for i,x in enumerate((18,30)):
            self.add_dot(f'eye-{i}',(x,25))
        _circle(self,'ball',24,6,2)
        self.add_line('antenna',(24,8),(24,16))
        self.relate('connect','ball','antenna')
        self.relate('connect','antenna','head')
        self.add_line('neck',(24,34),(24,42))
        self.add_arc('shoulder-left',(8,44),(24,42),radius_x=16,radius_y=2)
        self.add_arc('shoulder-right',(24,42),(40,44),radius_x=16,radius_y=2)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','neck','head')
        self.relate('connect','neck','shoulders')
