"""A standing hen in profile facing left, with comb, beak, round body, raised tail and two legs.

Plan: SQUARE (6,6)-(42,42). Head: r5 circle about (16,19) with a tilted comb stroke from its top (16,14) to (17,6) and a beak from its left point (11,19) to (6,21). Body: an r10 semicircular belly about (26,24) from (16,24) (which is also the head's bottom point) round the bottom to (36,24), a tail line rising from (36,24) to the tip (42,14), and a back line from the tip to the head's right point (21,19). Legs drop from the belly's 3-4-5 points (20,32) and (32,32) to y=42.
Review of the rejected drawing: the body was a lumpy multi-cubic blob with a hook on top and the legs were bent hooks, so it read as a dinosaur or a shoe; the original is a plump hen with a small head, comb, beak, pointed tail and straight legs.
Omissions: the eye, the wattle and the feet.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '325e54cb-8d70-4bde-86ba-e15543964464'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-hen-profile/20260928T042731Z-thuan-mac-1/reference/hen_325e54cb-8d70-4bde-86ba-e15543964464.svg'
AUTHOR = 'claude-fable-5-1'


class StandingHenProfile(Solo48):
    icon_id = 'standing-hen-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('chicken', 'hen-side-view')
    keywords = ('hen', 'chicken', 'bird', 'farm', 'poultry', 'standing', 'profile')

    def build(self) -> None:
        hx, hy, r = 16, 19, 5
        # head split at top, right, bottom and left points
        self.add_arc('head-0', (hx - r, hy), (hx, hy - r), radius_x=r, sweep=True)
        self.add_arc('head-1', (hx, hy - r), (hx + r, hy), radius_x=r, sweep=True)
        self.add_arc('head-2', (hx + r, hy), (hx, hy + r), radius_x=r, sweep=True)
        self.add_arc('head-3', (hx, hy + r), (hx - r, hy), radius_x=r, sweep=True)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        self.add_line('comb', (hx, hy - r), (17, 6))
        self.add_line('beak', (hx - r, hy), (6, 21))
        self.relate('connect', 'comb', 'head')
        self.relate('connect', 'beak', 'head')
        # body: belly semicircle about (26,24), split at the leg roots
        bx, by, br = 26, 24, 10
        self.add_arc('belly-0', (bx - br, by), (bx - 6, by + 8), radius_x=br, sweep=False)
        self.add_arc('belly-1', (bx - 6, by + 8), (bx + 6, by + 8), radius_x=br, sweep=False)
        self.add_arc('belly-2', (bx + 6, by + 8), (bx + br, by), radius_x=br, sweep=False)
        self.add_line('tail', (bx + br, by), (42, 14))
        self.add_line('back', (42, 14), (hx + r, hy))
        self.add_contour('body', 'belly-0', 'belly-1', 'belly-2', 'tail', 'back')
        self.relate('connect', 'body', 'head')
        self.add_line('leg-left', (bx - 6, by + 8), (18, 42))
        self.add_line('leg-right', (bx + 6, by + 8), (32, 42))
        self.relate('connect', 'leg-left', 'body')
        self.relate('connect', 'leg-right', 'body')
