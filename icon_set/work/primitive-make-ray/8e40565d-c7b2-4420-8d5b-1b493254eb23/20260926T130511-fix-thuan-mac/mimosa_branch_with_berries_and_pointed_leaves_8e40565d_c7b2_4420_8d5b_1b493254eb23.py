"""Mimosa branch with round berries and pointed leaves.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: one stem rises from the base (27,42) to the upper left on a 1:3
slope and ends in a berry; two more berries hang on short horizontal twigs to
its left. A leafy branch forks from the stem at (25,36) and climbs to the upper
right on the mirrored 1:3 slope, ending in a pointed leaf, with a second
pointed leaf (vesicas of two equal arcs) reaching right. Berries are r3 rings
(the exempt 6-diameter circle), 14+ apart so their ink stays 8 apart.
Revision: the earlier drawing put everything on a right-angle comb and read as
a circuit; this follows the reference's two diverging sprigs.
Reduction: five berries reduced to three, leaves reduced to two so
they keep 8 units apart.
Construction reference: no useful local Lucide match (`leaf`/`sprout` checked
for the vesica leaf construction only).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8e40565d-c7b2-4420-8d5b-1b493254eb23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mimosa-branch-with-berries-and-pointed-leaves/20260926T125429Z-thuan-mac/reference/mimosa_8e40565d-c7b2-4420-8d5b-1b493254eb23.svg'
AUTHOR = "claude-opus-5-5"

BERRY_R = 3
BASE = (27, 42)
STEM_TOP = (17, 12)         # berry-top bottom point
FORK = (25, 36)
BRANCH_TOP = (31, 18)


class BatchIcon(Solo48):
    icon_id = 'mimosa-branch-with-berries-and-pointed-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('mimosa sprig',)
    keywords = ('mimosa', 'branch', 'berries', 'leaves', 'plant', 'sprig', 'botanical')

    def berry(self, name, c):
        cx, cy = c
        r = BERRY_R
        pts = [(cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        for i in range(4):
            self.add_arc(f'{name}-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)
        return {'E': (pts[0], (f'{name}-0', f'{name}-3')), 'S': (pts[1], (f'{name}-1', f'{name}-0'))}

    def leaf(self, name, base, tip, r):
        self.add_arc(f'{name}-a', base, tip, radius_x=r, sweep=True)
        self.add_arc(f'{name}-b', tip, base, radius_x=r, sweep=True)
        self.add_contour(name, f'{name}-a', f'{name}-b', closed=True)
        return (f'{name}-a', f'{name}-b')

    def link(self, a, bs):
        for b in bs:
            self.relate('connect', a, b)

    def build(self):
        # stem, split where twigs and the branch leave it (x = 17 + (y - 12) / 3)
        nodes = [BASE, (26, 39), FORK, (21, 24), STEM_TOP]
        stem = []
        for i in range(len(nodes) - 1):
            self.add_line(f'stem-{i}', nodes[i], nodes[i + 1])
            stem.append(f'stem-{i}')
        self.add_contour('stem', *stem)
        top = self.berry('berry-top', (17, 9))
        self.link('stem-3', top['S'][1])
        # berries on twigs to the left
        for name, node, centre, near in (('berry-mid', (21, 24), (9, 24), ('stem-2', 'stem-3')),
                                          ('berry-low', (26, 39), (9, 39), ('stem-0', 'stem-1'))):
            b = self.berry(name, centre)
            self.add_line(f'{name}-twig', node, b['E'][0])
            self.link(f'{name}-twig', b['E'][1])
            self.link(f'{name}-twig', near)
        # leafy branch (x = 25 + (36 - y) / 3), split at the leaf node
        bnodes = [FORK, (27, 30), BRANCH_TOP]
        br = []
        for i in range(len(bnodes) - 1):
            self.add_line(f'branch-{i}', bnodes[i], bnodes[i + 1])
            br.append(f'branch-{i}')
        self.add_contour('branch', *br)
        self.link('branch-0', ('stem-1', 'stem-2'))
        self.link('branch-1', self.leaf('leaf-top', BRANCH_TOP, (41, 8), 9))
        lower = self.leaf('leaf-lower', (27, 30), (42, 30), 10)
        self.link('branch-0', lower); self.link('branch-1', lower)
