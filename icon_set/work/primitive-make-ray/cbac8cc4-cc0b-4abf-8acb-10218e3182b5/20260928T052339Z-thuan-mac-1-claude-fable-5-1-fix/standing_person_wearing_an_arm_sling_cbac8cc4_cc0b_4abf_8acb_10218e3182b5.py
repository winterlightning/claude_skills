"""A standing person wearing an arm sling: a strap over one shoulder holds the forearm across the body.

Plan: VRECT_L (8,4)-(40,44). Detached r5 head at (24,9) exactly 8 above the body's top line. Body: a rounded-shouldered outline (top line y=22 with r4 corners, sides at x=8 and x=40 running to the bottom, open below). Sling: a strap from the right shoulder (30,22) diagonally down to (18,34), meeting the forearm bar (18,34)-(30,34) that lies across the waist.
Review of the rejected drawing: the body was a square-shouldered U with a floating triangle in it and a 2-unit torso stub, so it read as a box with a wedge; the original is a person whose bandaged arm rests in a sling on a diagonal strap.
Omissions: the leg split and the hanging free arm (the body sides stand in for it); the sling pouch is reduced to the forearm bar.
Human reference: icon_set/references/human_ref/user.svg for the head-over-rounded-shoulders proportions; head-to-body gap 8 on centerlines / 4 visible.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cbac8cc4-cc0b-4abf-8acb-10218e3182b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-person-wearing-an-arm-sling/20260928T042731Z-thuan-mac-1/reference/bandage shoulder_cbac8cc4-cc0b-4abf-8acb-10218e3182b5.svg'
AUTHOR = 'claude-fable-5-1'


class StandingPersonWearingAnArmSling(Solo48):
    icon_id = 'standing-person-wearing-an-arm-sling'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('arm-in-sling', 'bandaged-shoulder')
    keywords = ('person', 'sling', 'arm', 'injury', 'medical', 'bandage', 'shoulder', 'recovery')

    def build(self) -> None:
        hx, hy, r = 24, 9, 5
        pts = [(hx - r, hy), (hx, hy - r), (hx + r, hy), (hx, hy + r)]
        for i in range(4):
            self.add_arc(f'head-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        top = hy + r + 8
        self.add_line('side-left', (8, 44), (8, top + 4))
        self.add_arc('shoulder-left', (8, top + 4), (12, top), radius_x=4, sweep=True)
        self.add_line('top-left', (12, top), (30, top))
        self.add_line('top-right', (30, top), (36, top))
        self.add_arc('shoulder-right', (36, top), (40, top + 4), radius_x=4, sweep=True)
        self.add_line('side-right', (40, top + 4), (40, 44))
        chain = ['side-left', 'shoulder-left', 'top-left', 'top-right', 'shoulder-right', 'side-right']
        for a, b in zip(chain, chain[1:]):
            self.relate('connect', a, b)
        self.add_line('strap', (30, top), (18, 34))
        self.add_line('forearm', (18, 34), (30, 34))
        self.relate('connect', 'strap', 'top-left')
        self.relate('connect', 'strap', 'top-right')
        self.relate('connect', 'strap', 'forearm')
