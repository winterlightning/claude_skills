"""Steel I-Beam in Perspective.

Plan: Two matching receding flange planes around a front web, with explicit corner contacts. Extremes (6,6)-(42,42).
Reduction: Flange thickness and hidden interior edges removed; two receding flange planes and the joining web retain the I-beam profile.
Construction reference: Lucide construction and package.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e859c168-e250-4c14-a90e-b0b07cb0380f'
SOURCE_PATH = 'pictographic-primitives/construction/steal beam_e859c168-e250-4c14-a90e-b0b07cb0380f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e859c168-e250-4c14-a90e-b0b07cb0380f', 'pictographic-primitives/construction/steal beam_e859c168-e250-4c14-a90e-b0b07cb0380f.svg'),)

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


class SteelIBeamInPerspective(Solo48):
    icon_id = 'steel-i-beam-in-perspective'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('steel', 'i-beam', 'in', 'perspective')

    def build(self):
        for n,y in enumerate((18,42)):
            self.add_polyline(f'flange-{n}',(6,y),(18,y-12),(42,y-12),(30,y),(18,y),closed=True)
        self.add_polyline('web',(18,18),(18,30),(18,42))
        for n in range(2):self.relate('connect','web',f'flange-{n}')
        self.add_line('far-edge',(42,6),(42,30))
        for n in range(2):self.relate('connect','far-edge',f'flange-{n}')
