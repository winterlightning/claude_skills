"""Balanced Scale with Hanging Pans.

Plan: A common center post and level beam own two identical suspended bowls at x=9 and39. Bowl radii and suspension height are shared. Centerline extremes (4,8)-(44,40).
Reduction: Beam corner rounding reduced to a straight balanced beam; both suspension triangles and curved bowls remain. Three sources share this concept.
Construction reference: Lucide scale.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '098c5b62-8287-467b-95c6-c1b202763219'
SOURCE_PATH = 'pictographic-primitives/business/scale_098c5b62-8287-467b-95c6-c1b202763219.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('098c5b62-8287-467b-95c6-c1b202763219', 'pictographic-primitives/business/scale_098c5b62-8287-467b-95c6-c1b202763219.svg'), ('a443bfb2-9fd7-4e55-96b8-03968dd0394b', 'pictographic-primitives/business/scale_a443bfb2-9fd7-4e55-96b8-03968dd0394b.svg'), ('fcb4406f-0560-4d96-8364-53fb1119bcf0', 'pictographic-primitives/business/scale_fcb4406f-0560-4d96-8364-53fb1119bcf0.svg'))

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


class BalancedScaleWithHangingPans(Solo48):
    icon_id = 'balanced-scale-with-hanging-pans'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('balanced', 'scale', 'with', 'hanging', 'pans')

    def build(self):
        self.add_polyline('post',(24,8),(24,12),(24,40))
        self.add_polyline('beam',(9,12),(24,12),(39,12))
        self.add_polyline('base',(16,40),(24,40),(32,40))
        self.relate('connect','post','beam')
        self.relate('connect','post','base')
        for index,cx in enumerate((9,39)):
            name=f'pan-{index}'
            self.add_line(name+'-right',(cx,12),(cx+5,24))
            self.add_arc(name+'-bowl',(cx+5,24),(cx-5,24),radius_x=5,radius_y=6)
            self.add_line(name+'-left',(cx-5,24),(cx,12))
            self.add_contour(name,name+'-right',name+'-bowl',name+'-left',closed=True)
            self.add_line(name+'-rim',(cx-5,24),(cx+5,24))
            self.relate('connect',name,name+'-rim')
            self.relate('connect',name,'beam')
