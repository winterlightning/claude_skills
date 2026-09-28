"""A standing figure with legs apart aiming a pistol to the right (sport shooting).

Plan: HRECT_L (4,8)-(44,40). Stick figure: r4 head at (16,12), a vertical torso starting exactly 8 below the head outline at (16,24), legs spread to (4,40) and (20,40). The shooting arm runs horizontally from the neck (16,24) to the hand at (28,24); the pistol is a backward-tilted grip from (30,16) through the hand to (26,32) with the barrel from (30,16) to (44,16), 8 above the arm.
Review of the rejected drawing: the pistol was a stepped bend at the end of a T of arms, so the figure read as a person pointing or waving; the original shows a pistol held out with its grip below the hand and barrel above.
Omissions: the resting arm (it would sit 6 from the torso at the hip).
Human reference: icon_set/references/human_ref/full_body_ref.png (round head, straight torso, spread legs); head-to-torso gap 8 on centerlines / 4 visible.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '911ac869-135a-4c07-a867-4ded07c4f4e7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-figure-aiming-a-pistol/20260928T042731Z-thuan-mac-1/reference/athletics shooting_911ac869-135a-4c07-a867-4ded07c4f4e7.svg'
AUTHOR = 'claude-fable-5-1'


class StandingFigureAimingAPistol(Solo48):
    icon_id = 'standing-figure-aiming-a-pistol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('sport-shooter', 'athletics-shooting')
    keywords = ('shooting', 'pistol', 'person', 'aim', 'stance', 'sport', 'athletics', 'figure')

    def build(self) -> None:
        hx, hy, r = 16, 12, 4
        pts = [(hx - r, hy), (hx, hy - r), (hx + r, hy), (hx, hy + r)]
        for i in range(4):
            self.add_arc(f'head-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        neck = (hx, hy + r + 8)
        self.add_line('torso', neck, (hx, 32))
        self.add_line('leg-left', (hx, 32), (4, 40))
        self.add_line('leg-right', (hx, 32), (20, 40))
        self.relate('connect', 'torso', 'leg-left')
        self.relate('connect', 'torso', 'leg-right')
        self.mark_human_figure('shooter', head='head', torso='torso', torso_junction='start')
        # arm out to the hand on the grip; the grip tilts back under the barrel
        self.add_line('arm', neck, (28, 24))
        self.relate('connect', 'arm', 'torso')
        self.add_line('grip-upper', (30, 16), (28, 24))
        self.add_line('grip-lower', (28, 24), (26, 32))
        self.add_line('barrel', (30, 16), (44, 16))
        self.relate('connect', 'arm', 'grip-upper')
        self.relate('connect', 'arm', 'grip-lower')
        self.relate('connect', 'grip-upper', 'grip-lower')
        self.relate('connect', 'grip-upper', 'barrel')
