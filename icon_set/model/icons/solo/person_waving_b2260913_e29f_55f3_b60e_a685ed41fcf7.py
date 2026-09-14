"""A standing person raises a bent right arm. Lucide person-standing informs the simple limbs; hand fingers and doubled arm outlines are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2260913-e29f-55f3-b60e-a685ed41fcf7'
SOURCE_PATH = 'pictographic-primitives/users/man actions_b2260913-e29f-55f3-b60e-a685ed41fcf7.svg'
AUTHOR = 'gpt-6'


class PersonWaving(Solo48):
    icon_id = 'person-waving'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
    aliases = ()
    keywords = ('person', 'waving', 'hello', 'greeting', 'man', 'hand', 'raised', 'figure')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-right', top, bottom, radius_x=radius)
        self.add_arc(name+'-left', bottom, top, radius_x=radius)
        self.add_contour(name, name+'-right', name+'-left', closed=True)

    def build(self) -> None:
        # Portrait extremes (8,6)-(40,42); raised arm intentionally asymmetric.
        self.circle('head',23,10,6)
        self.add_line('torso',(23,25),(23,33))
        self.add_polyline('left-arm',(23,25),(14,25),(8,31),(8,36))
        self.add_polyline('wave',(23,25),(32,25),(40,17),(40,7))
        self.add_polyline('legs',(17,42),(17,33),(23,33),(29,33),(29,42))
        for member in ('left-arm','wave','legs'):
            self.relate('connect','torso',member)
        self.relate('connect','left-arm','wave')
