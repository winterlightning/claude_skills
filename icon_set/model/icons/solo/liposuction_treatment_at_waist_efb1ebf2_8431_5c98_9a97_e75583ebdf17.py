"""Liposuction Treatment at Waist.

Plan: Cropped curved torso and underwear line with a diagonal capsule handle and aligned slender cannula; human body reference supplies minimal anatomy. Extremes (6,6)-(42,42).
Reduction: Navel, fine underwear divisions and the upper-right waist contour are omitted to keep the capsule handle and slender cannula clearly separated from the treatment area.
Construction reference: Lucide human reference and circle-dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efb1ebf2-8431-5c98-9a97-e75583ebdf17'
SOURCE_PATH = 'pictographic-primitives/beauty/surgery liposuction_efb1ebf2-8431-5c98-9a97-e75583ebdf17.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('efb1ebf2-8431-5c98-9a97-e75583ebdf17', 'pictographic-primitives/beauty/surgery liposuction_efb1ebf2-8431-5c98-9a97-e75583ebdf17.svg'),)

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


class LiposuctionTreatmentAtWaist(Solo48):
    icon_id = 'liposuction-treatment-at-waist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('liposuction', 'treatment', 'at', 'waist')

    def build(self):
        self.add_arc('left-upper',(10,6),(6,30),radius_x=36)
        self.add_line('left-lower',(6,30),(6,42))
        self.add_line('right-lower',(34,30),(34,42))
        self.add_polyline('underwear',(6,30),(20,42),(34,30))
        for name in ('left-upper','left-lower','right-lower'):self.relate('connect','underwear',name)
        # A true diagonal capsule: radius5 end caps and a shared 3-4-5 axis.
        self.add_line('handle-top',(34,7),(26,13))
        self.add_arc('handle-left-a',(26,13),(25,20),radius_x=5,sweep=False)
        self.add_arc('handle-left-b',(25,20),(32,21),radius_x=5,sweep=False)
        self.add_line('handle-bottom',(32,21),(40,15))
        self.add_arc('handle-right',(40,15),(34,7),radius_x=5,sweep=False)
        self.add_contour('handle','handle-top','handle-left-a','handle-left-b','handle-bottom','handle-right',closed=True)
        self.add_line('cannula',(25,20),(17,26))
        self.relate('connect','cannula','handle')
