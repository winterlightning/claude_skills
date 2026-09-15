"""Person beside Exploded Pie Chart.

Plan: Small circular head over semicircular shoulders beside two separated chart sectors. A curved connector links the person to the lower slice. Head bottom16 and shoulders top24 give exactly4 units of ink clearance. Human reference: human_ref/user.svg. Centerline extremes (4,8)-(44,40).
Reduction: Sectors become clear quarter forms; the person, separation, and curved linking line are retained.
Construction reference: Lucide chart-pie.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '678c9a4a-e6bd-4d6d-a6e7-1350c5f780ff'
SOURCE_PATH = 'pictographic-primitives/business/segmentation pie chart_678c9a4a-e6bd-4d6d-a6e7-1350c5f780ff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('678c9a4a-e6bd-4d6d-a6e7-1350c5f780ff', 'pictographic-primitives/business/segmentation pie chart_678c9a4a-e6bd-4d6d-a6e7-1350c5f780ff.svg'),)

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


class PersonBesideExplodedPieChart(Solo48):
    icon_id = 'person-beside-exploded-pie-chart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('person', 'beside', 'exploded', 'pie', 'chart')

    def build(self):
        _circle(self,'head',12,12,4)
        self.add_arc('shoulder-left',(4,32),(12,24),radius_x=8)
        self.add_arc('shoulder-right',(12,24),(20,32),radius_x=8)
        self.add_line('base-right',(20,32),(12,32))
        self.add_line('base-left',(12,32),(4,32))
        self.add_contour('bust','shoulder-left','shoulder-right','base-right','base-left',closed=True)
        self.add_arc('upper-sector-curve',(31,8),(44,21),radius_x=13)
        self.add_polyline('upper-sector-radii',(44,21),(31,21),(31,8))
        self.relate('connect','upper-sector-radii','upper-sector-curve')
        self.add_arc('lower-sector-curve',(44,30),(28,40),radius_x=16,radius_y=10)
        self.add_polyline('lower-sector-radii',(28,40),(28,30),(44,30))
        self.relate('connect','lower-sector-radii','lower-sector-curve')
        self.add_arc('connector',(12,32),(28,40),radius_x=16,radius_y=8,sweep=False)
        self.relate('connect','connector','bust')
        self.relate('connect','connector','lower-sector-curve')
        self.relate('connect','connector','lower-sector-radii')
