"""Hand Holding Open-End Wrench.

Plan: Open-end tool above a simplified wrapped hand, with a single grip crease. Upright tool owns the shared hand attachment. Centerline extremes (8,4)-(40,44). Human construction references reviewed; Lucide hand-grab supplies rounded hand vocabulary.
Reduction: Individual finger divisions and the small handle end are omitted to keep a clear wrapped grip and open jaw.
Construction reference: Lucide hand-grab and wrench.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69fd62d6-2807-4c9b-9e1a-35e009d9fd9f'
SOURCE_PATH = 'pictographic-primitives/business/self service wrench_69fd62d6-2807-4c9b-9e1a-35e009d9fd9f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('69fd62d6-2807-4c9b-9e1a-35e009d9fd9f', 'pictographic-primitives/business/self service wrench_69fd62d6-2807-4c9b-9e1a-35e009d9fd9f.svg'),)

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


class HandHoldingOpenEndWrench(Solo48):
    icon_id = 'hand-holding-open-end-wrench'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('hand', 'holding', 'open-end', 'wrench')

    def build(self):
        self.add_polyline('jaw',(22,4),(22,12),(30,12),(30,4))
        self.add_arc('tool-right',(30,4),(34,20),radius_x=12)
        self.add_line('shaft-right',(34,20),(34,28))
        points=[(8,34),(14,32),(20,24),(24,24),(24,28),(34,28)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'hand-top-{i}',a,b)
        self.add_arc('fingers',(34,28),(34,44),radius_x=6,radius_y=8)
        points=[(34,44),(20,44),(14,42),(8,44)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'hand-bottom-{i}',a,b)
        self.add_contour('hand','hand-top-1','hand-top-2','hand-top-3','hand-top-4','hand-top-5','fingers','hand-bottom-1','hand-bottom-2','hand-bottom-3')
        self.add_arc('tool-left',(18,20),(22,4),radius_x=12)
        self.add_line('shaft-left',(18,20),(20,24))
        self.relate('connect','jaw','tool-right')
        self.relate('connect','jaw','tool-left')
        self.relate('connect','tool-right','shaft-right')
        self.relate('connect','tool-left','shaft-left')
        self.relate('connect','shaft-right','hand')
        self.relate('connect','shaft-left','hand')
