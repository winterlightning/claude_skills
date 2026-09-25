"""Wrapped Scarf with Fringed End.

Plan: Two broad wrap layers form one capsule; a rectangular hanging end has a shared fold line and a regular three-fringe series. Centerline extremes (8,4)-(40,44).
Reduction: Overlapping fabric curves become two broad capsule layers; one lower band and three evenly spaced fringes remain.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5e97e1a-0180-4ff1-98d3-eb0a39cd5639'
SOURCE_PATH = 'pictographic-primitives/clothes/sewing scarf_d5e97e1a-0180-4ff1-98d3-eb0a39cd5639.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d5e97e1a-0180-4ff1-98d3-eb0a39cd5639', 'pictographic-primitives/clothes/sewing scarf_d5e97e1a-0180-4ff1-98d3-eb0a39cd5639.svg'),)

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


class WrappedScarfWithFringedEnd(Solo48):
    icon_id = 'wrapped-scarf-with-fringed-end'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('wrapped', 'scarf', 'with', 'fringed', 'end')

    def build(self):
        _box(self,'wrap',8,4,40,20,8)
        self.add_line('wrap-fold',(8,12),(40,12))
        self.relate('connect','wrap-fold','wrap')
        self.add_polyline('end',(16,20),(16,32),(16,40),(24,40),(32,40),(32,32),(32,20))
        self.relate('connect','end','wrap')
        self.add_line('end-band',(16,32),(32,32))
        self.relate('connect','end-band','end')
        for i,x in enumerate(range(16,33,8)):
            self.add_line(f'fringe-{i}',(x,40),(x,44))
            self.relate('connect',f'fringe-{i}','end')
