"""Peacock head in profile with its fan of crest stalks, a short beak and a long neck.

Plan: VRECT_M (10,4)-(38,44). Head: r5 circle centred (21,19). Crest: three stalks fanning from the crown point (21,14) to (10,6), (21,4) and (32,6). Beak: a line from the head's right point (26,19) to (38,21). Neck: back line from the 3-4-5 point (17,22) straight down to 44, front line from (25,22) down to 36 then an r8 arc sweeping right to (33,44) for the breast.
Review of the rejected drawing: it was a broken polygon with a dented head, a pointed blob for the crest and a zigzag neck, so nothing read as a bird; the original has a round head, a fan crest, a small beak and a long straight neck.
Omissions: the eye (no 8-unit room inside an r5 head) and the individual crest tips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd6e818ba-d5c0-428b-965b-c68e132721e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__peacock-head-broad-crest/20260928T042731Z-thuan-mac-1/reference/peacock head_d6e818ba-d5c0-428b-965b-c68e132721e4.svg'
AUTHOR = 'thuan-mac-1/claude-fable-5-1'


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
        cx, cy, r = 21, 19, 5
        # head circle split at the crown, the right point and the two 3-4-5 neck points
        self.add_arc('head-crown-right', (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc('head-cheek-right', (cx + r, cy), (cx + 4, cy + 3), radius_x=r, sweep=True)
        self.add_arc('head-chin', (cx + 4, cy + 3), (cx - 4, cy + 3), radius_x=r, sweep=True)
        self.add_arc('head-cheek-left', (cx - 4, cy + 3), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc('head-crown-left', (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour('head', 'head-crown-right', 'head-cheek-right', 'head-chin',
                         'head-cheek-left', 'head-crown-left', closed=True)
        for name, tip in (('crest-left', (10, 6)), ('crest-mid', (21, 4)), ('crest-right', (32, 6))):
            self.add_line(name, (cx, cy - r), tip)
            self.relate('connect', name, 'head')
        self.add_line('beak', (cx + r, cy), (38, 21))
        self.relate('connect', 'beak', 'head')
        self.add_line('neck-back', (cx - 4, cy + 3), (cx - 4, 44))
        self.relate('connect', 'neck-back', 'head')
        self.add_line('neck-front', (cx + 4, cy + 3), (cx + 4, 36))
        self.add_arc('breast', (cx + 4, 36), (cx + 12, 44), radius_x=8, sweep=False)
        self.add_contour('throat', 'neck-front', 'breast')
        self.relate('connect', 'throat', 'head')
