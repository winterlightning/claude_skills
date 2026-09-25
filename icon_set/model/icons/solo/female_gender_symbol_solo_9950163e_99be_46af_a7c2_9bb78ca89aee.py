"""A Venus circle with an upright crossed stem. Lucide venus informs the circle and axial junctions; no defining feature omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9950163e-99be-46af-a7c2-9bb78ca89aee'
SOURCE_PATH = 'pictographic-primitives/users/gender female_9950163e-99be-46af-a7c2-9bb78ca89aee.svg'
AUTHOR = 'gpt-6'


class FemaleGenderSymbolSoloSource9950163E(Solo48):
    icon_id = 'female-gender-symbol-solo-source-9950163e'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    aliases = ()
    keywords = ('female', 'gender', 'venus', 'woman', 'symbol', 'sex', 'feminine')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-right', top, bottom, radius_x=radius)
        self.add_arc(name+'-left', bottom, top, radius_x=radius)
        self.add_contour(name, name+'-right', name+'-left', closed=True)

    def build(self) -> None:
        # Radial envelope center (24,24), radius 22; top and bottom ink touch.
        self.circle('ring',24,17,13)
        self.add_polyline('stem',(24,30),(24,39),(24,42))
        self.add_polyline('bar',(16,39),(24,39),(32,39))
        self.relate('connect','ring','stem')
        self.relate('connect','stem','bar')
