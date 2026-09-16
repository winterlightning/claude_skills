"""Fitted Tank Top.

Plan: Deep U neck between wide straps; mirrored curved armholes and fitted sides above a shallow hem ellipse. Extremes (8,4)-(40,44).
Reduction: Shoulder straps widened for clear openings; deep neckline, fitted waist and curved hem retained.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '369f3a54-01a1-5544-a5a5-6efe159659e2'
SOURCE_PATH = 'pictographic-primitives/clothes/tank top female_369f3a54-01a1-5544-a5a5-6efe159659e2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('369f3a54-01a1-5544-a5a5-6efe159659e2', 'pictographic-primitives/clothes/tank top female_369f3a54-01a1-5544-a5a5-6efe159659e2.svg'),)

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


class FittedTankTop(Solo48):
    icon_id = 'fitted-tank-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('fitted', 'tank', 'top')

    def build(self):
        axis=24
        self.add_arc('neck',(16,4),(32,4),radius_x=8,radius_y=12,sweep=False)
        for side in (-1,1):
            def p(x,y):return (axis+side*x,y)
            self.add_line(f'strap-{side}',p(8,4),p(16,4))
            self.add_arc(f'armhole-{side}',p(16,4),p(12,20),radius_x=34,sweep=side==1)
            self.add_arc(f'waist-{side}',p(12,20),p(16,40),radius_x=30,sweep=side==-1)
            self.add_contour(f'side-{side}',f'strap-{side}',f'armhole-{side}',f'waist-{side}')
            self.relate('connect',f'side-{side}','neck')
        self.add_arc('hem',(40,40),(8,40),radius_x=16,radius_y=4)
        for side in (-1,1):self.relate('connect','hem',f'side-{side}')
