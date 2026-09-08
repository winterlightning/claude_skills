"""A leaning shepherd staff with a rounded hook. Bounds (8,2)-(40,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7169d0df-e69e-5ecc-8180-aa3f755ddd80'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology cane_7169d0df-e69e-5ecc-8180-aa3f755ddd80.svg'
AUTHOR = 'astra-chatgpt'


class ShepherdsCrook(Solo48):
    icon_id = 'shepherds-crook'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('crook', 'cane', 'staff', 'shepherd', 'hook', 'stick', 'symbol', 'pastoral')

    def build(self) -> None:
        self.add_line("shaft", (8,46), (20,12))
        self.add_arc("hook", (20,12), (40,12), radius_x=10)
        self.add_line("tip", (40,12), (40,18))
        self.add_contour("crook", "shaft", "hook", "tip")
