"""T-Shirt with Wide Neckband.

Plan: A level inner neck edge and broad semicircular band provide a 12-unit central separation, shared shoulders and mirrored short sleeves. Extremes (4,8)-(44,40).
Reduction: Wide neckband retained with a level inner edge above its broad curved outer edge; sleeves and hem remain simple.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d18c440-3b17-53ef-b7f8-141a77051e35'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_9d18c440-3b17-53ef-b7f8-141a77051e35.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9d18c440-3b17-53ef-b7f8-141a77051e35', 'pictographic-primitives/clothes/t shirt_9d18c440-3b17-53ef-b7f8-141a77051e35.svg'),)

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


class TShirtWithWideNeckband(Solo48):
    icon_id = 't-shirt-with-wide-neckband'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('t-shirt', 'with', 'wide', 'neckband')

    def build(self):
        axis=24
        self.add_line('neck',(12,8),(36,8))
        self.add_arc('band',(12,8),(36,8),radius_x=12,radius_y=12,sweep=False)
        for side in (-1,1):
            def p(x,y):return (axis+side*x,y)
            self.add_polyline(f'body-{side}',p(12,8),p(16,12),p(20,20),p(12,24),p(12,40),p(0,40))
            self.relate('connect',f'body-{side}','neck')
            self.relate('connect',f'body-{side}','band')
        self.relate('connect','body--1','body-1')
