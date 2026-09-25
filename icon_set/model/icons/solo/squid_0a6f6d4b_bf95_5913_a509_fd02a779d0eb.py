"""Diagonal squid with pointed mantle and two streaming tentacles. Bounds (6,6)-(42,42). No useful local squid match; coherent sweeping arcs, intentional diagonal asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a6f6d4b-bf95-5913-a509-fd02a779d0eb'
SOURCE_PATH = 'pictographic-primitives/animals/squid_0a6f6d4b-bf95-5913-a509-fd02a779d0eb.svg'
AUTHOR = 'gpt-6'


class SwimmingSquid(Solo48):
    icon_id = 'swimming-squid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('squid', 'sea', 'ocean', 'marine', 'cephalopod', 'tentacles', 'swim', 'calamari')

    def build(self) -> None:
        self.add_bezier('left-hook', (6, 28), *(((6, 30.21753356), (6.24779087, 32.5422399), (8, 34)),))
        self.add_arc('left-arm',(8,34),(19,25),radius_x=18,sweep=False)
        self.add_arc('mantle-left',(19,25),(42,6),radius_x=32)
        self.add_arc('mantle-right',(42,6),(30,32),radius_x=38,sweep=True)
        self.add_arc('right-arm',(30,32),(22,40),radius_x=14,sweep=False)
        self.add_bezier('right-hook', (22, 40), *(((23.4577601, 41.75220913), (25.78246644, 42), (28, 42)),))
        self.add_contour('squid','left-hook','left-arm','mantle-left','mantle-right','right-arm','right-hook')
