"""A Venus circle with an upright crossed stem. Lucide venus informs the circle and axial junctions; no defining feature omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '988744ca-750f-510f-99e9-7f3857a7d07b'
SOURCE_PATH = 'pictographic-primitives/users/gender female_988744ca-750f-510f-99e9-7f3857a7d07b.svg'
AUTHOR = 'gpt-6'


class FemaleGenderSymbolSolo(Solo48):
    icon_id = 'female-gender-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
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
