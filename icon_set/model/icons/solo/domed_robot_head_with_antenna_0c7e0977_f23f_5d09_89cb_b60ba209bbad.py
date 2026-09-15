"""Domed Robot Head with Antenna.

Plan: Circular dome and lower corner arcs share tangent sidewalls; all paired parts mirror x=24. Centerline extremes (4,8)-(44,40).
Reduction: Round eye holes and ball tip reduced to round marks; ears reduced to rods.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c7e0977-f23f-5d09-89cb-b60ba209bbad'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot head_0c7e0977-f23f-5d09-89cb-b60ba209bbad.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0c7e0977-f23f-5d09-89cb-b60ba209bbad', 'pictographic-primitives/artificial-intelligence/robot head_0c7e0977-f23f-5d09-89cb-b60ba209bbad.svg'),)

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


class DomedRobotHeadWithAntenna(Solo48):
    icon_id = 'domed-robot-head-with-antenna'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('domed', 'robot', 'head', 'with', 'antenna')

    def build(self):
        self.add_arc('crown-left',(10,32),(24,18),radius_x=14)
        self.add_arc('crown-right',(24,18),(38,32),radius_x=14)
        self.add_line('wall-right',(38,32),(38,36))
        self.add_arc('corner-right',(38,36),(34,40),radius_x=4)
        self.add_line('base',(34,40),(14,40))
        self.add_arc('corner-left',(14,40),(10,36),radius_x=4)
        self.add_line('wall-left',(10,36),(10,32))
        self.add_contour('head','crown-left','crown-right','wall-right','corner-right','base','corner-left','wall-left',closed=True)
        for i,x in enumerate((19,29)):
            self.add_dot(f'eye-{i}',(x,31))
        for side,x,end in [('left',10,4),('right',38,44)]:
            self.add_line('ear-'+side,(x,32),(end,32))
            self.relate('connect','ear-'+side,'head')
        self.add_line('antenna',(24,8),(24,18))
        self.relate('connect','antenna','head')
