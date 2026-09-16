"""Fruit and Carton Cycle.

Plan: Fruit and folded carton occupy opposite corners; two equal r10 curved arrows describe a process between them. Extremes (6,6)-(42,42).
Reduction: Fruit leaf, carton lip and internal fold seam omitted; stem, folded carton and both curved process arrows are retained.
Construction reference: Lucide milk and arrow-right-left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d2e8b45-430a-4208-bbed-b76c29804bc7'
SOURCE_PATH = 'pictographic-primitives/business/supply chain distributor fruit juice_0d2e8b45-430a-4208-bbed-b76c29804bc7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0d2e8b45-430a-4208-bbed-b76c29804bc7', 'pictographic-primitives/business/supply chain distributor fruit juice_0d2e8b45-430a-4208-bbed-b76c29804bc7.svg'),)

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


class FruitAndCartonCycle(Solo48):
    icon_id = 'fruit-and-carton-cycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('fruit', 'and', 'carton', 'cycle')

    def build(self):
        pts=[(6,17),(13,10),(20,17),(13,24)]
        for i,a in enumerate(pts):self.add_arc(f'fruit-{i}',a,pts[(i+1)%4],radius_x=7)
        self.add_contour('fruit',*[f'fruit-{i}' for i in range(4)],closed=True)
        self.add_line('stem',(13,10),(13,6))
        self.relate('connect','stem','fruit')
        self.add_polyline('carton',(26,34),(30,28),(38,28),(42,34),(42,42),(34,42),(26,42),closed=True)

        self.add_arc('upper-arrow',(42,16),(32,6),radius_x=10,sweep=False)
        self.add_polyline('upper-head',(40,6),(32,6),(32,14))
        self.relate('connect','upper-arrow','upper-head')
        self.add_arc('lower-arrow',(6,32),(16,42),radius_x=10,sweep=False)
        self.add_polyline('lower-head',(8,42),(16,42),(16,34))
        self.relate('connect','lower-arrow','lower-head')
