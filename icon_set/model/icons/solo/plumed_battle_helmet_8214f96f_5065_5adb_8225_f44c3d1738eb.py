"""Right-facing battle helmet with trailing plume and flared neck guard. Bounds (5,2)-(43,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8214f96f-5065-5adb-8225-f44c3d1738eb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/spartan mask_8214f96f-5065-5adb-8225-f44c3d1738eb.svg'
AUTHOR = 'astra-chatgpt'


class PlumedBattleHelmet(Solo48):
    icon_id = 'plumed-battle-helmet'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('helmet', 'plume', 'spartan', 'greek', 'warrior', 'armour', 'battle', 'crest')

    def build(self) -> None:
        self.add_arc("dome-left", (13,25), (26,12), radius_x=13)
        self.add_arc("dome-right", (26,12), (39,25), radius_x=13)
        points = [(39,25), (43,33), (36,33), (39,42), (28,38), (22,28), (19,37), (17,37), (11,37), (13,25)]
        for i, (a,b) in enumerate(zip(points, points[1:]),1): self.add_line(f"face-{i}", a,b)
        self.add_contour("helmet", "dome-left", "dome-right", *[f"face-{i}" for i in range(1,10)], closed=True)
        self.add_line("plume-attachment", (26,12), (35,2))
        self.add_arc("plume", (35,2), (5,28), radius_x=30, radius_y=26, sweep=False)
        self.add_line("plume-end", (5,28), (5,38))
        self.add_contour("crest", "plume-attachment", "plume", "plume-end")
        self.add_polyline("neck", (17,37), (9,46), (23,43), (31,46), (28,38))
        self.relate("connect", "helmet", "crest")
        self.relate("connect", "helmet", "neck")
