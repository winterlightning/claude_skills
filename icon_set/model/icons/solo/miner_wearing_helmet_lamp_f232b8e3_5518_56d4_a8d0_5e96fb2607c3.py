"""Miner Wearing Helmet Lamp.

Plan: Helmet and circular lower face share a horizontal brim; a circular lamp is centered at x=24. No torso is depicted. Centerline extremes (8,4)-(40,44). Human reference: human_ref/user.svg, circular face vocabulary.
Reduction: The thin helmet band and projecting brim thickness are removed; the lamp and circular blank face remain.
Construction reference: Lucide hard-hat.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f232b8e3-5518-56d4-a8d0-5e96fb2607c3'
SOURCE_PATH = 'pictographic-primitives/construction/safety helmlet mine light_f232b8e3-5518-56d4-a8d0-5e96fb2607c3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f232b8e3-5518-56d4-a8d0-5e96fb2607c3', 'pictographic-primitives/construction/safety helmlet mine light_f232b8e3-5518-56d4-a8d0-5e96fb2607c3.svg'),)

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


class MinerWearingHelmetLamp(Solo48):
    icon_id = 'miner-wearing-helmet-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('miner', 'wearing', 'helmet', 'lamp')

    def build(self):
        axis=24
        self.add_arc('helmet-top',(8,20),(40,20),radius_x=16)
        self.add_line('helmet-right',(40,20),(40,28))
        self.add_line('helmet-left',(8,28),(8,20))
        self.add_contour('outline','helmet-top','helmet-right')
        self.relate('connect','helmet-left','outline')
        self.add_polyline('brim',(8,28),(12,28),(36,28),(40,28))
        self.add_line('face-left',(12,28),(12,32))
        self.add_arc('face-jaw',(12,32),(36,32),radius_x=12,sweep=False)
        self.add_line('face-right',(36,32),(36,28))
        self.add_contour('face','face-left','face-jaw','face-right')
        self.relate('connect','face','brim')
        self.relate('connect','helmet-left','brim')
        self.relate('connect','brim','outline')
        _circle(self,'lamp',axis,16,3)
