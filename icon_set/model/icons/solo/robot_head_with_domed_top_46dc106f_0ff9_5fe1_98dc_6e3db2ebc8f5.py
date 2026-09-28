"""Robot Head with Domed Top.

Plan: Rounded head with a semicircular cap as an intrinsic crown, symmetric eye pair and ears. Centerline extremes (4,8)-(44,40).
Reduction: Tiny mouth and circular eye holes removed to keep the domed cap and face readable.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46dc106f-0ff9-5fe1-98dc-6e3db2ebc8f5'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot head_46dc106f-0ff9-5fe1-98dc-6e3db2ebc8f5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('46dc106f-0ff9-5fe1-98dc-6e3db2ebc8f5', 'pictographic-primitives/artificial-intelligence/robot head_46dc106f-0ff9-5fe1-98dc-6e3db2ebc8f5.svg'),)

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


class RobotHeadWithDomedTop(Solo48):
    icon_id = 'robot-head-with-domed-top'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'head', 'with', 'domed', 'top')

    def build(self):
        _box(self,'head',10,16,38,40,4,attachments=((16,16),(32,16)))
        self.add_arc('cap-left',(16,16),(24,8),radius_x=8)
        self.add_arc('cap-right',(24,8),(32,16),radius_x=8)
        self.add_contour('cap','cap-left','cap-right')
        for part in ('cap',):
            self.relate('connect',part,'head')
        for i,x in enumerate((19,29)):
            self.add_dot(f'eye-{i}',(x,28))
        for side,x,end in [('left',10,4),('right',38,44)]:
            self.add_line('ear-'+side,(x,28),(end,28))
            self.relate('connect','ear-'+side,'head')
