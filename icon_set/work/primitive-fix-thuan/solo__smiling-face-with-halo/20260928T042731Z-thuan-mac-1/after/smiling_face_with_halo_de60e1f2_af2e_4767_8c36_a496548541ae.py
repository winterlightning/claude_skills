"""A smiling angel face with a halo ring floating over its head.

Plan: CIRCLE (only the chin reaches radius 20). The halo is an ellipse rx15 ry5 about (24,13); the head is an r15 circle about (24,29). The two meet at the lattice points (15,17) and (33,17), which lie on both curves, so the halo's front arc between them is hidden behind the head and the head's top cap is hidden inside the ring: the visible halo is the ellipse from (15,17) up over (24,8) to (33,17), and the visible head runs from (15,17) down around the chin (24,44) to (33,17). Dot eyes at (20,25)/(28,25) and an r6 smile from (20,34) to (28,34).
Review of the rejected drawing: the halo floated 12 units above a small r12 face that had no eyes, so it read as a ring over a mouth; the original is a full face with eyes and a smile under a wide halo that sits on the head.
Omissions: the eyes' dash shape becomes dots (a 2-unit dash cannot keep 8 from both the rim and the smile).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'de60e1f2-af2e-4767-8c36-a496548541ae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-face-with-halo/20260928T042731Z-thuan-mac-1/reference/face smile halo_de60e1f2-af2e-4767-8c36-a496548541ae.svg'
AUTHOR = 'claude-fable-5-1'


class SmilingFaceWithHalo(Solo48):
    icon_id = 'smiling-face-with-halo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('angel-face', 'innocent-face')
    keywords = ('face', 'smile', 'halo', 'angel', 'innocent', 'emoji')

    def build(self) -> None:
        # halo: visible upper part of the ellipse, split at its cardinal points
        self.add_arc('halo-0', (15, 17), (9, 13), radius_x=15, radius_y=5, sweep=True)
        self.add_arc('halo-1', (9, 13), (24, 8), radius_x=15, radius_y=5, sweep=True)
        self.add_arc('halo-2', (24, 8), (39, 13), radius_x=15, radius_y=5, sweep=True)
        self.add_arc('halo-3', (39, 13), (33, 17), radius_x=15, radius_y=5, sweep=True)
        self.add_contour('halo', 'halo-0', 'halo-1', 'halo-2', 'halo-3')
        # head: visible lower part of the r15 circle, split at its cardinal points
        self.add_arc('head-0', (15, 17), (9, 29), radius_x=15, sweep=False)
        self.add_arc('head-1', (9, 29), (24, 44), radius_x=15, sweep=False)
        self.add_arc('head-2', (24, 44), (39, 29), radius_x=15, sweep=False)
        self.add_arc('head-3', (39, 29), (33, 17), radius_x=15, sweep=False)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3')
        self.relate('connect', 'halo', 'head')
        self.add_dot('eye-left', (20, 25))
        self.add_dot('eye-right', (28, 25))
        self.add_arc('smile', (20, 34), (28, 34), radius_x=6, sweep=False)
