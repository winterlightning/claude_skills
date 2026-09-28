"""Hard Hat with Wide Curved Brim.

Plan: Symmetric circular crown, single central ridge, broad half-ellipse brim. Centerline extremes (4,8)-(44,40).
Reduction: Raised ridge becomes a single central rib; the wide curved brim is retained.
Construction reference: Lucide hard-hat.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cefdcc61-2ed2-5460-9530-e110178b2c81'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hard-hat-with-wide-curved-brim/20260927T061835Z-thuan-mac-1/reference/safety helmet mine_cefdcc61-2ed2-5460-9530-e110178b2c81.svg'
AUTHOR = "gpt-6"
SOURCE_REFERENCES = (('cefdcc61-2ed2-5460-9530-e110178b2c81', 'pictographic-primitives/construction/safety helmet mine_cefdcc61-2ed2-5460-9530-e110178b2c81.svg'),)

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


class HardHatWithWideCurvedBrim(Solo48):
    icon_id = 'hard-hat-with-wide-curved-brim'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('hard', 'hat', 'with', 'wide', 'curved', 'brim')

    def build(self):
        # Raised crown ridge follows the distinct original mine helmet.
        self.add_line('side-left',(8,29),(8,24))
        self.add_bezier('crown-left',(8,24),((8,17),(12,11),(18,9)))
        self.add_line('ridge-top-left',(18,9),(20,8))
        self.add_line('ridge-top',(20,8),(28,8))
        self.add_line('ridge-top-right',(28,8),(30,9))
        self.add_bezier('crown-right',(30,9),((36,11),(40,17),(40,24)))
        self.add_line('side-right',(40,24),(40,29))
        self.add_contour('shell','side-left','crown-left','ridge-top-left','ridge-top','ridge-top-right','crown-right','side-right')
        self.add_polyline('brim-top',(4,29),(8,29),(40,29),(44,29))
        self.add_arc('brim-bottom',(44,29),(4,29),radius_x=20,radius_y=11)
        self.relate('connect','shell','brim-top')
        self.relate('connect','brim-top','brim-bottom')
        self.add_line('ridge-left',(18,9),(20,19))
        self.add_line('ridge-right',(30,9),(28,19))
        self.relate('connect','ridge-left','shell')
        self.relate('connect','ridge-right','shell')
