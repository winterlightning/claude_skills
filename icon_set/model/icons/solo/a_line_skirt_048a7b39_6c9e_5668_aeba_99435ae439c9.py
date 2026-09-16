"""A-Line Skirt.

Plan: Symmetric trapezoid with a broad lower half ellipse and horizontal waistband. Extremes (4,8)-(44,40).
Reduction: One clean waistband and curved hem preserve the plain A-line silhouette.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '048a7b39-6c9e-5668-aeba-99435ae439c9'
SOURCE_PATH = 'pictographic-primitives/clothes/skirt_048a7b39-6c9e-5668-aeba-99435ae439c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('048a7b39-6c9e-5668-aeba-99435ae439c9', 'pictographic-primitives/clothes/skirt_048a7b39-6c9e-5668-aeba-99435ae439c9.svg'),)

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


class ALineSkirt(Solo48):
    icon_id = 'a-line-skirt'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('a-line', 'skirt')

    def build(self):
        self.add_polyline('upper',(4,36),(12,16),(14,8),(34,8),(36,16),(44,36))
        self.add_arc('hem',(44,36),(4,36),radius_x=20,radius_y=4)
        self.relate('connect','upper','hem')
        self.add_line('waistband',(12,16),(36,16))
        self.relate('connect','waistband','upper')
