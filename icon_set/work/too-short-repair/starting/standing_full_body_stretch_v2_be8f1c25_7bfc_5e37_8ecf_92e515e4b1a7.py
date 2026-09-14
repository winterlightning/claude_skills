# Variant of standing-full-body-stretch; parent file remains unchanged.
"""A standing figure raises both arms in a wide rounded arc around the head. One leg remains straight while the other bends outward, opening a narrow triangular gap below the torso.
Construction: Bounds (8,6)-(40,42). Mirrored overhead arm arcs; straight supporting leg and one outward bend retain intentional lower-body asymmetry.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be8f1c25-7bfc-5e37-8ecf-92e515e4b1a7'
SOURCE_PATH = 'pictographic-primitives/sports/yoga full body stretch_be8f1c25-7bfc-5e37-8ecf-92e515e4b1a7.svg'
AUTHOR = 'gpt-6'

class StandingFullBodyStretchVariant2(Solo48):
    icon_id = 'standing-full-body-stretch-v2'
    variant_of = 'standing-full-body-stretch'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('standing', 'full', 'body', 'stretch', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 12), (27, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 12), (21, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arm-l', (8, 6), (8, 8))
        self.add_arc('shoulder-l', (8, 8), (24, 24), radius_x=16, radius_y=16, sweep=False)
        self.add_arc('shoulder-r', (24, 24), (40, 8), radius_x=16, radius_y=16, sweep=False)
        self.add_line('arm-r', (40, 8), (40, 6))
        self.add_contour('arms', 'arm-l', 'shoulder-l', 'shoulder-r', 'arm-r', closed=False)
        self.add_polyline('torso', (24, 24), (24, 32), (24, 42), closed=False)
        self.relate('connect', 'arms', 'torso')
        self.add_polyline('leg', (24, 32), (35, 39), (33, 42), closed=False)
        self.relate('connect', 'torso', 'leg')
