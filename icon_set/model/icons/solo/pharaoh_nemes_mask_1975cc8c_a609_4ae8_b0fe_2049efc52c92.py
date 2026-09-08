"""An Egyptian pharaoh mask with flared nemes, a raised crest, and a hanging beard. Fine stripes and almond eye loops reduced for native-size clarity.

Construction: No useful Lucide subject match found.
Keyshape SQUARE; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1975cc8c-a609-4ae8-b0fe-2049efc52c92'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/sphinx_1975cc8c-a609-4ae8-b0fe-2049efc52c92.svg'
AUTHOR = 'astra-chatgpt'


class PharaohNemesMask(Solo48):
    icon_id = 'pharaoh-nemes-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('pharaoh', 'mask', 'tutankhamun', 'egyptian', 'nemes', 'ancient', 'tomb', 'gold')

    def build(self) -> None:
        self.add_arc("crown-left", (2,38), (14,10), radius_x=12, radius_y=28)
        self.add_line("crown-top-left", (14,10), (20,10))
        self.add_line("crown-top-middle", (20,10), (28,10))
        self.add_line("crown-top-right", (28,10), (34,10))
        self.add_arc("crown-right", (34,10), (46,38), radius_x=12, radius_y=28)
        for i,(a,b) in enumerate(zip([(46,38),(38,38),(38,46),(31,46)],[(38,38),(38,46),(31,46),(31,34)]),1):
            self.add_line(f"drape-right-{i}",a,b)
        self.add_arc("chin-right", (31,34), (24,38), radius_x=10)
        self.add_arc("chin-left", (24,38), (17,34), radius_x=10)
        for i,(a,b) in enumerate(zip([(17,34),(17,46),(10,46),(10,38)],[(17,46),(10,46),(10,38),(2,38)]),1):
            self.add_line(f"drape-left-{i}",a,b)
        # Each drape is part of the continuous outside silhouette.
        self.add_contour("outline", "crown-left", "crown-top-left", "crown-top-middle", "crown-top-right", "crown-right", "drape-right-1", "drape-right-2", "drape-right-3", "drape-right-4", "chin-right", "chin-left", "drape-left-1", "drape-left-2", "drape-left-3", "drape-left-4", closed=True)
        self.add_line("face-left", (14,10), (14,24))
        self.add_arc("jaw-left", (14,24), (17,34), radius_x=18, sweep=False)
        self.add_contour("face-left-side", "face-left", "jaw-left")
        self.add_line("face-right", (34,10), (34,24))
        self.add_arc("jaw-right", (34,24), (31,34), radius_x=18)
        self.add_contour("face-right-side", "face-right", "jaw-right")
        self.add_polyline("crest", (20,10), (20,2), (28,2), (28,10))
        self.add_line("beard", (24,38), (24,46))
        self.add_dot("eye-left", (21,22))
        self.add_dot("eye-right", (27,22))
        self.relate("connect", "outline", "face-left-side")
        self.relate("connect", "outline", "face-right-side")
        self.relate("connect", "outline", "crest")
        self.relate("connect", "outline", "beard")
