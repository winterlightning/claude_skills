"""Left-facing Corinthian helmet and tall crest. Bounds (5,2)-(43,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72959280-0cd4-51d8-9544-b784119c7e1d'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/spartan helmet_72959280-0cd4-51d8-9544-b784119c7e1d.svg'


class SpartanHelmet(Solo48):
    icon_id = 'spartan-helmet'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('helmet', 'spartan', 'corinthian', 'greek', 'warrior', 'crest', 'armour', 'soldier')

    def build(self) -> None:
        self.add_arc("dome-left", (5,25), (20,10), radius_x=15)
        self.add_arc("dome-right", (20,10), (35,25), radius_x=15)
        points = [(35,25), (35,32), (35,38), (27,35), (22,42), (11,46), (14,29), (23,25), (11,25), (5,32), (5,25)]
        for i, (a,b) in enumerate(zip(points, points[1:]),1): self.add_line(f"guard-{i}", a,b)
        self.add_contour("helmet", "dome-left", "dome-right", *[f"guard-{i}" for i in range(1,11)], closed=True)
        self.add_line("crest-front", (20,10), (17,2))
        self.add_arc("crest-top", (17,2), (43,28), radius_x=26)
        self.add_line("crest-back", (43,28), (43,36))
        self.add_line("crest-base", (43,36), (35,32))
        self.add_contour("crest", "crest-front", "crest-top", "crest-back", "crest-base")
        self.relate("connect", "helmet", "crest")
