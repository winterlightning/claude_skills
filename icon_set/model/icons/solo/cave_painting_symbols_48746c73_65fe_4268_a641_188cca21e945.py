"""Three separate prehistoric marks: a branched staff, angular arch and tailed diamond."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48746c73-65fe-4268-a641-188cca21e945'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/caveman symbols_48746c73-65fe-4268-a641-188cca21e945.svg'
SOURCE_REFERENCES = (('1837ed86-65ba-5a7c-9d4a-bcb9c0b8972e', 'pictographic-primitives/culture/batch-01/history caveman symbols_1837ed86-65ba-5a7c-9d4a-bcb9c0b8972e.svg'),)


class CavePaintingSymbols(Solo48):
    icon_id = 'cave-painting-symbols'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('cave painting', 'petroglyph', 'rune', 'prehistoric', 'symbols', 'marks', 'ancient', 'rock art')

    def build(self) -> None:
        # SQUARE: visible extremes (0, 0, 48, 48); centerlines inset 2.
        self.add_polyline("staff", (2,2), (2,12), (2,24), (2,38))
        self.add_line("branch-upper", (2,12), (12,2))
        self.add_line("branch-lower", (2,24), (12,14))
        self.relate("connect", "staff", "branch-upper")
        self.relate("connect", "staff", "branch-lower")
        self.add_polyline("arch", (30,20), (30,6), (34,2), (46,12), (46,24))
        self.add_polyline("diamond", (22,22), (32,32), (22,42), (12,32), (22,22), closed=True)
        self.add_line("tail-left", (22,42), (18,46))
        self.add_line("tail-right", (22,42), (26,46))
        self.relate("connect", "diamond", "tail-left")
        self.relate("connect", "diamond", "tail-right")
        self.relate("connect", "tail-left", "tail-right")
