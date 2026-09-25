"""An infinity loop drawn as a single stroke, its two rounded lobes crossing at the centre.

Plan: Mirrored infinity lobes meeting at a shared central crossing.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: infinity: smooth paired lobes and central crossing.
Simplification: Source crossing simplified to one shared junction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ce8e1ba-097d-4525-a918-6d39f51da6d9'
SOURCE_PATH = 'pictographic-primitives/logos/irc galleria logo_5ce8e1ba-097d-4525-a918-6d39f51da6d9.svg'
AUTHOR = 'gpt-6'


class IrcGalleriaLogo(Solo48):
    icon_id = 'irc-galleria-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('irc-galleria', 'infinity', 'social', 'logo', 'brand', 'community', 'loop')

    def build(self):
        self.add_bezier('left',(24,24),((18,18),(16,8),(12,8)),((6,8),(4,14),(4,24)),((4,34),(6,40),(12,40)),((16,40),(18,30),(24,24)))
        self.add_bezier('right',(24,24),((30,18),(32,8),(36,8)),((42,8),(44,14),(44,24)),((44,34),(42,40),(36,40)),((32,40),(30,30),(24,24)))
        self.add_contour('leftloop','left',closed=True)
        self.add_contour('rightloop','right',closed=True)
        self.relate('connect','leftloop','rightloop')
