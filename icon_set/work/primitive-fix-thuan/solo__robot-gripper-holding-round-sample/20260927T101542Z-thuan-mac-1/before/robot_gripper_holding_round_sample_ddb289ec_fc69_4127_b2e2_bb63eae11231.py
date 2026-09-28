"""Robot Gripper Holding Round Sample.

Plan: Circular sample nested in an open U gripper; central handle attaches at bottom midpoint. Symmetric jaws about x=24. Centerline extremes (8,4)-(40,44).
Reduction: Probe lines and double handle walls removed; open rounded jaws and circular sample carry the subject.
Construction reference: Lucide robot-arm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddb289ec-fc69-4127-b2e2-bb63eae11231'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot hand science experiment_ddb289ec-fc69-4127-b2e2-bb63eae11231.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ddb289ec-fc69-4127-b2e2-bb63eae11231', 'pictographic-primitives/artificial-intelligence/robot hand science experiment_ddb289ec-fc69-4127-b2e2-bb63eae11231.svg'),)

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


class RobotGripperHoldingRoundSample(Solo48):
    icon_id = 'robot-gripper-holding-round-sample'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'gripper', 'holding', 'round', 'sample')

    def build(self):
        _circle(self,'sample',24,10,6)
        self.add_line('jaw-left',(8,12),(8,20))
        self.add_arc('grip-left',(8,20),(24,36),radius_x=16,sweep=False)
        self.add_arc('grip-right',(24,36),(40,20),radius_x=16,sweep=False)
        self.add_line('jaw-right',(40,20),(40,12))
        self.add_contour('gripper','jaw-left','grip-left','grip-right','jaw-right')
        self.add_line('handle',(24,36),(24,44))
        self.relate('connect','gripper','handle')
