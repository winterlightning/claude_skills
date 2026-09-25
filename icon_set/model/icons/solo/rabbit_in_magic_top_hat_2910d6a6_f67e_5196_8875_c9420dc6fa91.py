"""A rabbit with two upright ears and two eyes emerges from a top hat. Lucide rabbit informs rounded ear tips and minimal facial marks; hat-glasses informs the clear brim and tapered crown. Simplify oval eyes to dots and omit inner ear lines. Mirrored about x=24; the rabbit and hat are a natural magic-trick scene."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2910d6a6-f67e-5196-8875-c9420dc6fa91'
SOURCE_PATH = 'pictographic-primitives/products/magic rabbit hide_2910d6a6-f67e-5196-8875-c9420dc6fa91.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'rabbit-in-magic-top-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "products"
    aliases = ()
    keywords = ('magic', 'rabbit', 'top-hat', 'magician', 'trick', 'bunny', 'illusion', 'surprise')

    def build(self):
        # SQUARE centerline extremes (6, 6, 42, 42).

        # Paired ears share width/radius. Head and hat meet along a common brim.
        self.add_polyline('left-cheek',(11,33),(11,24),(10,14),(10,10))
        self.add_arc('left-ear',(10,10),(18,10),radius_x=4)
        self.add_polyline('forehead',(18,10),(18,15),(30,15),(30,10))
        self.add_arc('right-ear',(30,10),(38,10),radius_x=4)
        self.add_polyline('right-cheek',(38,10),(38,14),(37,24),(37,33))
        self.add_polyline('brim',(6,33),(11,33),(12,33),(36,33),(37,33),(42,33))
        self.relate('connect','left-cheek','left-ear')
        self.relate('connect','left-ear','forehead')
        self.relate('connect','forehead','right-ear')
        self.relate('connect','right-ear','right-cheek')
        self.relate('connect','left-cheek','brim')
        self.relate('connect','right-cheek','brim')
        self.add_dot('eye-left',(20,24))
        self.add_dot('eye-right',(28,24))
        self.add_polyline('hat',(12,33),(14,42),(34,42),(36,33))
        self.relate('connect','hat','brim')
