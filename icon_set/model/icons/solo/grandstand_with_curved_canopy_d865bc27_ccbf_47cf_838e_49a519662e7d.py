"""Grandstand with Curved Canopy.

Plan: Shallow elliptical canopy with exact shared post nodes over a rectangular stand and rounded platform. Extremes (4,8)-(44,40).
Reduction: Keeps the sagging curved canopy, two posts, stand and rounded platform without extra facade seams.
Construction reference: Lucide landmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd865bc27-ccbf-47cf-838e-49a519662e7d'
SOURCE_PATH = 'pictographic-primitives/building/stadium_d865bc27-ccbf-47cf-838e-49a519662e7d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d865bc27-ccbf-47cf-838e-49a519662e7d', 'pictographic-primitives/building/stadium_d865bc27-ccbf-47cf-838e-49a519662e7d.svg'),)

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


class GrandstandWithCurvedCanopy(Solo48):
    icon_id = 'grandstand-with-curved-canopy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('grandstand', 'with', 'curved', 'canopy')

    def build(self):
        _box(self,'platform',4,32,44,40,4)
        self.add_polyline('stand',(8,32),(8,22),(40,22),(40,32))
        self.relate('connect','stand','platform')
        for n,a,b in [(0,(4,8),(8,11)),(1,(8,11),(40,11)),(2,(40,11),(44,8))]:self.add_arc(f'canopy-{n}',a,b,radius_x=20,radius_y=5,sweep=False)
        self.add_contour('canopy','canopy-0','canopy-1','canopy-2')
        for n,x in enumerate((8,40)):
            self.add_line(f'post-{n}',(x,11),(x,22))
            self.relate('connect',f'post-{n}','stand')
            self.relate('connect',f'post-{n}','canopy')
