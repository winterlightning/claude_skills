"""Magnifying Glass over Bar.

Plan: Circular lens centered(24,21), radius15; a horizontal target bar crosses exact left/right cardinal nodes and a diagonal handle attaches at(33,33). Centerline extremes (6,6)-(42,42).
Reduction: The target bar becomes one bold horizontal run; extra outlines that would crowd the lens are removed.
Construction reference: Lucide search.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a0dc2db-df7a-4a89-a012-e791a2f92301'
SOURCE_PATH = 'pictographic-primitives/apps/seo zoom_2a0dc2db-df7a-4a89-a012-e791a2f92301.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2a0dc2db-df7a-4a89-a012-e791a2f92301', 'pictographic-primitives/apps/seo zoom_2a0dc2db-df7a-4a89-a012-e791a2f92301.svg'),)

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


class MagnifierOverBar(Solo48):
    icon_id = 'magnifier-over-bar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('magnifying', 'glass', 'over', 'bar')

    def build(self):
        self.add_arc('lens-top',(9,21),(39,21),radius_x=15)
        self.add_arc('lens-lower-right',(39,21),(33,33),radius_x=15)
        self.add_arc('lens-bottom',(33,33),(9,21),radius_x=15)
        self.add_contour('lens','lens-top','lens-lower-right','lens-bottom',closed=True)
        self.add_polyline('bar',(6,21),(9,21),(39,21),(42,21))
        self.relate('connect','lens','bar')
        self.add_line('handle',(33,33),(42,42))
        self.relate('connect','handle','lens')
