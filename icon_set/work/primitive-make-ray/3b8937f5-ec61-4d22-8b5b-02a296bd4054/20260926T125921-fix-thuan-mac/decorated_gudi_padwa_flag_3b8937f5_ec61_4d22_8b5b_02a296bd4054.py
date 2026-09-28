"""Decorated Gudi Padwa flag: an inverted kalash pot crowning a pole, with
garland strands hanging from the pot rim and a waving cloth flag.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: pole on x=14; the inverted pot is symmetric about the pole (round
body r5 about (14,11), a neck at y=15 flaring to a rim line y=18 from x=6 to x=22); two
garland strands hang 8 long from the rim tips; the right strand falls onto
the flag's top edge (it hangs in front of the cloth, as in the reference);
the flag waves with two parallel cubics 10 apart.
Revision: the earlier ring-on-a-pole read as a map pin; the pot silhouette with
flared rim and hanging garlands now carries the Gudi meaning.
Omitted: neem-leaf twigs on the strands (too small at 48).
Construction reference: Lucide `flag` (pole plus waving cloth), re-authored.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3b8937f5-ec61-4d22-8b5b-02a296bd4054'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__decorated-gudi-padwa-flag/20260926T125429Z-thuan-mac/reference/gudi padwa 1_3b8937f5-ec61-4d22-8b5b-02a296bd4054.svg'
AUTHOR = 'claude-opus-5-5'

POLE_X = 14
RIM_Y = 18
RIM_HALF = 8
FLAG_TOP = 26
FLAG_H = 10


class DecoratedGudiPadwaFlag(Solo48):
    icon_id = 'decorated-gudi-padwa-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ('gudi', 'kalash flag')
    keywords = ('decorated', 'gudi', 'padwa', 'flag', 'kalash', 'pot', 'festival', 'new year')

    def build(self):
        x, rl, rr = POLE_X, POLE_X - RIM_HALF, POLE_X + RIM_HALF
        # inverted pot
        self.add_line('rim-left', (x, RIM_Y), (rl, RIM_Y))
        # round body r5 about (16, 11); 3-4-5 neck points (13,15) and (19,15)
        self.add_line('flare-left', (rl, RIM_Y), (x - 3, 15))
        self.add_arc('dome', (x - 3, 15), (x + 3, 15), radius_x=5, large_arc=True, sweep=True)
        self.add_line('flare-right', (x + 3, 15), (rr, RIM_Y))
        self.add_line('rim-right', (rr, RIM_Y), (x, RIM_Y))
        self.add_contour('pot', 'rim-left', 'flare-left', 'dome', 'flare-right', 'rim-right', closed=True)
        # pole
        self.add_line('pole', (x, RIM_Y), (x, 42))
        self.relate('connect', 'pole', 'rim-left')
        self.relate('connect', 'pole', 'rim-right')
        # garland strands
        self.add_line('garland-left', (rl, RIM_Y), (rl, FLAG_TOP))
        self.add_line('garland-right', (rr, RIM_Y), (rr, FLAG_TOP))
        self.relate('connect', 'garland-left', 'rim-left')
        self.relate('connect', 'garland-left', 'flare-left')
        self.relate('connect', 'garland-right', 'rim-right')
        self.relate('connect', 'garland-right', 'flare-right')
        # waving flag
        b = FLAG_TOP + FLAG_H
        self.add_line('flag-top-in', (x, FLAG_TOP), (rr, FLAG_TOP))
        self.add_bezier('flag-top-wave', (rr, FLAG_TOP), ((rr + 6, FLAG_TOP), (36, 22), (42, 22)))
        self.add_line('flag-fly', (42, 22), (42, 22 + FLAG_H))
        self.add_bezier('flag-bottom-wave', (42, 22 + FLAG_H), ((36, 22 + FLAG_H), (rr + 6, b), (rr, b)))
        self.add_line('flag-bottom-in', (rr, b), (x, b))
        self.add_contour('flag', 'flag-top-in', 'flag-top-wave', 'flag-fly', 'flag-bottom-wave', 'flag-bottom-in')
        self.relate('connect', 'flag-top-in', 'pole')
        self.relate('connect', 'flag-bottom-in', 'pole')
        self.relate('connect', 'garland-right', 'flag-top-in')
        self.relate('connect', 'garland-right', 'flag-top-wave')
