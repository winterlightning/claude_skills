"""A triangular bricklaying trowel with a bent neck and broad diagonal handle; surface marks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab28c662-ca28-5468-96ca-7027884adf42'
SOURCE_PATH = 'pictographic-primitives/tools/tools palette trowel_ab28c662-ca28-5468-96ca-7027884adf42.svg'
AUTHOR = 'gpt-6'

class BrickTrowel(Solo48):
    icon_id = 'brick-trowel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('trowel', 'palette knife', 'masonry', 'mortar', 'brick', 'plaster', 'construction', 'tool')

    def build(self) -> None:


        self.add_polyline('blade',(6,42),(10,16),(32,38),closed=True)
        self.add_polyline('neck',(21,27),(25,23),(25,17))
        self.add_polyline('handle',(25,17),(32,6),(42,16),(31,23),closed=True)
        self.relate('connect','neck','blade')
        self.relate('connect','neck','handle')
