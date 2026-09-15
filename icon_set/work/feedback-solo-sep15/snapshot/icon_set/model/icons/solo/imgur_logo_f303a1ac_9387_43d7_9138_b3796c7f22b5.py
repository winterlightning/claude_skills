"""A square with a clipped lower right corner and a notched upper left corner holds a thick arrow pointing to the upper right.

Plan: Clipped square with a rising arrow; shared northeast directional construction.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected corner-down-right: shared arrow tip junction.
Simplification: Heavy arrow outline reduces to a single arrow stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f303a1ac-9387-43d7-9138-b3796c7f22b5'
SOURCE_PATH = 'pictographic-primitives/logos/imgur logo_f303a1ac-9387-43d7-9138-b3796c7f22b5.svg'
AUTHOR = 'gpt-6'


class ImgurLogo(Solo48):
    icon_id = 'imgur-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('imgur', 'images', 'sharing', 'arrow', 'logo', 'brand', 'upload')

    def build(self):
        self.add_polyline('frame',(20,6),(42,6),(42,28),(28,42),(6,42),(6,20),(20,6),closed=True)
        self.add_polyline('arrow',(17,31),(31,17))
        self.add_polyline('tip',(21,17),(31,17),(31,27))
        self.relate('connect','arrow','tip')
