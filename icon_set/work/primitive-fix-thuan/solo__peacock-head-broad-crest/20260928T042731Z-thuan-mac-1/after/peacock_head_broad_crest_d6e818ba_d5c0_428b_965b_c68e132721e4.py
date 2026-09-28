"""Peacock head in profile with its broad fan crest, a short beak and a long neck.

Plan: VRECT_M (10,4)-(38,44). Head: r8 ring centred (22,25). Crest: a broad fan (a 135-degree sector of radius 13) opening upward from the crown (22,17), its straight edges reaching (10,12) and (34,12) and its arc topping out at (22,4). Beak: a line from the head's right point (30,25) to (38,27). Neck: back line from the head's left point (14,25) straight down to y=44, throat line from the head's bottom point (22,33) straight down to y=44, 8 from the back line.
Review of the rejected drawing: it was a broken polygon with a dented head, a pointed blob for the crest and a zigzag neck, so nothing read as a bird; the original has a round head, a broad fan crest, a small beak and a long neck.
Omissions: the eye (no 8-unit room inside the head ring beside the outline) and the individual crest feathers.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd6e818ba-d5c0-428b-965b-c68e132721e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__peacock-head-broad-crest/20260928T042731Z-thuan-mac-1/reference/peacock head_d6e818ba-d5c0-428b-965b-c68e132721e4.svg'
AUTHOR = "claude-fable-5-1"


class PeacockHeadBroadCrest(Solo48):
    icon_id = 'peacock-head-broad-crest'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('peacock-profile',)
    keywords = ('peacock', 'bird', 'head', 'crest', 'beak', 'neck', 'peafowl')

    def build(self) -> None:
        cx, cy, r = 22, 25, 8
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        for i in range(4):
            self.add_arc(f'head-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        crown = (cx, cy - r)
        # fan crest: sector of radius 13 about the crown, corners at 5-12-13 lattice points
        self.add_line('crest-left', crown, (cx - 12, cy - r - 5))
        self.add_arc('crest-arc', (cx - 12, cy - r - 5), (cx + 12, cy - r - 5), radius_x=13, sweep=True)
        self.add_line('crest-right', (cx + 12, cy - r - 5), crown)
        self.add_contour('crest', 'crest-left', 'crest-arc', 'crest-right', closed=True)
        self.relate('connect', 'crest', 'head')
        self.add_line('beak', (cx + r, cy), (38, 27))
        self.relate('connect', 'beak', 'head')
        self.add_line('neck-back', (cx - r, cy), (cx - r, 44))
        self.relate('connect', 'neck-back', 'head')
        self.add_line('throat', (cx, cy + r), (cx, 44))
        self.relate('connect', 'throat', 'head')
