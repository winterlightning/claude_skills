"""Curved Street Lantern.

Plan: A tall pole bends through a semicircular r10 arch to one hanging lantern; rounded pedestal below. Extremes (8,4)-(40,44).
Reduction: Pedestal and lantern remain; cap seam and lower finial are omitted.
Construction reference: Lucide lamp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70139615-7e04-5ac3-b7af-3298842e82a5'
SOURCE_PATH = 'pictographic-primitives/building/street light_70139615-7e04-5ac3-b7af-3298842e82a5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('70139615-7e04-5ac3-b7af-3298842e82a5', 'pictographic-primitives/building/street light_70139615-7e04-5ac3-b7af-3298842e82a5.svg'),)

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


class CurvedStreetLantern(Solo48):
    icon_id = 'curved-street-lantern'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('curved', 'street', 'lantern')

    def build(self):
        self.add_arc('arch',(16,14),(36,14),radius_x=10)
        self.add_line('pole',(36,14),(36,32))
        self.add_contour('post','arch','pole')
        _box(self,'pedestal',32,32,40,44,4)
        self.relate('connect','post','pedestal')
        self.add_polyline('lantern',(16,14),(8,20),(12,32),(20,32),(24,20),closed=True)
        self.relate('connect','lantern','post')
