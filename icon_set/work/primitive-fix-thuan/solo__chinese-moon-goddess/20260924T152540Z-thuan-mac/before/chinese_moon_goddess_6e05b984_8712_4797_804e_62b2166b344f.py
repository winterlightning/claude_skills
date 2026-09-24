"""Chinese Moon Goddess.

Plan: Paired hair buns and a circular radius-8 lower jaw centered at (24,12), above a flared robe and flowing sleeves. Jaw bottom y20 and robe/shoulders at (24,28) give exactly 8 centerline / 4 visible units of detached clearance. Shared human references user.svg and full_body_ref.png. Remove interior robe folds. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e05b984-8712-4797-804e-62b2166b344f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/chinese moon festival lady_6e05b984-8712-4797-804e-62b2166b344f.svg'
AUTHOR = 'gpt-6'

class ChineseMoonGoddess(Solo48):
    icon_id = 'chinese-moon-goddess'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('chinese', 'moon', 'goddess')

    def build(self):
        self.add_line('hair-left',(16,12),(16,10))
        self.add_arc('hair-bun-left',(16,10),(24,10),radius_x=4)
        self.add_arc('hair-bun-right',(24,10),(32,10),radius_x=4)
        self.add_line('hair-right',(32,10),(32,12))
        self.add_arc('jaw',(32,12),(16,12),radius_x=8)
        self.add_contour('head','hair-left','hair-bun-left','hair-bun-right','hair-right','jaw',closed=True)
        self.add_polyline('robe',(24,28),(34,42),(14,42),closed=True)
        self.add_line('left-shoulder',(24,28),(14,28))
        self.add_arc('left-sleeve',(14,28),(6,36),radius_x=8,sweep=False)
        self.add_line('left-tail',(6,36),(6,40))
        self.add_contour('left','left-shoulder','left-sleeve','left-tail')
        self.add_line('right-shoulder',(24,28),(34,28))
        self.add_arc('right-sleeve',(34,28),(42,36),radius_x=8)
        self.add_line('right-tail',(42,36),(42,40))
        self.add_contour('right','right-shoulder','right-sleeve','right-tail')
        for a,b in [('robe','left'),('robe','right'),('left','right')]:self.relate('connect',a,b)
