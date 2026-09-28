'Pear-shaped vase: continuous rounded shoulders and bowl, with a slender neck. Exact VRECT_L bounds.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd5f7537-8a7a-4054-b479-eedbb6a2ed1e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.svg'
AUTHOR = 'gpt-6'


class SlenderPearShapedVase(Solo48):
    icon_id = 'slender-pear-shaped-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    categories = ("primitives", "decoration")
    aliases = ()
    keywords = ('vase', 'bottle', 'ceramic', 'vessel', 'decor', 'flared lip', 'pear shape')

    def build(self) -> None:
        # A slender neck leads into a broad rounded bowl; preserve the pear-shaped silhouette.
        self.add_line('lip',(16,4),(32,4))
        self.add_bezier('right',(32,4),((30,9),(30,14),(32,18)),((34,22),(40,23),(40,31)),((40,39),(33,44),(24,44)))
        self.add_bezier('left',(24,44),((15,44),(8,39),(8,31)),((8,23),(14,22),(16,18)),((18,14),(18,9),(16,4)))
        self.add_contour('vase','lip','right','left',closed=True)
