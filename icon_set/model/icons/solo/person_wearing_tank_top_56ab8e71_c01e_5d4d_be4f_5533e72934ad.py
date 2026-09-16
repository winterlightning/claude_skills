"""Person Wearing Tank Top.

Plan: Circular detached head above a shoulder bar with exact 8-unit centerline gap; scoop neck and open arm outlines define the sleeveless shirt. Extremes (8,4)-(40,44). Human reference: user.svg and full_body_ref.png.
Reduction: Oval head becomes the required circular human vocabulary; neck detail and finger anatomy omitted while scoop-neck top and bare arms remain.
Construction reference: Lucide shirt and shared human references.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56ab8e71-c01e-5d4d-be4f-5533e72934ad'
SOURCE_PATH = 'pictographic-primitives/clothes/tank top female_56ab8e71-c01e-5d4d-be4f-5533e72934ad.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('56ab8e71-c01e-5d4d-be4f-5533e72934ad', 'pictographic-primitives/clothes/tank top female_56ab8e71-c01e-5d4d-be4f-5533e72934ad.svg'),)

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


class PersonWearingTankTop(Solo48):
    icon_id = 'person-wearing-tank-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('person', 'wearing', 'tank', 'top')

    def build(self):
        axis=24
        _circle(self,'head',axis,10,6)
        self.add_polyline('shoulders',(8,44),(8,28),(16,24),(24,24),(32,24),(40,28),(40,44))
        self.add_polyline('tank',(16,24),(16,44),(32,44),(32,24))
        self.add_arc('scoop',(16,24),(32,24),radius_x=8,sweep=False)
        self.relate('connect','shoulders','tank')
        self.relate('connect','shoulders','scoop')
        self.relate('connect','tank','scoop')
