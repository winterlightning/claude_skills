"""An upright prehistoric egg with two zigzag bands."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b74494c1-2fee-487e-800b-589bbfa51024'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur egg_b74494c1-2fee-487e-800b-589bbfa51024.svg'
AUTHOR = 'gpt-6'


class DinosaurEgg(Solo48):
    icon_id = 'dinosaur-egg'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('egg', 'dinosaur', 'zigzag', 'pattern', 'prehistoric', 'shell', 'oval', 'decorated')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46).
        self.add_arc("upper-left",(5,28),(24,2),radius_x=19,radius_y=26)
        self.add_arc("upper-right",(24,2),(43,28),radius_x=19,radius_y=26)
        self.add_arc("bottom",(43,28),(5,28),radius_x=19,radius_y=18)
        self.add_contour("shell","upper-left","upper-right","bottom",closed=True)
        self.add_polyline("upper-band",(17,16),(24,20),(31,16))
        self.add_polyline("lower-band",(14,32),(24,36),(34,32))
