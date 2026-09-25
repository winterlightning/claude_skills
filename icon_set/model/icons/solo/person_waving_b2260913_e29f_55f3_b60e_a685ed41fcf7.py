"""A standing person raises a bent right arm. Lucide person-standing informs the simple limbs; hand fingers and doubled arm outlines are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b2260913-e29f-55f3-b60e-a685ed41fcf7'
SOURCE_PATH = 'pictographic-primitives/users/man actions_b2260913-e29f-55f3-b60e-a685ed41fcf7.svg'
AUTHOR = 'gpt-6'

class PersonWaving(Solo48):
    icon_id = 'person-waving'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    aliases = ()
    keywords = ('person', 'waving', 'hello', 'greeting', 'man', 'hand', 'raised', 'figure')

    def circle(self, name, cx, cy, radius):
        top, bottom = ((cx, cy - radius), (cx, cy + radius))
        self.add_arc(name + '-right', top, bottom, radius_x=radius)
        self.add_arc(name + '-left', bottom, top, radius_x=radius)
        self.add_contour(name, name + '-right', name + '-left', closed=True)

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.circle('head', 23, 10, 6)
        self.add_line('torso', (23, 24), (23, 33))
        self.add_polyline('left-arm', (23, 24), (14, 24), (8, 31), (8, 36))
        self.add_line('wave-base', (23, 24), (32, 24))
        self.add_polyline('wave', (32, 24), (40, 17), (40, 7))
        self.relate('connect', 'wave-base', 'wave')
        self.relate('connect', 'wave-base', 'torso')
        self.add_polyline('legs', (17, 44), (17, 33), (23, 33), (29, 33), (29, 44))
        for member in ('left-arm', 'wave-base', 'legs'):
            self.relate('connect', 'torso', member)
        self.relate('connect', 'left-arm', 'wave-base')
