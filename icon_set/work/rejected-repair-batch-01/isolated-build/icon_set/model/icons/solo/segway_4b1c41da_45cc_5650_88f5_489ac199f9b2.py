"""segway: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b1c41da-45cc-5650-88f5-489ac199f9b2'
SOURCE_PATH = 'pictographic-primitives/transportation/segway_4b1c41da-45cc-5650-88f5-489ac199f9b2.svg'
AUTHOR = 'gpt-6'

class Segway(Solo48):
    icon_id = 'segway'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('segway', 'self-balancing', 'personal transporter', 'wheel', 'micromobility', 'scooter', 'ride', 'side view')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('wheel-top', (12, 34), (32, 34), radius_x=10)
        self.add_arc('wheel-bottom', (32, 34), (12, 34), radius_x=10)
        self.add_contour('wheel', 'wheel-top', 'wheel-bottom', closed=True)
        self.add_dot('hub', (22, 34))
        self.add_polyline('column', (32, 34), (34, 34), (40, 4), (30, 4))
        self.relate('connect', 'column-1', 'wheel-top')
        self.relate('connect', 'column-1', 'wheel-bottom')
        self.add_line('platform', (8, 34), (12, 34))
        self.relate('connect', 'platform', 'wheel-top')
        self.relate('connect', 'platform', 'wheel-bottom')
