"""Diagonal wrapped rope coil: a hank of rope folded into two loops along the
diagonal, bound at the middle by a wrap.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: coil axis runs from the lower-left to the upper-right corner
through (24,24). Each loop is drawn with the rope's thickness: an outer
outline that narrows to a waist at the band, and a teardrop eye 8+ inside it
pointing into the band (figure-eight hank). The
wrap is a band across the axis (edges x - y = +/-6, 8.5 apart) whose ends
bulge past the loop outlines. The upper-right loop is mirrored about the
coil axis x + y = 48; the lower-left loop is its point reflection through
(24,24).
Revision: the earlier drawing had no eyes in the loops and read as an egg
cut by a band; the eyes now show the rope's loops.
Reduction: the reference's three wrap turns become one band (two more turns
cannot keep 8 units apart inside the neck).
Construction reference: Lucide `cable`/`paperclip` rounded return loops, re-authored.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5038cc3d-6360-4042-ac7a-accba6076287'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-wrapped-rope-coil/20260926T125429Z-thuan-mac/reference/outdoors rope 1_5038cc3d-6360-4042-ac7a-accba6076287.svg'
AUTHOR = 'claude-opus-5-5'


def ab(a, b):
    """Axis frame: a runs along the coil toward the upper-right corner, b across it."""
    return (24 + a + b, 24 - a + b)


def rot(p):
    """Point reflection through the centre (24, 24)."""
    return (48 - p[0], 48 - p[1])


# upper-right loop in the axis frame (mirrored in b)
WAIST = (3, 5)                                   # band corner, xy (32, 26)
OUTER = ((4.5, 13.5), (10, 8), (15, 3))          # to the tip arc, arriving vertically at (42, 12)
TIP_R = 6                                        # tip arc about (36, 12)
EYE = ((5, 3.2), (7, 3), (9, 0))                 # teardrop eye from the band point (3, 0)


class Drawing(Solo48):
    icon_id = 'diagonal-wrapped-rope-coil'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('rope hank', 'coiled rope')
    keywords = ('rope', 'coil', 'climbing', 'loops', 'wrapped', 'camping', 'hank')

    def loop(self, tag, f):
        """One loop; f maps upper-right xy coordinates to this loop's position."""
        def P(a, b):
            return f(ab(a, b))
        wa, wb = WAIST
        (c1a, c1b), (c2a, c2b), (ta, tb) = OUTER
        self.add_bezier(f'{tag}-outer-a', P(wa, wb), (P(c1a, c1b), P(c2a, c2b), P(ta, tb)))
        self.add_arc(f'{tag}-outer-tip', P(ta, tb), P(ta, -tb), radius_x=TIP_R, sweep=False)
        self.add_bezier(f'{tag}-outer-b', P(ta, -tb), (P(c2a, -c2b), P(c1a, -c1b), P(wa, -wb)))
        self.add_contour(f'{tag}-outer', f'{tag}-outer-a', f'{tag}-outer-tip', f'{tag}-outer-b')
        (e1a, e1b), (e2a, e2b), (eta, etb) = EYE
        self.add_bezier(f'{tag}-eye', P(wa, 0), (P(e1a, e1b), P(e2a, e2b), P(eta, etb)),
                        (P(e2a, -e2b), P(e1a, -e1b), P(wa, 0)))
        # band edge (a = 3) split at the eye
        self.add_line(f'{tag}-edge-1', P(wa, -wb), P(wa, 0))
        self.add_line(f'{tag}-edge-2', P(wa, 0), P(wa, wb))

    def build(self):
        self.loop('ur', lambda p: p)
        self.loop('ll', rot)
        # band ends bulge across the axis between the two loops
        self.add_arc('band-end-lower', ab(3, 5), ab(-3, 5), radius_x=5, sweep=True)
        self.add_arc('band-end-upper', ab(-3, -5), ab(3, -5), radius_x=5, sweep=True)
        self.add_contour('band', 'ur-edge-2', 'band-end-lower', 'll-edge-1', 'll-edge-2',
                         'band-end-upper', 'ur-edge-1', closed=True)
        for tag in ('ur', 'll'):
            self.relate('connect', f'{tag}-outer-a', f'{tag}-edge-2')
            self.relate('connect', f'{tag}-outer-b', f'{tag}-edge-1')
            self.relate('connect', f'{tag}-eye', f'{tag}-edge-1')
            self.relate('connect', f'{tag}-eye', f'{tag}-edge-2')
        self.relate('connect', 'ur-outer-a', 'band-end-lower')
        self.relate('connect', 'll-outer-b', 'band-end-lower')
        self.relate('connect', 'll-outer-a', 'band-end-upper')
        self.relate('connect', 'ur-outer-b', 'band-end-upper')
