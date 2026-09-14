"""A standing figure raises both arms in a wide rounded arc around the head. One leg remains straight while the other bends outward, opening a narrow triangular gap below the torso.
Construction: Bounds (8,6)-(40,42). Mirrored overhead arm arcs; straight supporting leg and one outward bend retain intentional lower-body asymmetry.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be8f1c25-7bfc-5e37-8ecf-92e515e4b1a7'
SOURCE_PATH = 'pictographic-primitives/sports/yoga full body stretch_be8f1c25-7bfc-5e37-8ecf-92e515e4b1a7.svg'
AUTHOR = 'gpt-6'

class StandingFullBodyStretch(Solo48):
    icon_id = 'standing-full-body-stretch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('standing', 'full', 'body', 'stretch', 'yoga', 'exercise')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('head-top', (21, 13), (27, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 13), (21, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        # Separate the rounded side arms from the flat shoulder span so the exact gap is certifiable.
        self.add_line('arm-l', (8, 4), (8, 16))
        self.add_arc('shoulder-l', (8, 16), (16, 24), radius_x=8, sweep=False)
        self.add_contour('left-arm', 'arm-l', 'shoulder-l')
        self.add_line('arms', (16, 24), (24, 24))
        self.add_line('arms-right', (24, 24), (32, 24))
        self.add_arc('shoulder-r', (32, 24), (40, 16), radius_x=8, sweep=False)
        self.add_line('arm-r', (40, 16), (40, 4))
        self.add_contour('right-arm', 'shoulder-r', 'arm-r')
        self.relate('connect', 'left-arm', 'arms')
        self.relate('connect', 'arms', 'arms-right')
        self.relate('connect', 'arms-right', 'right-arm')
        self.add_polyline('torso', (24, 24), (24, 32), (24, 44), closed=False)
        self.relate('connect', 'arms', 'torso')
        self.add_polyline('leg', (24, 32), (35, 39), (33, 44), closed=False)
        self.relate('connect', 'torso', 'leg')
