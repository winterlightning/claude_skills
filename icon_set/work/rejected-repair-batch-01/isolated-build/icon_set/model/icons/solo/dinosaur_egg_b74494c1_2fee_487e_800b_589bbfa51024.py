'Dinosaur egg: retain two chevron markings inside a smooth upright egg with generous margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b74494c1-2fee-487e-800b-589bbfa51024'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur egg_b74494c1-2fee-487e-800b-589bbfa51024.svg'
AUTHOR = 'gpt-6'


class DinosaurEgg(Solo48):
    icon_id = 'dinosaur-egg'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('egg', 'dinosaur', 'zigzag', 'pattern', 'prehistoric', 'shell', 'oval', 'decorated')

    def build(self) -> None:
        self.add_bezier('left',(24,4),((15,4),(8,20),(8,31)),((8,39),(15,44),(24,44)))
        self.add_bezier('right',(24,44),((33,44),(40,39),(40,31)),((40,20),(33,4),(24,4)))
        self.add_contour('shell','left','right',closed=True)
        self.add_polyline('upper-band',(20,19),(24,21),(28,19))
        self.add_polyline('lower-band',(17,32),(24,35),(31,32))
