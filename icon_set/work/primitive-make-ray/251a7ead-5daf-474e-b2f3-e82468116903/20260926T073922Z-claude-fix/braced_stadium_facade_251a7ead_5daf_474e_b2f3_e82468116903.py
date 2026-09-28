"""Braced Stadium Facade.

Plan: Broad roof and dome above repeated triangular braces and sloping walls. Extremes (4,8)-(44,40).
Reduction: Overhead decoration removed; dome, roof and repeating structural braces retained.
Construction reference: Lucide landmark.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '251a7ead-5daf-474e-b2f3-e82468116903'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__braced-stadium-facade/20260926T073831Z-thuan-mac/reference/stadium 2_251a7ead-5daf-474e-b2f3-e82468116903.svg'
AUTHOR = "claude-opus-5-5"
SOURCE_REFERENCES = (('251a7ead-5daf-474e-b2f3-e82468116903', 'pictographic-primitives/building/stadium 2_251a7ead-5daf-474e-b2f3-e82468116903.svg'),)

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


class BracedStadiumFacade(Solo48):
    icon_id = 'braced-stadium-facade'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('braced', 'stadium', 'facade')

    def build(self):
        # Redraw (no reviewer text; matched to the reference): a stadium drum. A wide flat roof
        # (x 13..35, y 8..16, r4 upper corners) sits on a rim band that flares outward (top
        # (8, 16)-(40, 16), bottom (4, 24)-(44, 24)); below it the wall tapers inward to the
        # ground ((4, 24)-(10, 40) and (44, 24)-(38, 40)) and is braced by a zigzag of struts
        # (10, 40)-(17, 24)-(24, 40)-(31, 24)-(38, 40); a ground line runs (4, 40)-(44, 40).
        # The reference's two light rays above the roof are omitted: they cannot sit 8 from the
        # roof and the rim inside the 32-unit height. Earlier attempts with a rim flaring the
        # other way read as a basket (attempts/v1-v3).
        self.add_line('rim-top-left', (8, 16), (13, 16))
        self.add_line('rim-top-mid', (13, 16), (35, 16))
        self.add_line('rim-top-right', (35, 16), (40, 16))
        self.add_line('rim-right', (40, 16), (44, 24))
        self.add_line('rim-bottom-right', (44, 24), (31, 24))
        self.add_line('rim-bottom-mid', (31, 24), (17, 24))
        self.add_line('rim-bottom-left', (17, 24), (4, 24))
        self.add_line('rim-left', (4, 24), (8, 16))
        self.add_contour('rim', 'rim-top-left', 'rim-top-mid', 'rim-top-right', 'rim-right', 'rim-bottom-right',
                         'rim-bottom-mid', 'rim-bottom-left', 'rim-left', closed=True)
        self.add_line('roof-left', (13, 16), (13, 12))
        self.add_arc('roof-corner-left', (13, 12), (17, 8), radius_x=4)
        self.add_line('roof-top', (17, 8), (31, 8))
        self.add_arc('roof-corner-right', (31, 8), (35, 12), radius_x=4)
        self.add_line('roof-right', (35, 12), (35, 16))
        self.add_contour('roof', 'roof-left', 'roof-corner-left', 'roof-top', 'roof-corner-right', 'roof-right')
        self.relate('connect', 'rim', 'roof')
        self.add_line('wall-left', (4, 24), (10, 40))
        self.add_line('wall-right', (44, 24), (38, 40))
        self.add_polyline('struts', (10, 40), (17, 24), (24, 40), (31, 24), (38, 40))
        self.add_polyline('ground', (4, 40), (10, 40), (24, 40), (38, 40), (44, 40))
        for part in ('wall-left', 'wall-right', 'struts'):
            self.relate('connect', 'rim', part)
            self.relate('connect', 'ground', part)
        self.relate('connect', 'wall-left', 'struts')
        self.relate('connect', 'wall-right', 'struts')
